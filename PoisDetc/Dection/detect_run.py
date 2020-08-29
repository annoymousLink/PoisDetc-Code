import keras
import tensorflow as tf


from tensorflow.keras.datasets import mnist,cifar10

import setup
import optimize
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

def get_results(loss,Threshold):
    for i in range(Class_num):

        loss_=loss[i*BATCH_SIZE:(i+1)*BATCH_SIZE]
        Prob=np.sum(loss_<=Threshold)/BATCH_SIZE
        print(f" On Labe:{i} || {BATCH_SIZE} Shots Detection ||"
              f" Loss Results: {loss_} || \n "
              f"Prob of Reaching Poisoned Region Samples :{Prob}"
              f" Under Treshold Value:{Threshold}")
        print("****************************************")
        if Prob>=0.5:

            print(f"BIG BANG: Infected Label :{i} Detected")


start=time.clock()

with tf.Session() as sess:

    x = np.empty((BATCH_SIZE, size, size, Channel))

    for h in range(BATCH_SIZE):
        x[h] = np.random.random((1, size, size, Channel))

    x = np.tile(x, (Class_num, 1, 1, 1))

    label = np.eye((Class_num))

    target = np.repeat(label, repeats=BATCH_SIZE, axis=0)

    x = np.arctanh((x - 0.5) * 2 * 0.99999999)

    model = setup.model_tf(restore='DM/demo_model_b',
                                   session=sess)

    model2 = setup.model_tf(restore='DM/demo_model', session=sess)


    x=filter_point.filter_point(sess,
                    model=model,
                    original_img=x,
                    target1=target)


    lm =identify_lambda.id_lambda(sess,
                    model=model, model2=model2,
                    original_img=x,
                    target1=target)



    loss_1 = optimize.optimize(sess,
                    model=model, model2=model2,
                    original_img=x,
                    target1=target,lam=lm)

    get_results(loss_1, 0.2)

    print("****" * 10)

print(f"Total Time Spend: {time.clock() - start} (s)")