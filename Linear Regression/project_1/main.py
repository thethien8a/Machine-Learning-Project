"""
    Dự án xây dựng mô hình dự đoán lương của nhân viên AI/Data
"""
import numpy as np
import warnings
from utils import load_and_prepare_data
from feature_engineering import (
    process_skill_features,
    drop_irrelevant_features,
    create_interaction_features
)
from data_preprocessing import (
    target_encode_features,
    ordinal_encode_features,
    ohe_encode_features,
    standardize_features
)
from model_training import train_xgboost, train_random_forest
from evaluation import evaluate_model, plot_feature_importance

warnings.filterwarnings('ignore')

def main():
    """Ham chinh de chay toan bo pipeline xu ly du lieu."""
    # 1. Tai va chuan bi du lieu
    train_df, test_df = load_and_prepare_data('ai_job_dataset1.csv')
    
    # 2. Feature Engineering
    train_df, test_df = process_skill_features(train_df, test_df)
    train_df = drop_irrelevant_features(train_df)
    test_df = drop_irrelevant_features(test_df)

    # 3. Data Preprocessing (Encoding)
    high_cardinality_cols = ['employee_residence', 'company_location', 'job_title']
    train_df, test_df = target_encode_features(train_df, test_df, high_cardinality_cols)
    train_df, test_df = ordinal_encode_features(train_df, test_df)
    train_df, test_df = ohe_encode_features(train_df, test_df)
    
    # 4. Tach feature va target
    X_train = train_df.drop('salary_usd', axis=1)
    y_train = train_df['salary_usd']
    X_test = test_df.drop('salary_usd', axis=1)
    y_test = test_df['salary_usd']

    y_train_log = np.log1p(y_train)
    y_test_log = np.log1p(y_test)

    X_train = X_train.fillna(X_train.median())
    X_test = X_test.fillna(X_test.median())
    
    X_train = create_interaction_features(X_train)
    X_test = create_interaction_features(X_test)
    
    X_train, X_test = standardize_features(X_train, X_test)

    # 5. Huan luyen va danh gia mo hinh
    xgb_model = train_random_forest(X_train, y_train_log)
    
    print("\n\n--- Danh gia mo hinh Random Forest ---")
    print("\nDanh gia tren tap test:")
    evaluate_model(xgb_model, X_test, y_test_log)
    print("\nDanh gia tren tap train:")
    evaluate_model(xgb_model, X_train, y_train_log)
    
    plot_feature_importance(xgb_model, X_train.columns)

if __name__ == "__main__":
    main() 