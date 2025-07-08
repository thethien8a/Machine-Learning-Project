import pandas as pd
from sklearn.model_selection import train_test_split

def load_and_prepare_data(filepath):
    """Đọc dữ liệu, xử lý cơ bản và chia train/test."""
    df = pd.read_csv(filepath)
    
    df["posting_date"] = pd.to_datetime(df["posting_date"], errors='coerce')
    df["posting_day"] = df["posting_date"].dt.day
    df["posting_month"] = df["posting_date"].dt.month
    df["posting_year"] = df["posting_date"].dt.year
    
    train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)
    return train_df, test_df 