# Giải Thích Chi Tiết `Dockerfile`

Tài liệu này giải thích từng dòng lệnh trong `Dockerfile` của dự án, giúp bạn hiểu rõ cách nó hoạt động để đóng gói ứng dụng.

---

## Giải Thích Theo Ngôn Ngữ "Dân Dã" (Dễ Hiểu)

Hãy coi `Dockerfile` như một "công thức nấu ăn" và Docker là người đầu bếp.

-   **`FROM python:3.9-slim as builder`**
    -   **"Lấy một cái thớt sạch (môi trường) có sẵn Python 3.9."**
    -   `as builder`: Đặt tên cho cái thớt này là "builder" để lát nữa dùng lại.

-   **`WORKDIR /app`**
    -   **"Tất cả nguyên liệu và thao tác từ giờ sẽ làm trong một cái tô tên là /app."**

-   **`COPY requirements.txt .`**
    -   **"Chép danh sách gia vị (file requirements.txt) từ máy tính của tôi vào trong tô."**

-   **`RUN pip wheel ...`**
    -   **"Dùng pip để sơ chế trước các gói gia vị này thành dạng 'viên nén' (wheels) để lát nữa nấu cho nhanh."** Đây là bước tối ưu hóa.

-   **`FROM python:3.9-slim`**
    -   **"Lấy một cái nồi sạch khác, cũng có sẵn Python 3.9."** (Đây là nồi để nấu món ăn cuối cùng).

-   **`COPY --from=builder /app/wheels /wheels`**
    -   **"Lấy các 'viên nén' gia vị đã sơ chế ở cái thớt 'builder' lúc nãy và bỏ vào nồi này."**

-   **`RUN pip install --no-cache /wheels/*`**
    -   **"Bỏ hết các viên nén gia vị vào nồi và hòa tan chúng."** (Cài đặt các thư viện).

-   **`COPY . .`**
    -   **"Bỏ tất cả nguyên liệu còn lại (code Python, thư mục frontend...) vào trong nồi."**

-   **`EXPOSE 8000`**
    -   **"Nói với người phục vụ rằng món ăn này sẽ được đưa ra ở cửa số 8000."** (Thông báo port).

-   **`CMD ["uvicorn", ...]`**
    -   **"Đây là công thức cuối cùng để bật bếp và bắt đầu nấu món ăn (chạy server)."**

---

## Phân Tích Chi Tiết Theo Ngôn Ngữ "Dân IT"

Đây là một `Dockerfile` sử dụng kỹ thuật **multi-stage build**, một best practice để tạo ra các Docker image vừa tinh gọn (lightweight) vừa an toàn.

#### **Giai Đoạn 1: `builder` - Môi trường Build Tạm Thời**

```dockerfile
# STAGE 1: Build dependencies
FROM python:3.9-slim as builder
```
-   **`FROM python:3.9-slim as builder`**: Khởi tạo một build stage mới từ base image là `python:3.9-slim`. Đây là một image nhẹ, chỉ chứa những gì cần thiết để chạy Python. Đặt tên cho stage này là `builder` để có thể tham chiếu đến nó sau này.

```dockerfile
WORKDIR /app
```
-   **`WORKDIR /app`**: Thiết lập thư mục làm việc mặc định bên trong container là `/app`. Tất cả các lệnh sau đó (`COPY`, `RUN`) sẽ được thực thi trong thư mục này.

```dockerfile
COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt
```
-   **`COPY requirements.txt .`**: Sao chép chỉ file `requirements.txt` từ máy host vào thư mục `/app` của container.
-   **`RUN pip wheel ...`**: Đây là bước tối ưu hóa quan trọng.
    -   `pip wheel`: Thay vì cài đặt trực tiếp, lệnh này sẽ build tất cả các dependencies trong `requirements.txt` thành các file `.whl` (wheel). Wheel là một định dạng distribution đã được pre-compiled, giúp việc cài đặt ở stage sau nhanh hơn nhiều.
    -   `--no-cache-dir`: Không lưu cache của pip để giữ cho image layer này gọn nhất có thể.
    -   `--no-deps`: Chỉ build các package được liệt kê trong `requirements.txt`, không build các package phụ thuộc của chúng.
    -   `--wheel-dir /app/wheels`: Chỉ định thư mục đầu ra cho các file `.whl` là `/app/wheels`.

**Kết quả của Stage 1:** Một image tạm thời chứa một thư mục `/app/wheels` với đầy đủ các package đã được build sẵn. Toàn bộ build toolchain (như `gcc`, các thư viện C,...) cần thiết để build các wheel này sẽ chỉ tồn tại trong layer của stage này và sẽ bị loại bỏ sau đó.

---

#### **Giai Đoạn 2: `final` - Image Production Cuối Cùng**

```dockerfile
# STAGE 2: Final application
FROM python:3.9-slim
```
-   **`FROM python:3.9-slim`**: **Bắt đầu lại từ đầu** với một base image `python:3.9-slim` hoàn toàn mới và sạch sẽ. Điều này đảm bảo image cuối cùng không chứa bất kỳ build artifact hay thư viện không cần thiết nào từ stage 1.

```dockerfile
WORKDIR /app
```
-   **`WORKDIR /app`**: Thiết lập lại thư mục làm việc.

```dockerfile
COPY --from=builder /app/wheels /wheels
RUN pip install --no-cache /wheels/*
```
-   **`COPY --from=builder ...`**: Đây là cú pháp đặc trưng của multi-stage build. Nó sao chép thư mục `/app/wheels` từ stage `builder` vào thư mục `/wheels` trong image hiện tại.
-   **`RUN pip install ...`**: Cài đặt tất cả các dependencies từ các file wheel đã được sao chép. Vì đây là các file pre-compiled, bước này sẽ thực thi rất nhanh và không cần build toolchain.

```dockerfile
COPY . .
```
-   **`COPY . .`**: Sao chép toàn bộ nội dung của thư mục dự án trên máy host vào thư mục `/app` của container. Docker caching sẽ hoạt động hiệu quả ở đây: nếu bạn chỉ thay đổi code Python mà không thay đổi `requirements.txt`, các layer cài đặt dependency sẽ được tái sử dụng, giúp build nhanh hơn đáng kể.

```dockerfile
EXPOSE 8000
```
-   **`EXPOSE 8000`**: Metadata. Thông báo cho Docker rằng container này sẽ lắng nghe trên port `8000` lúc chạy. Nó không tự động mở port, nhưng là một hình thức tài liệu hóa quan trọng cho người vận hành.

```dockerfile
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
```
-   **`CMD [...]`**: Định nghĩa lệnh mặc định sẽ được thực thi khi container khởi chạy.
    -   `--host 0.0.0.0`: Bind server với tất cả các network interface có sẵn bên trong container, cho phép các kết nối từ bên ngoài (thông qua port mapping của Docker) có thể truy cập được.
    
### Lợi Ích Của Cách Viết Này
1.  **Image Size Nhỏ Hơn:** Image cuối cùng không chứa các build dependencies.
2.  **Bảo Mật Tốt Hơn:** Bề mặt tấn công bị thu hẹp vì các công cụ build không có trong image production.
3.  **Tận Dụng Docker Cache:** Tách việc cài đặt dependency ra khỏi việc sao chép code giúp build nhanh hơn. 