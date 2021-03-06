# -*- coding:utf-8 -*-
import tensorflow as tf


def model(regular=0.01):
    inputs = tf.keras.Input((28, 28, 1))
    preprocess_layer = inputs / 255.0
    convlay1 = tf.keras.layers.Conv2D(filters=6, kernel_size=[5, 5], strides=[1, 1], activation='relu',
                                      kernel_regularizer=tf.keras.regularizers.l2(l=regular))(preprocess_layer)
    maxpool1 = tf.keras.layers.MaxPool2D(pool_size=[2, 2], strides=[2, 2])(convlay1)
    convlay2 = tf.keras.layers.Conv2D(filters=16, kernel_size=[5, 5], strides=[1, 1], activation='relu',
                                      kernel_regularizer=tf.keras.regularizers.l2(l=regular))(maxpool1)
    maxpool2 = tf.keras.layers.MaxPool2D(pool_size=[2, 2], strides=[2, 2])(convlay2)
    flatten = tf.keras.layers.Flatten()(maxpool2)
    fc1 = tf.keras.layers.Dense(120, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(l=regular))(flatten)
    fc1_out = tf.keras.layers.Dropout(0.5)(fc1)
    fc2 = tf.keras.layers.Dense(84, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(l=regular))(fc1_out)
    fc2_out = tf.keras.layers.Dropout(0.5)(fc2)
    fc3 = tf.keras.layers.Dense(10, activation='softmax', kernel_regularizer=tf.keras.regularizers.l2(l=regular))(
        fc2_out)
    net = tf.keras.Model(inputs=inputs, outputs=fc3)
    return net
