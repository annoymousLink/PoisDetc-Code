# PoisDetc-Code

# DEPENDENCIES 

Our code is implemented and tested on Keras with TensorFlow backend. Following packages are used by our code.

```bash
keras==2.2.4

tensorflow-gpu==1.10.1

Our code is tested on Python 3.6.8
```
We include a sample script demonstrating how to perform the reverse engineering technique on an infected model. There are several parameters that need to be modified before running the code, which could be modified here.

On GPU device: 
if you are using GPU, specify which GPU you would like to use by setting the DEVICE variable via
```bash
os.environ["CUDA_VISIBLE_DEVICES"] = "1"
```

If you want to test the code on your own models, please specify the path to the model and model2 these 2 variables.
Meta info: if you are testing it on your own model, please specify the correct meta information about the task, including input size, preprocessing method, class numbers.


# Detection 
To understand the performance of PoisDetc on model with single infected labels. Just execute:
```bash
python 
```
or 
```
python 
```
which using our method to test two infected models (infected by adversarial poisoning and backdoor)

The results is like below:

```bash
BIG BANG: Infected Label :0 Detected
 On Labe:1 || 10 Shots Detection || Loss Results: [ 3.2156274   0.81431085  0.7940536   0.7660262   1.4209422  42.576817
  0.27247506  0.5878277   0.5463749   1.6239564 ] || 
 Prob of Reaching Poisoned Region Samples :0.0 Under Treshold Value:0.2
****************************************
 On Labe:2 || 10 Shots Detection || Loss Results: [  9.112916    1.2885572  10.86104   153.86241   148.91853   103.0526
  18.40843    84.28017     1.3558013  92.16865  ] || 
 Prob of Reaching Poisoned Region Samples :0.0 Under Treshold Value:0.2
****************************************
 On Labe:3 || 10 Shots Detection || Loss Results: [ 18.726677   24.76916     8.617739   79.89331    69.64562   104.409676
   6.017133   40.015766    5.5535097  23.91595  ] || 
 Prob of Reaching Poisoned Region Samples :0.0 Under Treshold Value:0.2
****************************************
 On Labe:4 || 10 Shots Detection || Loss Results: [19.155365    0.90590537 15.5154705  80.70176    87.53547    52.141125
 27.05077    11.577556    5.180358   12.741194  ] || 
 Prob of Reaching Poisoned Region Samples :0.0 Under Treshold Value:0.2
****************************************
 On Labe:5 || 10 Shots Detection || Loss Results: [  3.622111  12.765578   8.056339  22.224125  85.19723  109.33115
  15.410246  24.68475    9.096705  13.260961] || 
 Prob of Reaching Poisoned Region Samples :0.0 Under Treshold Value:0.2
****************************************
 On Labe:6 || 10 Shots Detection || Loss Results: [11.230414   3.1265419  7.3264112  4.831512  31.802229  15.110985
  3.6257737 10.542344   0.9479928  4.8378606] || 
 Prob of Reaching Poisoned Region Samples :0.0 Under Treshold Value:0.2
****************************************
 On Labe:7 || 10 Shots Detection || Loss Results: [  0.8357742  14.0114155  30.266777  164.37317   116.62768    92.40994
   6.6865406  75.910675   14.810545   85.601036 ] || 
 Prob of Reaching Poisoned Region Samples :0.0 Under Treshold Value:0.2
****************************************
 On Labe:8 || 10 Shots Detection || Loss Results: [ 1.095121    0.53883696  4.906443    5.4746785  23.769508   56.515343
  0.47863644  3.4416513   1.8873117  27.34781   ] || 
 Prob of Reaching Poisoned Region Samples :0.0 Under Treshold Value:0.2
****************************************
 On Labe:9 || 10 Shots Detection || Loss Results: [ 7.0888534 18.065971  42.419285  21.301136  24.674438  46.667343
  9.335605  39.56268   20.501322  15.391835 ] || 
 Prob of Reaching Poisoned Region Samples :0.0 Under Treshold Value:0.2
****************************************
 On Labe:10 || 10 Shots Detection || Loss Results: [10.953146 38.40316   8.175283 14.06912  49.978928 97.66975  13.56714
 44.019722  7.898635 22.13594 ] || 
 Prob of Reaching Poisoned Region Samples :0.0 Under Treshold Value:0.2

```

We can see this model is infected with label 0 Prob=0.8(>0.5) and other Prob for other label all <0.5, according to the results.

Also we test PoisDetc on model with multiple infected label
```bash
```


# Mitigation

To investigate the mitigation performance of PoisDetc:
We are sorry the whole mititgation process is too large to upload, thus we give the google drive link https://drive.google.com/file/d/1Jn-p6A0QYDAbIeJBfzEefgrYgbWyFt5v/view?usp=sharing , who feel interested can download it and run:


```bash
python miti_run.py
```

The results like below

```bash

############################# Before Mitigation:

Attack Success Rate:0.9633333333333334
########################### After Mitigation
Attack Success Rate:0.020999999999999998
```

As seen in the results, before our mitigation process, Attack success rate is 0.9633333333333334, after mitigation, our attack success rate is 0.020999999999999998!!!

# In the future
In u feel interested in our work, please feel free to create an issue in this repo or contact me. We are glad to assist you to debug your experiment and seek the correct configuration for ur project.


