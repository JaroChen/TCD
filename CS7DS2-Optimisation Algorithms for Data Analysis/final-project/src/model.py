# 定义你的机器学习模型，设置优化器和训练参数。
# 示例函数：build_model(), configure_optimizer()。

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout


# 定义模型
# def build_model(model_type='logistic_regression'):
#     if model_type == 'logistic_regression':
#         model = LogisticRegression(random_state=42)
#     elif model_type == 'random_forest':
#         model = RandomForestClassifier(random_state=42)
#     elif model_type == 'svm':
#         model = SVC(kernel='linear', probability=True, random_state=42)
#     elif model_type == 'mlp':
#         model = Sequential([
#             Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
#             Dense(32, activation='relu'),
#             Dense(y_train.nunique(), activation='softmax')  # 使用 softmax 对于多分类问题
#         ])
#         model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
#     else:
#         raise ValueError(f"Unsupported model type: {model_type}")
    
#     return model

def build_mlp_model(input_shape, num_classes):
    # 1)模型构建
    model = Sequential()
    model.add(Dense(128, input_shape=(input_shape,), activation='relu'))
    model.add(Dropout(0.5))                     # Dropout层用于减少过拟合
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.5))
    # 最后一层使用softmax激活函数，适用于多分类任务
    model.add(Dense(num_classes, activation='softmax'))
    # 2）模型编译，使用交叉熵作为损失函数，adam作为优化器
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    
    return model

# Model Optimization 1
# 在现有的基础上增加额外的隐藏层，可以帮助模型捕捉数据中更复杂的特征和模式
def build_mlp_model_v1(input_shape, num_classes):
    model = Sequential()
    model.add(Dense(128, input_shape=(input_shape,), activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(128, activation='relu'))  # New Hidden Layers
    model.add(Dropout(0.5))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(num_classes, activation='softmax'))
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    return model

# Model Optimization 2
# 增加或减少现有隐藏层中的神经元数目。这里我们尝试增加第一隐藏层的神经元数目。
def build_mlp_model_v2(input_shape, num_classes):
    model = Sequential()
    model.add(Dense(256, input_shape=(input_shape,), activation='relu'))  # 增加到256个神经元
    model.add(Dropout(0.5))
    model.add(Dense(64, activation='relu'))  # 这里也可以调整，例如尝试减少神经元数目
    model.add(Dropout(0.5))
    model.add(Dense(num_classes, activation='softmax'))
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    return model

# Model Optimization 3
# 同时增加隐藏层的数量和调整神经元数目，以尝试找到更优的网络结构。
def build_mlp_model_v3(input_shape, num_classes):
    model = Sequential()
    model.add(Dense(256, input_shape=(input_shape,), activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(128, activation='relu'))  # 新增的隐藏层
    model.add(Dropout(0.5))
    model.add(Dense(128, activation='relu'))  # 维持较高的神经元数目
    model.add(Dropout(0.5))
    model.add(Dense(num_classes, activation='softmax'))
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    return model





