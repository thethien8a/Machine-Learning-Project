import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV
import xgboost as xgb

def train_linear_regression(X_train, y_train):
    """Huấn luyện mô hình Linear Regression."""
    print("\nBat dau huan luyen mo hinh Linear Regression...")
    model = LinearRegression()
    model.fit(X_train, y_train)
    print("Mo hinh Linear Regression da duoc huan luyen thanh cong.")
    return model

def train_random_forest(X_train, y_train):
    """Huấn luyện mô hình RandomForestRegressor."""
    print("\nBat dau huan luyen mo hinh Random Forest...")
    model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)
    print("Mo hinh Random Forest da duoc huan luyen thanh cong.")
    return model

def train_to_not_overfit_rdf(X_train, y_train):
    """Huan luyen mo hinh RandomForestRegressor voi cac tham so de giam overfitting."""
    print("\nBat dau huan luyen mo hinh Random Forest (chong overfitting)...")
    model = RandomForestRegressor(
        n_estimators=100, max_depth=15, min_samples_leaf=5, 
        min_samples_split=10, random_state=42, n_jobs=-1
    )
    model.fit(X_train, y_train)
    print("Mo hinh Random Forest (chong overfitting) da duoc huan luyen thanh cong.")
    return model

def tune_rf_with_fixed_hyperparameters(X_train, y_train):
    """Huấn luyện RF với các tham số cố định từ kết quả tìm kiếm."""
    print("\nBat dau huan luyen mo hinh Random Forest voi tham so duoc lay tu ket qua chay tren gg colab ...")
    model = RandomForestRegressor(
        n_estimators=700, min_samples_split=10, min_samples_leaf=2,
        max_features=1.0, max_depth=10, n_jobs=-1, random_state=42
    )
    model.fit(X_train, y_train)
    print("Mo hinh Random Forest da duoc huan luyen thanh cong.")
    return model
    
def tune_rf_with_randomized_search(X_train, y_train):
    """Tinh chỉnh hyperparameter cho RandomForestRegressor."""
    print("\nBat dau tinh chinh hyperparameter voi RandomizedSearchCV...")
    param_distributions = {
        'n_estimators': [int(x) for x in np.linspace(start=100, stop=1000, num=10)],
        'max_depth': [int(x) for x in np.linspace(10, 100, num=10)] + [None],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4],
        'max_features': [1.0, 'sqrt']
    }
    rf = RandomForestRegressor(random_state=42)
    rf_random = RandomizedSearchCV(
        estimator=rf, param_distributions=param_distributions, n_iter=50, 
        cv=3, verbose=2, random_state=42, n_jobs=-1
    )
    rf_random.fit(X_train, y_train)
    print("\nTo hop tham so tot nhat duoc tim thay:")
    print(rf_random.best_params_)
    print("\nMô hình Random Forest với tham số tốt nhất đã được huấn luyện.")
    return rf_random.best_estimator_

def tune_xgboost_with_randomized_search(X_train, y_train):
    """
    Tinh chỉnh hyperparameter cho XGBoost Regressor su dung RandomizedSearchCV.
    """
    print("\nBat dau tinh chinh hyperparameter cho XGBoost voi RandomizedSearchCV...")
    
    # Dinh nghia luoi tham so de tim kiem
    param_distributions = {
        'n_estimators': [int(x) for x in np.linspace(start=100, stop=1200, num=12)],
        'learning_rate': [0.01, 0.05, 0.1, 0.2],
        'max_depth': [3, 4, 5, 6, 8, 10],
        'subsample': [0.7, 0.8, 0.9, 1.0],
        'colsample_bytree': [0.7, 0.8, 0.9, 1.0],
        'gamma': [0, 0.1, 0.2, 0.5]
    }
    
    # Khoi tao model co so
    xgb_model = xgb.XGBRegressor(objective='reg:squarederror', random_state=42, n_jobs=-1)
    
    # Khoi tao RandomizedSearchCV
    xgb_random = RandomizedSearchCV(
        estimator=xgb_model,
        param_distributions=param_distributions,
        n_iter=50,  # So luong to hop tham so se thu
        cv=3,       # So fold cho cross-validation
        verbose=2,
        random_state=42,
        n_jobs=-1   # Su dung tat ca CPU cores
    )
    
    # Fit de tim kiem
    xgb_random.fit(X_train, y_train)
    
    print("\nTo hop tham so XGBoost tot nhat duoc tim thay:")
    print(xgb_random.best_params_)
    
    print("\nMo hinh XGBoost voi tham so tot nhat da duoc huan luyen.")
    return xgb_random.best_estimator_
      
def train_xgboost(X_train, y_train):
    """Huan luyen mo hinh XGBoost Regressor."""
    print("\nBat dau huan luyen mo hinh XGBoost...")
    model = xgb.XGBRegressor(
        objective='reg:squarederror', n_estimators=1000, learning_rate=0.05,
        max_depth=6, subsample=0.8, colsample_bytree=0.8, 
        random_state=42, n_jobs=-1
    )
    model.fit(X_train, y_train, verbose=False)
    print("Mo hinh XGBoost da duoc huan luyen thanh cong.")
    return model 

def train_xgboost_with_fixed_hyperparameters(X_train, y_train):
    """Huấn luyện mô hình XGBoost với các tham số cố định tìm được khi chạy trên GG Colab."""
    model = xgb.XGBRegressor(
        subsample=0.8, n_estimators=800, max_depth=5, learning_rate=0.1, gamma=0.2, colsample_bytree=0.7,
        random_state=42, n_jobs=-1
    )
    model.fit(X_train, y_train, verbose=False)
    print("Mô hình XGBoost với tham số lấy từ google colab đã được huấn luyện.")
    return model
