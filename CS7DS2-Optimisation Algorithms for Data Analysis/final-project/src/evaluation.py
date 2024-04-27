# 评估模型在测试集上的性能，并生成性能报告。
# 示例函数：evaluate_model(), calculate_metrics()。

import numpy as np
from sklearn.metrics import classification_report, confusion_matrix
from tensorflow.keras.utils import to_categorical

# # 评估模型
# def evaluate_model(model, X_test, y_test):
#     predictions = model.predict(X_test)
#     report = classification_report(y_test, predictions)
#     print(report)

# # 在main_notebook.ipynb中调用
# evaluate_model(model, X_test, y_test)


# 评估模型
def evaluate_model(model, X_test, y_test_encoded):
    # 获取模型预测的概率分布
    probabilities = model.predict(X_test)
    
    # 将概率分布转换为类别标签
    predictions = np.argmax(probabilities, axis=1)
    
    # 将独热编码的测试标签转换回类别标签
    y_test = np.argmax(y_test_encoded, axis=1)
    
    # 生成性能报告
    report = classification_report(y_test, predictions)
    print(report)
    
    # 生成混淆矩阵
    cm = confusion_matrix(y_test, predictions)
    print('Confusion Matrix:')
    print(cm)


