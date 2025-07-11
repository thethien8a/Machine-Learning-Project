"""
    Dự án xây dựng mô hình dự đoán lương của nhân viên AI/Data
    Script để xây dựng, huấn luyện, và lưu trữ pipeline hoàn chỉnh.
"""
import numpy as np
import warnings
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder
from sklearn.compose import ColumnTransformer, make_column_selector
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer, KNNImputer  # Thêm KNNImputer
import category_encoders as ce
import xgboost as xgb

# Import các transformer tùy chỉnh
from feature_engineering import (
    SkillFeatureTransformer,
    DropIrrelevantFeatures,
    TargetEncoderWrapper,
    DateFeatureExtractor  # Thêm DateFeatureExtractor
)
from evaluation import evaluate_model

warnings.filterwarnings('ignore')

def build_and_train_pipeline():
    """Hàm chính để xây dựng pipeline, huấn luyện và lưu model."""
    # 1. Tải và chia dữ liệu
    print("Đang tải dữ liệu...")
    df = pd.read_csv('ai_job_dataset1.csv')
    X = df.drop('salary_usd', axis=1)
    y = df['salary_usd']
    
    y_log = np.log1p(y)

    X_train, X_test, y_train_log, y_test_log = train_test_split(X, y_log, test_size=0.2, random_state=42)
    y_train_orig = np.expm1(y_train_log)

    print("Định nghĩa các bước của pipeline...")
    # 2. Định nghĩa các nhóm cột
    ordinal_cols = ['experience_level', 'company_size', 'education_required']
    target_cols = ['employee_residence', 'company_location', 'job_title']
    ohe_cols = ['employment_type', 'company_industry'] 
    
    numeric_cols = [
        'remote_ratio', 'years_experience', 'benefits_score', 
        'top_5_skills_common', 'top_5_skills_highest_salary',
        'posting_year', 'posting_month', 'posting_day'
    ]

    # 3. Định nghĩa các pipeline con
    numeric_transformer = Pipeline(steps=[
        ('imputer', KNNImputer(n_neighbors=5)), # Sửa: Dùng KNNImputer
        ('scaler', StandardScaler())])
    
    ordinal_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('encoder', OrdinalEncoder(categories=[
            ['EN', 'MI', 'SE', 'EX'], ['S', 'M', 'L'], ['Associate', 'Bachelor', 'Master', 'PhD']
        ], handle_unknown='use_encoded_value', unknown_value=-1))])

    ohe_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))])
        
    # Sửa lại để sử dụng Wrapper
    target_transformer = TargetEncoderWrapper()

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_cols), # Sửa: dùng danh sách cột số mới
            ('ord', ordinal_transformer, ordinal_cols),
            ('ohe', ohe_transformer, ohe_cols),
            ('target', target_transformer, target_cols)
        ],
        remainder='drop' 
    )

    # 4. Xây dựng Pipeline chính
    final_pipeline = Pipeline(steps=[
        ('date_features', DateFeatureExtractor()), # Thêm bước xử lý ngày tháng
        ('skill_features', SkillFeatureTransformer()),
        ('drop_features', DropIrrelevantFeatures()),
        ('preprocessor', preprocessor),
        ('regressor', xgb.XGBRegressor(
            subsample=0.9, n_estimators=400, max_depth=10, learning_rate=0.05, 
            gamma=0.2, colsample_bytree=0.9, random_state=42, n_jobs=-1
        ))
    ])

    # 5. Huấn luyện pipeline - Bây giờ đơn giản hơn
    print("Bắt đầu huấn luyện pipeline hoàn chỉnh...")
    # fit_params không còn cần thiết nữa
    final_pipeline.fit(X_train, y_train_log)
    print("Đã huấn luyện xong!")

    # 6. Đánh giá mô hình
    print("\n--- Đánh giá trên tập test ---")
    evaluate_model(final_pipeline, X_test, y_test_log)
    print("\n--- Đánh giá trên tập train ---")
    evaluate_model(final_pipeline, X_train, y_train_log)
    
    # # 7. Lưu pipeline
    # print("\nĐang lưu pipeline vào file 'salary_prediction_pipeline.joblib'...")
    # joblib.dump(final_pipeline, 'salary_prediction_pipeline.joblib')
    # print("Pipeline đã được lưu thành công!")


if __name__ == "__main__":
    build_and_train_pipeline() 