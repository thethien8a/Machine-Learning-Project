import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV
import xgboost as xgb

def train_linear_regression(X_train, y_train):
    """Huấn luyện mô hình Linear Regression."""
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
    model = RandomForestRegressor(
        n_estimators=1000, min_samples_split=2, min_samples_leaf=4,
        max_features=1.0, max_depth=10, n_jobs=-1, random_state=42
    )
    model.fit(X_train, y_train)
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