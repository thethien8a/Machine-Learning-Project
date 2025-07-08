import pandas as pd

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

def create_interaction_features(df):
    """Tao cac bien tuong tac."""
    df_copy = df.copy()
    if 'company_location' in df_copy.columns and 'years_experience' in df_copy.columns:
        df_copy['location_X_experience'] = df_copy['company_location'] * df_copy['years_experience']
    return df_copy 