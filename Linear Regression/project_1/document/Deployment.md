# Hướng Dẫn Triển Khai Ứng Dụng Dự Đoán Lương

Tài liệu này sẽ hướng dẫn bạn quy trình đầy đủ để triển khai (deploy) ứng dụng Machine Learning này lên môi trường production, giúp người dùng trên toàn thế giới có thể truy cập.

---

## 1. Tổng Quan & Triết Lý Triển Khai

Mục tiêu của chúng ta là đóng gói toàn bộ ứng dụng (cả backend FastAPI và frontend HTML/CSS/JS) vào một "chiếc hộp" duy nhất và đưa "chiếc hộp" đó lên một máy chủ trên Internet.

**Phương pháp hiện đại nhất để làm điều này là sử dụng Containerization với Docker.**

-   **Docker là gì?** Hãy tưởng tượng Docker như một công cụ giúp bạn tạo ra các container.
-   **Container là gì?** Là một gói độc lập, chứa mọi thứ ứng dụng của bạn cần để chạy:
    -   Mã nguồn (Python, HTML, CSS, JS)
    -   Các thư viện (dependencies) đã được cài đặt (FastAPI, scikit-learn, etc.)
    -   File model đã huấn luyện (`.joblib`)
    -   Các cài đặt hệ thống cần thiết.

**Tại sao lại dùng Docker?**
-   **Tính nhất quán:** Ứng dụng chạy trên máy bạn thế nào thì sẽ chạy y hệt như vậy trên máy chủ, tránh lỗi "It works on my machine".
-   **Tính di động:** "Chiếc hộp" container này có thể chạy trên bất kỳ nền tảng đám mây nào (Google Cloud, AWS, Render, etc.) mà không cần thay đổi.
-   **Dễ dàng quản lý:** Đơn giản hóa việc khởi động, dừng, và cập nhật ứng dụng.

---

## 2. Các Bước Triển Khai

Quy trình sẽ gồm 3 bước chính:

1.  **Chuẩn bị ứng dụng:** Chỉnh sửa một chút để backend và frontend có thể "sống chung một nhà".
2.  **Container hóa ứng dụng:** Viết "công thức" (`Dockerfile`) để đóng gói ứng dụng.
3.  **Chọn nền tảng và triển khai:** Đưa container của bạn lên một dịch vụ đám mây.

### **Bước 1: Chuẩn Bị Ứng Dụng (Self-Contained Service)**

Để đơn giản hóa việc triển khai, chúng ta sẽ cấu hình để **backend FastAPI có thể phục vụ luôn cả frontend**. Điều này biến ứng dụng của bạn thành một dịch vụ độc lập, tự phục vụ, không cần một web server riêng cho frontend.

**Hành động:** Mở file `api.py` và thêm đoạn code sau.

```python
# Thêm các import này ở đầu file
from fastapi import FastAPI, Response
from fastapi.staticfiles import StaticFiles

# ... (khởi tạo app = FastAPI())

# --- SERVE FRONTEND ---
# Mount thư mục 'frontend' để phục vụ các file tĩnh
# URL /static sẽ trỏ đến thư mục 'frontend' của bạn
app.mount("/static", StaticFiles(directory="frontend"), name="static")

# Tạo một route để phục vụ file index.html khi người dùng truy cập vào trang chủ
@app.get("/", include_in_schema=False)
async def root():
    with open("frontend/index.html", "r") as f:
        html_content = f.read()
    return Response(content=html_content, media_type="text/html")

# --- PHẦN API CÒN LẠI ---
# @app.post("/predict")
# ...
```

### **Bước 2: Container Hóa với `Dockerfile`**

Bây giờ chúng ta sẽ tạo "công thức" để Docker xây dựng container.

**Hành động:** Tạo một file mới tên là `Dockerfile` (không có đuôi file) trong thư mục gốc của dự án với nội dung sau.

```dockerfile
# STAGE 1: Build dependencies - Tối ưu hóa dung lượng image
FROM python:3.12-slim-bullseye as builder

WORKDIR /app

# Sao chép file requirements và cài đặt các "bánh xe" (wheels)
# Điều này giúp tăng tốc build và giảm dung lượng
COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

# STAGE 2: Final application - Xây dựng image cuối cùng
FROM python:3.12-slim-bullseye

WORKDIR /app

# Lấy các "bánh xe" đã được build từ stage 1
COPY --from=builder /app/wheels /wheels

# Cài đặt dependencies từ các file wheel đã có sẵn
RUN pip install --no-cache /wheels/*

# Sao chép toàn bộ mã nguồn còn lại của dự án vào image
# (api.py, feature_engineering.py, model .joblib, và thư mục frontend)
COPY . .

# Mở cổng 8000 để thế giới bên ngoài có thể giao tiếp với ứng dụng
EXPOSE 8000

# Lệnh để khởi chạy ứng dụng khi container bắt đầu
# Dùng --host 0.0.0.0 để API có thể được truy cập từ bên ngoài container
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
```

