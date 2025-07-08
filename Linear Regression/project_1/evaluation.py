import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def evaluate_model(model, X_test, y_test_log):
    """Đánh giá mô hình và in ra các metrics."""
    y_pred_log = model.predict(X_test)
    
    y_test_original = np.expm1(y_test_log)
    y_pred_original = np.expm1(y_pred_log)
    
    mae = mean_absolute_error(y_test_original, y_pred_original)
    mse = mean_squared_error(y_test_original, y_pred_original)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test_original, y_pred_original)
    
    evaluation_summary = (
        f"\n--- Model Evaluation ---\n"
        f"Mean Absolute Error (MAE): ${mae:,.2f}\n"
        f"Mean Squared Error (MSE): ${mse:,.2f}\n"
        f"Root Mean Squared Error (RMSE): ${rmse:,.2f}\n"
        f"R-squared (R2): {r2:.2f}\n"
        f"------------------------------------------------"
    )
    print(evaluation_summary)
    
    return y_pred_log

def plot_feature_importance(model, columns, top_n=20):
    """Vẽ biểu đồ top N feature quan trọng nhất của mô hình."""
    importances = model.feature_importances_
    feature_importance_df = pd.DataFrame({'feature': columns, 'importance': importances})
    feature_importance_df = feature_importance_df.sort_values(by='importance', ascending=False).head(top_n)
    
    plt.figure(figsize=(10, top_n / 2))
    sns.barplot(x='importance', y='feature', data=feature_importance_df, palette='viridis')
    plt.title(f'Top {top_n} features quan trọng nhất')
    plt.tight_layout()
    plt.show()

def plot_correlation_matrix(df):
    """Vẽ ma trận tương quan."""
    copy_df = df.copy().select_dtypes(include=["int", "float"])
    plt.figure(figsize=(12, 8))
    sns.heatmap(copy_df.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Ma trận tương quan')
    plt.tight_layout()
    plt.show()
    
def show_histogram_all_columns(df):
    """Hiển thị histogram cho tất cả các cột số."""
    numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()
    if not numeric_columns:
        print("Không có cột số nào để hiển thị histogram.")
        return
    df[numeric_columns].hist(bins=30, figsize=(15, 10), layout=(-1, 3))
    plt.tight_layout()
    plt.show() 