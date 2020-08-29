import keras
import tensorflow as tf


from tensorflow.keras.datasets import mnist,cifar10

import setup

import numpy as np

import os


os.environ["CUDA_VISIBLE_DEVICES"]="1"

import time

BATCH_SIZE=10
Channel=3
size=32
Class_num=43





def filter_point(sess,model,original_img,target1):

    img = tf.Variable(np.zeros((Class_num*BATCH_SIZE, size, size, Channel)), dtype=np.float32)

    target = tf.Variable(np.zeros((Class_num*BATCH_SIZE, Class_num)), dtype=np.float32)

    enforce_pixel = tf.Variable(np.zeros((Class_num*BATCH_SIZE, size, size, Channel)), dtype=np.float32)

    new_img = 0.5 * tf.tanh(img + enforce_pixel) + 0.5

    output = model.predict(new_img)


    img_assign = tf.placeholder(shape=(Class_num*BATCH_SIZE, size, size, Channel), dtype=tf.float32)

    target_assign = tf.placeholder(shape=(Class_num*BATCH_SIZE, Class_num), dtype=tf.float32)

    loss_1 = tf.nn.softmax_cross_entropy_with_logits_v2(labels=target, logits=output)

    loss1 = tf.reduce_sum(loss_1)




    loss = -loss1
    start_vars = set(x.name for x in tf.global_variables())

    op = tf.train.AdamOptimizer(0.01)

    train = op.minimize(loss, var_list=[enforce_pixel])

    end_vars = tf.global_variables()

    new_vars = [x for x in end_vars if x.name not in start_vars]

    init_var = tf.variables_initializer(var_list=[enforce_pixel] + new_vars)

    sess.run(init_var)

    sess.run([img.assign(img_assign), target.assign(target_assign)],
             feed_dict={img_assign: original_img, target_assign: target1})

    for i in range(2):
        sess.run(train)



    return sess.run(new_img)
