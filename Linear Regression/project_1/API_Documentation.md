# Hướng dẫn Xây dựng Backend API với FastAPI

Tài liệu này giải thích từng bước cách xây dựng một API để phục vụ mô hình dự đoán lương của chúng ta. API này sẽ là "bộ não" cho ứng dụng web sau này.

---

## 🏁 Mục tiêu cuối cùng

Tạo ra một dịch vụ web có thể:
1.  Nhận thông tin về một công việc (ví dụ: chức danh, kinh nghiệm, kỹ năng).
2.  Sử dụng mô hình đã huấn luyện (`salary_prediction_pipeline.joblib`) để dự đoán mức lương.
3.  Trả về kết quả dự đoán cho người dùng.

---

## 🛠️ Công cụ cần thiết

- **FastAPI:** Khung sườn (framework) để xây dựng API. Nó rất nhanh và dễ sử dụng.
- **Uvicorn:** Máy chủ (server) để chạy ứng dụng FastAPI của chúng ta.
- **Pydantic:** Dùng để định nghĩa cấu trúc dữ liệu và xác thực (validate) thông tin đầu vào.
- **Joblib:** Dùng để tải mô hình đã được lưu.

---

## 🏗️ Các bước xây dựng

### Bước 1: Chuẩn bị môi trường

Việc đầu tiên là đảm bảo chúng ta có đủ "nguyên liệu". Thêm các dòng sau vào tệp `requirements.txt` và chạy `pip install -r requirements.txt`:

```
fastapi
uvicorn[standard]
python-multipart 
```
*`uvicorn[standard]`* sẽ cài đặt uvicorn cùng với các thư viện hiệu năng cao khác.

### Bước 2: Tạo "Bản thiết kế" cho Dữ liệu đầu vào

Chúng ta cần quy định rõ ràng API sẽ nhận những thông tin gì. Chúng ta sẽ tạo một tệp `api.py` và định nghĩa một "khuôn mẫu" bằng Pydantic.

```python
# trong file api.py
from pydantic import BaseModel
from typing import Optional

# Định nghĩa một khuôn mẫu cho request
class JobPredictionRequest(BaseModel):
    job_title: str
    experience_level: str
    employment_type: str
    company_location: str
    company_size: str
    employee_residence: str
    remote_ratio: int
    required_skills: str
    education_required: str
    years_experience: int
    industry: str
    posting_date: str
    benefits_score: float

    # Ví dụ về dữ liệu mẫu sẽ trông như thế nào
    class Config:
        schema_extra = {
            "example": {
                "job_title": "Data Scientist",
                "experience_level": "MI",
                "employment_type": "FT",
                "company_location": "United States",
                "company_size": "M",
                "employee_residence": "United States",
                "remote_ratio": 100,
                "required_skills": "Python, SQL, PyTorch",
                "education_required": "Master",
                "years_experience": 4,
                "industry": "Technology",
                "posting_date": "2024-01-01",
                "benefits_score": 7.5
            }
        }
```
Khuôn mẫu này yêu cầu người dùng phải cung cấp tất cả các trường trên với đúng kiểu dữ liệu.

### Bước 3: Xây dựng "Cổng dịch vụ"

Bây giờ, chúng ta sẽ viết phần chính của API trong `api.py`.

```python
# tiếp tục trong file api.py
import joblib
import pandas as pd
import numpy as np
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 1. Khởi tạo ứng dụng FastAPI
app = FastAPI(title="Salary Prediction API", version="1.0")

# 2. Bật CORS để frontend có thể gọi
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cho phép tất cả
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Tải mô hình pipeline khi ứng dụng khởi động
#    Việc này chỉ xảy ra một lần, giúp API phản hồi nhanh hơn.
pipeline = joblib.load('salary_prediction_pipeline.joblib')

# 4. Tạo endpoint (cửa nhận yêu cầu)
@app.post("/predict", tags=["Prediction"])
def predict(request: JobPredictionRequest):
    """
    Nhận dữ liệu công việc và trả về mức lương dự đoán.
    """
    # Chuyển dữ liệu từ request thành một DataFrame mà pipeline hiểu được
    input_data = pd.DataFrame([request.dict()])
    
    # Dùng pipeline để dự đoán (kết quả ở thang log)
    log_prediction = pipeline.predict(input_data)[0]
    
    # Chuyển đổi ngược về giá trị lương thực tế
    prediction = np.expm1(log_prediction)
    
    return {"predicted_salary_usd": prediction}

@app.get("/", tags=["Health Check"])
def read_root():
    return {"status": "API is running"}

```

### Bước 4: Chạy và Kiểm tra

1.  Mở terminal trong thư mục dự án của bạn.
2.  Gõ lệnh sau để khởi động server:
    ```bash
    uvicorn api:app --reload
    ```
3.  Mở trình duyệt và truy cập vào địa chỉ `http://127.0.0.1:8000/docs`.
4.  Bạn sẽ thấy một giao diện tài liệu tự động. Tại đây bạn có thể mở endpoint `/predict`, nhấn "Try it out", điền thông tin mẫu và xem kết quả API trả về.

Nếu tất cả các bước trên thành công, bạn đã có một backend API hoàn chỉnh, sẵn sàng để kết nối với một giao diện người dùng! 