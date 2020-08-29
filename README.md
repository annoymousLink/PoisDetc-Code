# PoisDetc-Code

# DEPENDENCIES 

Our code is implemented and tested on Keras with TensorFlow backend. Following packages are used by our code.

```bash
keras==2.2.2
numpy==1.14.0
tensorflow-gpu==1.10.1
h5py==2.6.0
Our code is tested on Python 2.7.12 and Python 3.6.8
```
We include a sample script demonstrating how to perform the reverse engineering technique on an infected model. There are several parameters that need to be modified before running the code, which could be modified here.

GPU device: if you are using GPU, specify which GPU you would like to use by setting the DEVICE variable via
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

```

Also we test PoisDetc on model with multiple infected labels
```bash
```


#Mitigation

To investigate the mitigation performance of PoisDetc
Just run

```bash

```

The results like below

```bash
```

# In the future
In u feel interested in our work, please feel free to create an issue in this repo or contact me. We are glad to assist you to debug your experiment and seek the correct configuration for ur project.


