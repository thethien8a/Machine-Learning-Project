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