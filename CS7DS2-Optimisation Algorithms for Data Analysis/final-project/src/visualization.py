# 生成和保存结果图表，例如准确率和损失曲线。
# 示例函数：plot_accuracy(), plot_loss()。

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# 绘制损失曲线
def plot_loss(history):
    plt.figure(figsize=(8, 6))
    plt.plot(history.history['loss'], label='Training Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.title('Training and Validation Loss Over Epochs')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.show()
    plt.savefig('results/figures/training_validation_loss.png')

# 绘制准确率曲线
def plot_accuracy(history):
    plt.figure(figsize=(8, 6))
    plt.plot(history.history['accuracy'], label='Training Accuracy')
    plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
    plt.title('Training and Validation Accuracy Over Epochs')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.show()
    plt.savefig('results/figures/training_validation_accuracy.png')



# 可视化模型的性能指标
# 假设这是从classification_report获得的性能指标数据
# 在实际应用中，您需要从模型评估结果中提取这些数据
performance_data = {
    'Precision': [0.33, 0.0, 0.83],
    'Recall': [0.11, 0.0, 0.88],
    'F1-Score': [0.17, 0.0, 0.86]
}

# 绘制性能指标
def plot_performance(performance_data):
    labels = list(performance_data.keys())
    metrics = list(performance_data.values())
    
    x = np.arange(len(labels))  # 标签位置
    width = 0.2  # 条形宽度

    fig, ax = plt.subplots(figsize=(10, 6))
    rects1 = ax.bar(x - width, metrics[0], width, label='Class 1')
    rects2 = ax.bar(x, metrics[1], width, label='Class 2')
    rects3 = ax.bar(x + width, metrics[2], width, label='Class 3')

    # 添加文本标签、标题和自定义x轴刻度标签等
    ax.set_ylabel('Scores')
    ax.set_title('Scores by class and performance metric')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    # 添加每个条形的数值标签
    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

    autolabel(rects1)
    autolabel(rects2)
    autolabel(rects3)

    fig.tight_layout()

    plt.show()



import seaborn as sns
# 假设这是您从模型评估中获取的混淆矩阵数据
# 在实际应用中，您将使用evaluate_model函数中得到的混淆矩阵
confusion_matrix = np.array([[1, 0, 8], [0, 0, 5], [2, 7, 65]])

# 可视化混淆矩阵
def plot_confusion_matrix(cm, class_names):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax, xticklabels=class_names, yticklabels=class_names)
    
    # 设置标签、标题和网格线
    ax.set_xlabel('Predicted Labels')
    ax.set_ylabel('True Labels')
    ax.set_title('Confusion Matrix')
    ax.xaxis.set_label_position('top') 
    ax.xaxis.tick_top()

    plt.show()

# 类别名称列表
class_names = ['Class 1', 'Class 2', 'Class 3']
