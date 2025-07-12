from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np
from typing import Optional

# 1. Định nghĩa khuôn mẫu (schema) cho dữ liệu đầu vào bằng Pydantic
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
    industry: Optional[str] = None
    posting_date: str
    benefits_score: Optional[float] = None

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

# 2. Khởi tạo ứng dụng FastAPI
app = FastAPI(
    title="Salary Prediction API",
    description="An API to predict job salaries based on input features in job description",
    version="1.0.0"
)

# 3. Bật CORS (Cross-Origin Resource Sharing)
# Cho phép frontend (chạy ở một địa chỉ khác) có thể gọi đến API này.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Thận trọng: Cho phép tất cả các nguồn. Trong sản phẩm thực tế, bạn nên giới hạn lại.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 4. Tải pipeline đã được huấn luyện
# Việc này chỉ xảy ra một lần khi ứng dụng khởi động.
try:
    pipeline = joblib.load('salary_prediction_pipeline.joblib')
    print("Pipeline được load thành công !")
except FileNotFoundError:
    print("Lỗi: salary_prediction_pipeline.joblib không được tìm thấy.")
    pipeline = None

# 5. Tạo các endpoints
@app.get("/", tags=["Health Check"])
def read_root():
    """Endpoint gốc để kiểm tra xem API có đang hoạt động không."""
    return {"status": "ok", "message": "Salary Prediction API is running."}

@app.post("/predict", tags=["Prediction"])
def predict(request: JobPredictionRequest):
    """
    Nhận dữ liệu công việc và trả về mức lương dự đoán.
    """
    if pipeline is None:
        return {"error": "Model pipeline is not loaded. Please check the server logs."}, 500

    try:
        # Chuyển dữ liệu từ request Pydantic thành một DataFrame có 1 hàng
        input_data = pd.DataFrame([request.dict()])
        
        # Dùng pipeline để dự đoán (kết quả ở thang log)
        log_prediction = pipeline.predict(input_data)[0]
        
        # Chuyển đổi ngược về giá trị lương thực tế
        prediction = np.expm1(log_prediction)
        
        return {"predicted_salary_usd": round(prediction, 2)}

    except Exception as e:
        return {"error": f"An error occurred during prediction: {str(e)}"}, 400 