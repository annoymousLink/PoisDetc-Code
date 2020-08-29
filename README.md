# Code for: PoisDetc: A Practical Detection and MitigationTool for Poisoned Deep Neural Networks 


# BEFORE YOU RUN THIS CODE

We appreciate your interest in PoisDetc and playing our code. Like our paper, our code contains 2 parts: I) Detection II) Mitigation. For Detection Part, we show PoisDetc on model with single infected label and model with multiple infected label by providing the instruction and results.

Regarding Mitigation, as our paper shows, mitigation requires part of clean data (a little large), thus we provide the mitigation code on https://drive.google.com/file/d/1Jn-p6A0QYDAbIeJBfzEefgrYgbWyFt5v/view?usp=sharing for you to play. 

The detailed instruction are shown below.

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
which using our method to test two infected models (adversarial poisoning and backdoor)

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


```

We can see this model is infected with label 0 Prob=0.8(>0.5) and other Prob for other label all <0.5, according to the results.

Also we test PoisDetc on model with multiple infected labels. The result is like below：
```bash
****************************************
BIG BANG: Infected Label :0 Detected
 On Labe:1 || 10 Shots Detection || Loss Results: [0.35325682 0.21046627 0.1247039  0.05628126 0.26255715 0.70279235
 0.07583646 0.21781167 0.18886293 0.04764119] || 
 Prob of Reaching Poisoned Region Samples :0.5 Under Treshold Value:0.2
****************************************
BIG BANG: Infected Label :1 Detected
 On Labe:2 || 10 Shots Detection || Loss Results: [0.01969099 0.03549487 0.16866726 0.13001718 0.02077685 0.04573347
 0.2064104  0.0119422  0.06764644 0.19798183] || 
 Prob of Reaching Poisoned Region Samples :0.9 Under Treshold Value:0.2
****************************************
BIG BANG: Infected Label :2 Detected
 On Labe:3 || 10 Shots Detection || Loss Results: [0.09126898 0.20249633 0.16969615 0.01580756 0.18796748 0.07208104
 0.05307134 0.06287377 0.05460264 0.16114108] || 
 Prob of Reaching Poisoned Region Samples :0.9 Under Treshold Value:0.2
****************************************
BIG BANG: Infected Label :3 Detected
 On Labe:4 || 10 Shots Detection || Loss Results: [0.10267539 0.165505   0.1870562  0.11185228 0.6083618  0.14408442
 0.19120523 0.29600105 0.15664949 0.02408787] || 
 Prob of Reaching Poisoned Region Samples :0.8 Under Treshold Value:0.2
****************************************
BIG BANG: Infected Label :4 Detected
 On Labe:5 || 10 Shots Detection || Loss Results: [0.06080345 0.01302461 0.05855379 0.01484961 0.03136057 0.05721588
 0.11922818 0.1312197  0.07913539 0.00547149] || 
 Prob of Reaching Poisoned Region Samples :1.0 Under Treshold Value:0.2
****************************************
BIG BANG: Infected Label :5 Detected
 On Labe:6 || 10 Shots Detection || Loss Results: [0.04121681 0.02933144 0.13108148 0.08108559 0.04346799 0.08522524
 0.20743947 0.06239453 0.1394537  0.01303403] || 
 Prob of Reaching Poisoned Region Samples :0.9 Under Treshold Value:0.2
****************************************
BIG BANG: Infected Label :6 Detected
 On Labe:7 || 10 Shots Detection || Loss Results: [1.2472291  0.08573119 0.09100791 0.18725798 0.2276497  0.10550883
 0.11114072 0.352344   0.0643043  0.09187966] || 
 Prob of Reaching Poisoned Region Samples :0.7 Under Treshold Value:0.2
****************************************
BIG BANG: Infected Label :7 Detected
....................


BIG BANG: Infected Label :36 Detected
 On Labe:37 || 10 Shots Detection || Loss Results: [0.03297332 0.0335109  0.02651408 0.00888407 0.13258283 0.07696318
 0.03469828 0.02349163 0.05614772 0.01716894] || 
 Prob of Reaching Poisoned Region Samples :1.0 Under Treshold Value:0.2
****************************************
BIG BANG: Infected Label :37 Detected
 On Labe:38 || 10 Shots Detection || Loss Results: [0.00813303 0.05932701 0.03996958 0.06097226 0.09461465 0.09641044
 0.0321881  0.03680894 0.0292761  0.01664384] || 
 Prob of Reaching Poisoned Region Samples :1.0 Under Treshold Value:0.2
****************************************
BIG BANG: Infected Label :38 Detected
 On Labe:39 || 10 Shots Detection || Loss Results: [0.06577442 0.01129459 0.28396013 0.15900452 0.04137421 0.08394548
 0.08697239 0.0422047  0.13182549 0.03948038] || 
 Prob of Reaching Poisoned Region Samples :0.9 Under Treshold Value:0.2
****************************************
BIG BANG: Infected Label :39 Detected
 On Labe:40 || 10 Shots Detection || Loss Results: [0.05811353 0.0308832  0.02704354 0.02164211 0.1018156  0.11730121
 0.02073213 0.04995939 0.11409676 0.01769998] || 
 Prob of Reaching Poisoned Region Samples :1.0 Under Treshold Value:0.2
****************************************
BIG BANG: Infected Label :40 Detected
 On Labe:41 || 10 Shots Detection || Loss Results: [0.09488855 0.05186722 0.0514556  0.02768068 0.09325781 0.04232858
 0.03394899 0.16096684 0.05411795 0.07893249] || 
 Prob of Reaching Poisoned Region Samples :1.0 Under Treshold Value:0.2
****************************************
BIG BANG: Infected Label :41 Detected
 On Labe:42 || 10 Shots Detection || Loss Results: [0.03488088 0.03941151 0.12827407 0.02262901 0.04048751 0.03010109
 0.00991904 0.01264083 0.03621254 0.01709652] || 
 Prob of Reaching Poisoned Region Samples :1.0 Under Treshold Value:0.2
****************************************
BIG BANG: Infected Label :42 Detected
****************************************
```
We can see PoisDetc can still be effective on multi-label detection scenarios.

#Mitigation

To investigate the mitigation performance of PoisDetc, we provide the link https://drive.google.com/file/d/1Jn-p6A0QYDAbIeJBfzEefgrYgbWyFt5v/view?usp=sharing to access. After download mitigation codes, access and run: 

```bash

python miti_run.py

```

The results like below

```bash


```

# In the future
In u feel interested in our work, please feel free to create an issue in this repo or contact me. We are glad to assist you to debug your experiment and seek the correct configuration for ur project.


