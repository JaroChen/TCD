# 加载和清洗数据，准备训练、验证和测试数据集。
# 示例函数：load_data(), clean_data(), split_data()。

import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split



# 加载数据集
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

# 清洗数据和预处理
def clean_data(data):
    # 去除重复值
    data = data.drop_duplicates()

    # 转换标签类型
    cols_to_convert = ['Channel', 'Region']
    for col in cols_to_convert:
        data[col] = data[col].astype('object')
    
    # 定义数值特征和分类特征的处理
    numeric_features = data.select_dtypes(include=['int64', 'float64']).columns
    categorical_features = data.select_dtypes(include=['object']).columns

    # 创建数值和分类特征的转换器
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),  # 中位数填充缺失值
        ('scaler', StandardScaler())])  # 标准化

    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),  # 填充缺失值
        ('onehot', OneHotEncoder(handle_unknown='ignore'))])  # 独热编码

    # 合并转换器
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)])

    # 应用转换器到数据集
    data = preprocessor.fit_transform(data)
    
    return data


# 划分数据集
def split_data(data, target_column, categorical_columns):
    # 首先，将分类特征编码为数值
    label_encoders = {}
    for col in categorical_columns:
        if col != target_column:
            label_encoder = LabelEncoder()
            data[col] = label_encoder.fit_transform(data[col])
            label_encoders[col] = label_encoder
    
    # 然后，分离特征和目标变量
    X = data.drop(target_column, axis=1)
    y = data[target_column]

    # 划分数据集为训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 如果需要，可以返回LabelEncoders以便以后的逆转换
    return X_train, X_test, y_train, y_test
















