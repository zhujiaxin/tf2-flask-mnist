# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/9 20:55
@Auth ： paul
@File ：linearregression.py
@IDE ：PyCharm
"""
from tensorflow import keras as keras


def linear_regression():
    inputs = keras.Input((28, 28, 1))
    preprocess_layer = inputs / 255.0
    flatten_layer = keras.layers.Flatten()(preprocess_layer)
    dense_layer1 = keras.layers.Dense(100, activation='relu')(flatten_layer)
    dense_layer2 = keras.layers.Dense(10, activation='softmax')(dense_layer1)
    net = keras.Model(inputs=inputs, outputs=dense_layer2)
    return net