### **Bước 3: Chọn Nền Tảng và Triển Khai**

Sau khi có `Dockerfile`, bạn đã sẵn sàng để triển khai. Dưới đây là hai lựa chọn phổ biến, từ dễ đến khó.

#### **Lựa chọn A: Render (Đơn giản, hiện đại - Khuyên dùng)**

Render là một nền tảng PaaS (Platform as a Service) cực kỳ thân thiện với người mới bắt đầu. Họ sẽ tự động đọc `Dockerfile` của bạn, xây dựng image và chạy ứng dụng.

**Các bước thực hiện:**

1.  **Đẩy code lên GitHub:** Đảm bảo toàn bộ code của bạn (bao gồm cả `Dockerfile` mới) đã được đẩy lên một repository trên GitHub.
2.  **Tạo tài khoản Render:** Truy cập [render.com](https://render.com/) và đăng ký một tài khoản (có gói miễn phí).
3.  **Tạo "New Web Service":**
    -   Trên dashboard của Render, chọn "New" -> "Web Service".
    -   Kết nối tài khoản GitHub của bạn và chọn repository của dự án này.
4.  **Cấu hình dịch vụ:**
    -   **Name:** Đặt tên cho ứng dụng của bạn (ví dụ: `salary-predictor-app`).
    -   **Region:** Chọn khu vực gần bạn nhất (ví dụ: `Singapore`).
    -   **Environment:** Chọn `Docker`. Render sẽ tự động phát hiện `Dockerfile` của bạn.
    -   **Instance Type:** Chọn gói `Free`.
5.  **Deploy:** Nhấn nút "Create Web Service". Render sẽ bắt đầu quá trình build và deploy. Quá trình này có thể mất vài phút.
6.  **Truy cập:** Sau khi hoàn tất, Render sẽ cung cấp cho bạn một URL có dạng `https://your-app-name.onrender.com`. Truy cập vào URL này để xem ứng dụng của bạn hoạt động!

#### **Lựa chọn B: Google Cloud Run (Mạnh mẽ, Serverless)**

Đây là lựa chọn mạnh mẽ hơn, ứng dụng của bạn sẽ tự động co giãn (scale) theo lưu lượng truy cập và bạn chỉ trả tiền cho những gì bạn sử dụng.

**Các bước thực hiện (ở mức cao):**

1.  **Cài đặt Google Cloud SDK (`gcloud`):** Làm theo hướng dẫn trên trang chủ Google Cloud.
2.  **Xác thực Docker:** Chạy lệnh `gcloud auth configure-docker` để cho phép Docker đẩy image lên Google.
3.  **Build Docker image:**
    -   Mở terminal trong thư mục dự án.
    -   Chạy lệnh: `docker build -t gcr.io/YOUR_PROJECT_ID/salary-predictor .` (thay `YOUR_PROJECT_ID` bằng ID dự án Google Cloud của bạn).
4.  **Đẩy image lên Google Container Registry:**
    -   Chạy lệnh: `docker push gcr.io/YOUR_PROJECT_ID/salary-predictor`
5.  **Triển khai trên Cloud Run:**
    -   Truy cập vào Google Cloud Console, tìm đến dịch vụ Cloud Run.
    -   Tạo một service mới, chọn image bạn vừa đẩy lên.
    -   Cấu hình các thông số như port (8000), CPU, memory và cho phép "Allow unauthenticated invocations" để mọi người có thể truy cập.
    -   Sau khi deploy, bạn sẽ nhận được một URL để truy cập ứng dụng.

---

**Khuyến nghị của tôi:** Hãy bắt đầu với **Render**. Nó cực kỳ đơn giản và sẽ giúp bạn có được cảm giác thành tựu nhanh chóng khi thấy ứng dụng của mình chạy trên Internet. Sau khi đã quen, bạn có thể khám phá các nền tảng phức tạp hơn như Google Cloud Run hoặc AWS. 