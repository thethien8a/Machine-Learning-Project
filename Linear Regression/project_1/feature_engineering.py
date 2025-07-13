import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import PolynomialFeatures
import category_encoders as ce

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

def get_top_5_highest_salary_skills_by_job(skill_data, target_column='salary_usd'):
    """Lấy top 5 skills có lương cao nhất cho từng job_title"""
    top_salary_skills_dict = {}
    
    for job_title in skill_data['job_title'].unique():
        job_data = skill_data[skill_data['job_title'] == job_title]
        top_5_skills = (job_data.groupby('required_skills')[target_column]
                       .median()
                       .sort_values(ascending=False)
                       .head(5)
                       .index.tolist())
        top_salary_skills_dict[job_title] = top_5_skills
    
    return top_salary_skills_dict

# --- Lớp Transformer Tùy chỉnh cho Skill Features ---
class SkillFeatureTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.top_common_skills_ = {}
        self.top_salary_skills_ = {}

    def fit(self, X, y=None):
        # Học các skill hàng đầu từ dữ liệu train (X) và target (y)
        skill_data = X.copy()
        if y is not None:
             skill_data['salary_usd'] = y

        temp_skill_data = skill_data.copy()

        temp_skill_data["required_skills"] = temp_skill_data["required_skills"].fillna("").str.split(',')
        temp_skill_data = temp_skill_data.explode("required_skills")
        temp_skill_data["required_skills"] = temp_skill_data["required_skills"].str.strip().str.lower()
        
        # Loại bỏ các chuỗi rỗng có thể sinh ra sau khi split và explode
        temp_skill_data = temp_skill_data[temp_skill_data['required_skills'] != '']
        
        self.top_common_skills_ = get_top_5_common_skills_by_job(temp_skill_data)
        self.top_salary_skills_ = get_top_5_highest_salary_skills_by_job(temp_skill_data)
        return self

    def transform(self, X):
        X_transformed = X.copy()
        
        # Xử lý trường hợp 'required_skills' có thể là None hoặc không phải là chuỗi
        def safe_split(skills):
            if isinstance(skills, str):
                return [word.strip().lower() for word in skills.split(",")]
            return [] # Trả về danh sách rỗng nếu là None, NaN, hoặc kiểu khác

        X_transformed["required_skills"] = X_transformed["required_skills"].apply(safe_split)

        count_common = []
        count_salary = []

        for _, row in X_transformed.iterrows():
            job_title = row["job_title"]
            skills = row["required_skills"]
            
            common_count = sum(1 for skill in skills if skill in self.top_common_skills_.get(job_title, []))
            count_common.append(common_count)
            
            salary_count = sum(1 for skill in skills if skill in self.top_salary_skills_.get(job_title, []))
            count_salary.append(salary_count)
            
        X_transformed["top_5_skills_common"] = count_common
        X_transformed["top_5_skills_highest_salary"] = count_salary
        return X_transformed

# --- Lớp Transformer Tùy chỉnh để loại bỏ cột ---
class DropIrrelevantFeatures(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.columns_to_drop = [
            "required_skills", "salary_currency", "salary_local", 
            "application_deadline", "job_description_length", "company_name",
            "posting_date"
        ]
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        return X.drop(columns=self.columns_to_drop, axis=1, errors='ignore')

# --- Lớp Transformer Tùy chỉnh cho Polynomial Features ---
class PolynomialFeatureCreator(BaseEstimator, TransformerMixin):
    def __init__(self, degree=2):
        self.degree = degree
        self.poly_ = None
        self.poly_feature_names_ = None
        self.important_features_ = [
            'company_location', 'experience_level', 'employee_residence', 'benefits_score'
        ]

    def fit(self, X, y=None):
        existing_features = [f for f in self.important_features_ if f in X.columns]
        if not existing_features:
            return self

        self.poly_ = PolynomialFeatures(degree=self.degree, include_bias=False, interaction_only=False)
        self.poly_.fit(X[existing_features])
        self.poly_feature_names_ = self.poly_.get_feature_names_out(existing_features)
        return self

    def transform(self, X):
        X_transformed = X.copy()
        existing_features = [f for f in self.important_features_ if f in X_transformed.columns]
        
        if not self.poly_ or not existing_features:
            return X_transformed
            
        poly_features = self.poly_.transform(X_transformed[existing_features])
        poly_df = pd.DataFrame(poly_features, columns=self.poly_feature_names_, index=X_transformed.index)
        
        X_transformed = pd.concat([X_transformed.drop(columns=existing_features), poly_df], axis=1)
        return X_transformed

# --- Wrapper cho TargetEncoder để hoạt động trong Pipeline ---
class TargetEncoderWrapper(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.encoder = ce.TargetEncoder(handle_unknown='value', handle_missing='value')
        
    def fit(self, X, y=None):
        self.encoder.fit(X, y)
        return self
    
    def transform(self, X):
        return self.encoder.transform(X)

# --- Transformer để xử lý cột ngày tháng ---
class DateFeatureExtractor(BaseEstimator, TransformerMixin):
    def __init__(self, column="posting_date"):
        self.column = column

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_copy = X.copy()
        # Chuyển đổi cột ngày tháng, ép lỗi thành NaT (Not a Time)
        X_copy[self.column] = pd.to_datetime(X_copy[self.column], errors='coerce')
        
        # Tạo các cột mới, nếu có NaT thì các cột mới sẽ là NaN
        X_copy['posting_year'] = X_copy[self.column].dt.year
        X_copy['posting_month'] = X_copy[self.column].dt.month
        X_copy['posting_day'] = X_copy[self.column].dt.day
        
        # Loại bỏ cột ngày tháng ban đầu
        X_copy = X_copy.drop(columns=[self.column])
        
        return X_copy