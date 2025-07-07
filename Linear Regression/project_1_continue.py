""" 
    Ở project này, tôi tập trung vào việc mã hóa, feature engineering và huấn luyện mô hình Linear Regression. 
    Tôi sẽ không tập trung vào EDA cũng như tiền xử lý dữ liệu (Do file jupyter notebook đã có và thực hiền điều đó).
    
    Tuy nhiên, nếu trong 1 project thực tế. Thứ tự thông thường bạn cần thực hiện là:
    Đọc dữ liệu - EDA - Tiền xử lý dữ liệu - Feature Engineering - Huấn luyện mô hình - Đánh giá mô hình - Tối ưu mô hình - Deploy
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')

def get_top_5_common_skills_by_job(skill_data):
    """Lấy top 5 skills phổ biến nhất cho từng job_title"""
    top_skills_dict = {}
    
    for job_title in skill_data['job_title'].unique():
        # Đếm tần suất skills cho job_title cụ thể
        job_skills = skill_data[skill_data['job_title'] == job_title]
        top_5_skills = (job_skills['required_skills']
                       .value_counts()
                       .head(5)
                       .index.tolist())
        top_skills_dict[job_title] = top_5_skills
    
    return top_skills_dict

def get_top_5_highest_salary_skills_by_job(skill_data):
    """Lấy top 5 skills có lương cao nhất cho từng job_title"""
    top_salary_skills_dict = {}
    
    for job_title in skill_data['job_title'].unique():
        # Lọc data cho job_title cụ thể
        job_data = skill_data[skill_data['job_title'] == job_title]
        
        # Tính lương trung bình cho mỗi skill và lấy top 5
        top_5_skills = (job_data.groupby('required_skills')['salary_usd']
                       .median()
                       .sort_values(ascending=False)
                       .head(5)
                       .index.tolist())
        
        top_salary_skills_dict[job_title] = top_5_skills
    
    return top_salary_skills_dict

def engineer_skill_features(df, top_common_skills, top_salary_skills):
    """Áp dụng feature engineering cho skills vào dataframe."""
    df["required_skills"] = df["required_skills"].str.split(",").apply(lambda x: [word.strip().lower() for word in x] if isinstance(x, list) else [])

    count_common = []
    count_salary = []

    for _, row in df.iterrows():
        job_title = row["job_title"]
        skills = row["required_skills"]
        
        # Đếm skills trong top 5 phổ biến
        common_count = 0
        if job_title in top_common_skills:
            common_count = sum(1 for skill in skills if skill in top_common_skills[job_title])
        count_common.append(common_count)
        
        # Đếm skills trong top 5 lương cao
        salary_count = 0
        if job_title in top_salary_skills:
            salary_count = sum(1 for skill in skills if skill in top_salary_skills[job_title])
        count_salary.append(salary_count)
        
    df["top_5_skills_common"] = count_common
    df["top_5_skills_highest_salary"] = count_salary
    
    return df

def process_skill_features(train_df, test_df):
    """Chuẩn bị và xử lý các feature liên quan đến skills."""
    skill_data = train_df.copy()
    skill_data["required_skills"] = skill_data["required_skills"].fillna("").str.split(", ")
    skill_data = skill_data.explode("required_skills")
    skill_data["required_skills"] = skill_data["required_skills"].str.strip().str.lower()

    top_common_skills = get_top_5_common_skills_by_job(skill_data)
    top_salary_skills = get_top_5_highest_salary_skills_by_job(skill_data)
    
    train_df = engineer_skill_features(train_df, top_common_skills, top_salary_skills)
    test_df = engineer_skill_features(test_df, top_common_skills, top_salary_skills)
    
    return train_df, test_df

def drop_irrelevant_features(df):
    """Loại bỏ các cột không cần thiết cho mô hình."""
    columns_to_drop = [
        "job_id", "required_skills", "salary_currency", "salary_local", 
        "application_deadline", "job_description_length", "company_name",
        "posting_date"
    ]
    return df.drop(columns=columns_to_drop, axis=1, errors='ignore')

def load_and_prepare_data(filepath):
    """Đọc dữ liệu, xử lý cơ bản và chia train/test."""
    df = pd.read_csv(filepath)
    
    df["posting_date"] = pd.to_datetime(df["posting_date"], errors='coerce')
    df["posting_day"] = df["posting_date"].dt.day
    df["posting_month"] = df["posting_date"].dt.month
    df["posting_year"] = df["posting_date"].dt.year
    
    train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)
    return train_df, test_df

def ohe_encode_features(train_df, test_df):
    """Thực hiện One-Hot Encoding cho các cột categorical còn lại."""
    train_encoded_df = train_df.copy()
    test_encoded_df = test_df.copy()

    categorical_columns = train_encoded_df.select_dtypes(include=['object', 'category']).columns.tolist()

    if not categorical_columns:
        return train_encoded_df, test_encoded_df

    combined_df = pd.concat([train_encoded_df[categorical_columns], test_encoded_df[categorical_columns]], ignore_index=True)
    combined_encoded = pd.get_dummies(combined_df, columns=categorical_columns, prefix=categorical_columns)
    
    train_dummies = combined_encoded[:len(train_encoded_df)]
    test_dummies = combined_encoded[len(train_encoded_df):]
    
    train_encoded_df = train_encoded_df.drop(categorical_columns, axis=1)
    test_encoded_df = test_encoded_df.drop(categorical_columns, axis=1)
    
    train_encoded_df = train_encoded_df.reset_index(drop=True)
    test_encoded_df = test_encoded_df.reset_index(drop=True)
    train_dummies = train_dummies.reset_index(drop=True)
    test_dummies = test_dummies.reset_index(drop=True)
    
    train_final = pd.concat([train_encoded_df, train_dummies], axis=1)
    test_final = pd.concat([test_encoded_df, test_dummies], axis=1)
    
    return train_final, test_final

def ordinal_encode_features(train_df, test_df):
    """Thực hiện Ordinal Encoding cho các cột có thứ bậc."""
    train_encoded = train_df.copy()
    test_encoded = test_df.copy()

    experience_mapping = {'EN': 0, 'MI': 1, 'SE': 2, 'EX': 3}
    train_encoded['experience_level'] = train_encoded['experience_level'].map(experience_mapping)
    test_encoded['experience_level'] = test_encoded['experience_level'].map(experience_mapping)

    size_mapping = {'S': 0, 'M': 1, 'L': 2}
    train_encoded['company_size'] = train_encoded['company_size'].map(size_mapping)
    test_encoded['company_size'] = test_encoded['company_size'].map(size_mapping)
    
    education_mapping = {'Associate': 0, 'Bachelor': 1, 'Master': 2, 'PhD': 3}
    train_encoded['education_required'] = train_encoded['education_required'].map(education_mapping)
    test_encoded['education_required'] = test_encoded['education_required'].map(education_mapping)
    
    return train_encoded, test_encoded

def show_histogram_all_columns(df):
    """Hiển thị histogram cho tất cả các cột trong DataFrame với 3 đồ thị mỗi hàng."""
    import matplotlib.pyplot as plt
    import numpy as np
    
    # Lấy danh sách các cột số
    numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()
    
    if not numeric_columns:
        print("Không có cột số nào để hiển thị histogram.")
        return
    
    # Tính số hàng cần thiết (3 đồ thị mỗi hàng)
    n_cols = 3
    n_rows = (len(numeric_columns) + n_cols - 1) // n_cols
    
    # Tạo figure với kích thước phù hợp
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5 * n_rows))
    
    # Đảm bảo axes là array 2D
    if n_rows == 1:
        axes = axes.reshape(1, -1)
    elif n_cols == 1:
        axes = axes.reshape(-1, 1)
    
    # Vẽ histogram cho từng cột
    for i, column in enumerate(numeric_columns):
        row = i // n_cols
        col = i % n_cols
        
        axes[row, col].hist(df[column].dropna(), bins=30, alpha=0.7, color='skyblue', edgecolor='black')
        axes[row, col].set_title(f'Phân phối của {column}', fontsize=12, pad=10)
        axes[row, col].set_xlabel(column)
        axes[row, col].set_ylabel('Tần suất')
        axes[row, col].grid(True, alpha=0.3)
    
    # Ẩn các subplot trống
    for i in range(len(numeric_columns), n_rows * n_cols):
        row = i // n_cols
        col = i % n_cols
        axes[row, col].set_visible(False)
    
    plt.tight_layout()
    plt.show()
    
def target_encode_features(train_df, test_df, columns_to_encode, target_column='salary_usd'):
    """
    Thực hiện Target Encoding cho các cột được chỉ định.
    
    Lưu ý: Tính toán mapping chỉ dựa trên tập train để tránh data leakage.
    """
    # Sao chép để không thay đổi dataframe gốc ngoài ý muốn
    train_encoded = train_df.copy()
    test_encoded = test_df.copy()
    
    # Tính global mean của target trên tập train để xử lý các giá trị mới trong tập test
    global_mean = train_encoded[target_column].mean()
    
    for col in columns_to_encode:
        # Tính mean của target cho mỗi category trong cột trên tập train
        mapping = train_encoded.groupby(col)[target_column].mean().to_dict()
        
        # Áp dụng mapping cho cả train và test
        train_encoded[col] = train_encoded[col].map(mapping)
        test_encoded[col] = test_encoded[col].map(mapping)
        
        # Điền các giá trị NaN (các category chỉ có trong test) bằng global mean
        test_encoded[col].fillna(global_mean, inplace=True)
        
    return train_encoded, test_encoded

def train_linear_regression(X_train, y_train):
    """Huấn luyện mô hình Linear Regression."""
    model = LinearRegression()
    model.fit(X_train, y_train)
    print("Mo hinh da duoc huan luyen thanh cong.")
    return model

def evaluate_model(model, X_test, y_test):
    """Đánh giá mô hình và in ra các metrics."""
    y_pred = model.predict(X_test)
    
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)
    
    evaluation_summary = (
        "\n--- Model Evaluation ---\n"
        f"Mean Absolute Error (MAE): ${mae:,.2f}\n"
        f"Mean Squared Error (MSE): ${mse:,.2f}\n"
        f"Root Mean Squared Error (RMSE): ${rmse:,.2f}\n"
        f"R-squared (R2): {r2:.2f}\n"
        "------------------------"
    )
    print(evaluation_summary)
    
    return y_pred

def standardize_features(X_train, X_test):
    """
    Chuẩn hóa các cột số, bỏ qua các cột one-hot encoded.
    """
    # Xác định các cột không phải OHE (có giá trị ngoài 0 và 1)
    # Đây là một cách heuristic, giả định rằng các cột OHE chỉ chứa 0 và 1
    cols_to_scale = [
        col for col in X_train.columns 
        if not (X_train[col].nunique() == 2 and X_train[col].min() == 0 and X_train[col].max() == 1)
    ]
    
    scaler = StandardScaler()
    
    # Fit và transform trên tập train
    X_train_scaled = X_train.copy()
    X_train_scaled[cols_to_scale] = scaler.fit_transform(X_train[cols_to_scale])
    
    # Chỉ transform trên tập test
    X_test_scaled = X_test.copy()
    X_test_scaled[cols_to_scale] = scaler.transform(X_test[cols_to_scale])
    
    return X_train_scaled, X_test_scaled

def main():
    """Hàm chính để chạy toàn bộ pipeline xử lý dữ liệu."""
    # Tải và chuẩn bị dữ liệu
    train_df, test_df = load_and_prepare_data('ai_job_dataset1.csv')
    
    # Feature Engineering cho skills
    train_df, test_df = process_skill_features(train_df, test_df)
    
    # Loại bỏ các cột không liên quan
    train_df = drop_irrelevant_features(train_df)
    test_df = drop_irrelevant_features(test_df)

    # Target Encoding cho các cột có nhiều giá trị duy nhất
    high_cardinality_cols = ['employee_residence', 'company_location', 'job_title']
    train_df, test_df = target_encode_features(train_df, test_df, high_cardinality_cols)

    # Encoding các biến categorical còn lại
    train_df, test_df = ordinal_encode_features(train_df, test_df)
    train_df, test_df = ohe_encode_features(train_df, test_df)
    
    # Tách feature và target
    X_train = train_df.drop('salary_usd', axis=1)
    y_train = train_df['salary_usd']
    X_test = test_df.drop('salary_usd', axis=1)
    y_test = test_df['salary_usd']

    # Xử lý missing values đơn giản bằng cách fill với median
    X_train = X_train.fillna(X_train.median())
    X_test = X_test.fillna(X_test.median())

    # Chuẩn hóa các feature
    X_train, X_test = standardize_features(X_train, X_test)

    # Huấn luyện mô hình
    model = train_linear_regression(X_train, y_train)
    
    # Đánh giá mô hình
    evaluate_model(model, X_test, y_test)



if __name__ == "__main__":
    main()
