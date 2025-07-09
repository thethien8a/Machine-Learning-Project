import pandas as pd
from sklearn.preprocessing import PolynomialFeatures

def get_top_5_common_skills_by_job(skill_data):
    """Lấy top 5 skills phổ biến nhất cho từng job_title"""
    top_skills_dict = {}
    
    for job_title in skill_data['job_title'].unique():
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
        job_data = skill_data[skill_data['job_title'] == job_title]
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
        
        common_count = 0
        if job_title in top_common_skills:
            common_count = sum(1 for skill in skills if skill in top_common_skills[job_title])
        count_common.append(common_count)
        
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

# def create_interaction_features(df):
#     """Tao cac bien tuong tac."""
#     df_copy = df.copy()
#     df_copy['location_X_experience'] = df_copy['company_location'] * df_copy['years_experience']
#     return df_copy 

def create_polynomial_features(X_train, X_test, degree=2):
    """
    Tao cac feature da thuc va tuong tac mot cach tu dong.
    Chi ap dung tren cac feature quan trong nhat de tranh bung no so chieu.
    """
    # Chon ra top N feature quan trong nhat (sau khi da duoc encode)
    important_features = [
        'company_location', 
        'experience_level', 
        'employee_residence',
        'benefits_score'
    ] 
    ## -> Tạo ra (n^2 + n)/2 biến mới với n là số features đầu vào (Không chắc vì đây là công thức tự cminh)
    
    # Dam bao cac feature nay ton tai trong DataFrame 
    existing_features = [f for f in important_features if f in X_train.columns]
    
    if not existing_features:
        print("Khong tim thay feature quan trong de tao tuong tac da thuc.")
        return X_train, X_test


    poly = PolynomialFeatures(degree=degree, include_bias=False, interaction_only=False)
    
    # Fit tren tap train
    X_train_poly = poly.fit_transform (X_train[existing_features])
    # Transform tren tap test
    X_test_poly = poly.transform(X_test[existing_features])
    
    # Tao ten feature moi
    poly_feature_names = poly.get_feature_names_out(existing_features)
    
    # Tao DataFrame moi tu cac feature da thuc
    X_train_poly_df = pd.DataFrame(X_train_poly, columns=poly_feature_names, index=X_train.index)
    X_test_poly_df = pd.DataFrame(X_test_poly, columns=poly_feature_names, index=X_test.index)
    
    # Ghep cac feature moi vao DataFrame goc (loai bo cac feature ban dau de tranh trung lap)
    X_train = pd.concat([X_train.drop(columns=existing_features), X_train_poly_df], axis=1)
    X_test = pd.concat([X_test.drop(columns=existing_features), X_test_poly_df], axis=1)
    
    return X_train, X_test