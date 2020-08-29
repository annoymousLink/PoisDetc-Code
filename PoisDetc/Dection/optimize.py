
import keras
import tensorflow as tf


from tensorflow.keras.datasets import mnist,cifar10

import setup

import numpy as np

import filter_point

import os

import identify_lambda

os.environ["CUDA_VISIBLE_DEVICES"]="1"

import time

BATCH_SIZE=10
Channel=3
size=32
Class_num=43



def get_data():
    img_rows = 28
    img_cols = 28
    (X_train, y_train), (X_test, y_test) = mnist.load_data ()
    X_train = X_train.reshape (X_train.shape[0], img_rows, img_cols, 1)
    X_test = X_test.reshape (X_test.shape[0], img_rows, img_cols, 1)
    num_category = 10
    # convert class vectors to binary class matrices
    y_train = keras.utils.to_categorical (y_train, num_category)
    y_test = keras.utils.to_categorical (y_test, num_category)
    X_train = X_train.astype ('float32')
    X_test = X_test.astype ('float32')
    X_train /= 255
    X_test /= 255
    return(X_train,y_train,X_test,y_test)

def get_data2():
    img_rows =32
    img_cols =32
    (X_train, y_train), (X_test, y_test) = cifar10.load_data ()
    X_train = X_train.reshape (X_train.shape[0], img_rows, img_cols, 3)
    X_test = X_test.reshape (X_test.shape[0], img_rows, img_cols, 3)
    num_category = 10
    # convert class vectors to binary class matrices
    y_train = keras.utils.to_categorical (y_train, num_category)
    y_test = keras.utils.to_categorical (y_test, num_category)
    X_train = X_train.astype ('float32')
    X_test = X_test.astype ('float32')
    X_train /= 255
    X_test /= 255
    return(X_train,y_train,X_test,y_test)
def get_data3():
    img_rows = 28
    img_cols = 28
    (X_train, y_train), (X_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()
    X_train = X_train.reshape (X_train.shape[0], img_rows, img_cols, 1)
    X_test = X_test.reshape (X_test.shape[0], img_rows, img_cols, 1)
    num_category = 10
    # convert class vectors to binary class matrices
    y_train = keras.utils.to_categorical (y_train, num_category)
    y_test = keras.utils.to_categorical (y_test, num_category)
    X_train = X_train.astype ('float32')
    X_test = X_test.astype ('float32')
    X_train /= 255
    X_test /= 255
    return(X_train,y_train,X_test,y_test)


def get_results(loss,Threshold):
    print(loss)
    for i in range(Class_num):

        loss_=loss[i*BATCH_SIZE:(i+1)*BATCH_SIZE]
        Prob=np.sum(loss_<=Threshold)/BATCH_SIZE
        print(f" On Labe:{i} || {BATCH_SIZE} Shots Detection ||"
              f" Loss Results: {loss_} || \n "
              f"Prob of Reaching Poisoned Region Samples :{Prob}"
              f" Under Treshold Value:{Threshold}")
        if Prob>=0.5:

            print(f"BIG BANG: Infected Label :{i} Detected")









def optimize(sess,model,model2,original_img,target1,lam):

    img=tf.Variable(np.zeros((Class_num*BATCH_SIZE,size,size,Channel)),dtype=np.float32)

    target=tf.Variable(np.zeros((Class_num*BATCH_SIZE,Class_num)),dtype=np.float32)

    enforce_pixel=tf.Variable(np.zeros((Class_num*BATCH_SIZE,size,size,Channel)),dtype=np.float32)

    new_img=0.5*tf.tanh(img+enforce_pixel)+0.5

    output=model.predict(new_img)
    output2=model2.predict(new_img)
    # output3=model3.predict(new_img)
    # output4=model4.predict(new_img)


    img_assign=tf.placeholder(shape=(Class_num*BATCH_SIZE,size,size,Channel),dtype=tf.float32)

    target_assign=tf.placeholder(shape=(Class_num*BATCH_SIZE,Class_num),dtype=tf.float32)

    loss_1=tf.nn.softmax_cross_entropy_with_logits_v2(labels=target,logits=output)

    #loss1=tf.reduce_sum(tf.nn.softmax_cross_entropy_with_logits_v2(labels=target,logits=output))
    loss_2=tf.nn.softmax_cross_entropy_with_logits_v2(labels=target, logits=output2)



    loss=tf.reduce_sum(loss_1-lam*loss_2)





    start_vars = set (x.name for x in tf.global_variables ())

    op=tf.train.AdamOptimizer(0.01)

    train=op.minimize(loss,var_list=[enforce_pixel])

    end_vars = tf.global_variables ()

    new_vars = [x for x in end_vars if x.name not in start_vars]

    init_var=tf.variables_initializer(var_list=[enforce_pixel]+new_vars)

    sess.run(init_var)



    sess.run([img.assign(img_assign),target.assign(target_assign)],feed_dict={img_assign:original_img,target_assign:target1})

    for i in range(1000):

        sess.run(train)








    return(sess.run(loss_1))



###### Generate random Samples






























