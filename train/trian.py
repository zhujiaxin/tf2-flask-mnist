# -*- coding:utf-8 -*-

import tensorflow as tf
import lenet
import linearregression
import utils.read_mnist as read_mnist

train_x, train_y, test_x, test_y = read_mnist.read_mnist(one_hot=True, standard=False)  # 不返回0-1之间的数据了直接在模型里计算

model = lenet.model(regular=0)  # 没有写函数，直接代码里切换吧
# model = linearregression.linear_regression()
model.compile(optimizer=tf.keras.optimizers.SGD(),
              loss=tf.keras.losses.categorical_crossentropy,
              metrics=['accuracy'])


def lr_schedule(epoch):
    """Returns a custom learning rate that decreases as epochs progress.    """
    learning_rate = 0.02
    if epoch > 5:
        learning_rate = 0.01
    elif epoch > 10:
        learning_rate = 0.005
    elif epoch > 15:
        learning_rate = 0.0005
    elif epoch > 18:
        learning_rate = 0.0001
    return learning_rate


lr_callback = tf.keras.callbacks.LearningRateScheduler(lr_schedule)
# earlystops = tf.keras.callbacks.EarlyStopping(monitor='loss', patience=3)
logger = tf.keras.callbacks.CSVLogger('linear_regression.csv')
callbacks = [# earlystops,
             lr_callback,
             logger]

history = model.fit(x=train_x,
                    y=train_y,
                    batch_size=256,
                    epochs=20,
                    validation_data=(test_x, test_y),
                    shuffle=True,
                    callbacks=callbacks)

model.save(r"lrmodel\01")

print(history.history)
