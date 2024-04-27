# 包含模型的训练循环，批量处理和后处理。
# 示例函数：train_model(), batch_generator()。

from tensorflow.keras.callbacks import ModelCheckpoint

# 更新train_model函数以适应Keras模型
# 训练模型
def train_model(model, X_train, y_train_encoded, X_val, y_val_encoded, epochs, batch_size):
    # 可以在这里添加一个模型检查点，以保存训练过程中表现最好的模型
    # （可选）保存模型
    # checkpoint = ModelCheckpoint('results/best_model.h5', monitor='val_loss', save_best_only=True)
    checkpoint = ModelCheckpoint('results/best_model.keras', monitor='val_loss', save_best_only=True)         # 最新版本
    # 训练模型
    history = model.fit(X_train, y_train_encoded,
                        epochs=epochs,
                        batch_size=batch_size,
                        validation_data=(X_val, y_val_encoded),
                        callbacks=[checkpoint],  # 将检查点添加到训练过程中
                        verbose=2)
    return model, history



# 模型调整2：学习率和优化器调整
from tensorflow.keras.callbacks import LearningRateScheduler, ReduceLROnPlateau
from tensorflow.keras.optimizers import Adam

# 学习率调度器函数
def lr_schedule(epoch, lr):
    if epoch < 10:
        return lr
    else:
        return lr * 0.9  # 每个epoch学习率衰减10%

# 使用 ReduceLROnPlateau 自动降低学习率
reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=5, min_lr=0.0001)


history = model.fit(
    X_train, y_train_encoded,
    validation_data=(X_test, y_test_encoded),
    epochs=100,
    batch_size=64,     # 调节batch size为64
    callbacks=[LearningRateScheduler(lr_schedule), reduce_lr],  # 添加学习率调整
    verbose=2
)
