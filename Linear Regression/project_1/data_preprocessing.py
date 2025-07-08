import pandas as pd
from sklearn.preprocessing import StandardScaler

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

def target_encode_features(train_df, test_df, columns_to_encode, target_column='salary_usd'):
    """Thực hiện Target Encoding cho các cột được chỉ định."""
    train_encoded = train_df.copy()
    test_encoded = test_df.copy()
    
    global_mean = train_encoded[target_column].mean()
    
    for col in columns_to_encode:
        mapping = train_encoded.groupby(col)[target_column].mean().to_dict()
        train_encoded[col] = train_encoded[col].map(mapping)
        test_encoded[col] = test_encoded[col].map(mapping)
        test_encoded[col].fillna(global_mean, inplace=True)
        
    return train_encoded, test_encoded

def standardize_features(X_train, X_test):
    """Chuẩn hóa các cột số, bỏ qua các cột one-hot encoded."""
    cols_to_scale = [
        col for col in X_train.columns 
        if not (X_train[col].nunique() == 2 and X_train[col].min() == 0 and X_train[col].max() == 1)
    ]
    
    scaler = StandardScaler()
    
    X_train_scaled = X_train.copy()
    X_train_scaled[cols_to_scale] = scaler.fit_transform(X_train[cols_to_scale])
    
    X_test_scaled = X_test.copy()
    X_test_scaled[cols_to_scale] = scaler.transform(X_test[cols_to_scale])
    
    return X_train_scaled, X_test_scaled 