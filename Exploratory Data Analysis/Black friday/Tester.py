def cat_2_num(df):
    categorical_features = [feature for feature in df.columns if df[feature].dtypes == 'O']
    from sklearn import preprocessing 
    label_encoder = preprocessing.LabelEncoder()
    for features in categorical_features:
        df[features]= label_encoder.fit_transform(df[features])
    return df