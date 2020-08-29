

from keras import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Input, Convolution2D, ZeroPadding2D, MaxPooling2D, Flatten, Dense, Dropout

from keras import Model

import keras

class GTSRBModel:
    def __init__(self, restore, session=None):
        self.num_channels = 3
        self.image_size = 32
        self.num_labels = 43

        model = Sequential()

        model.add(Conv2D(32, (5, 5),
                         input_shape=(32, 32, 3)))
        model.add(Activation('relu'))
        model.add(Conv2D(32, (5, 5)))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Conv2D(64, (3, 3)))
        model.add(Activation('relu'))
        model.add(Conv2D(64, (3, 3)))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Flatten())
        model.add(Dense(256))
        model.add(Activation('relu'))
        model.add(Dense(43))
        #model.add(Activation('softmax'))

        model.load_weights(restore)

        self.model = model

    def predict(self, data):
        return self.model(data)

    def pre(self,data):
        out = self.model.layers[-9].output
        model_new = Model(self.model.layers[0].input, out)
        return (model_new(data))

    def give(self,black):
        out = self.model.layers[-9].output
        model_new = Model(self.model.layers[0].input, out)
        return (model_new.predict(black))

class GTSRBModel2:
    def __init__(self, restore, session=None):
        self.num_channels = 3
        self.image_size = 32
        self.num_labels = 43

        model = Sequential()

        model.add(Conv2D(64, (3, 3),
                         input_shape=(32, 32, 3)))
        model.add(Activation('relu'))
        model.add(Conv2D(64, (3, 3)))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Conv2D(128, (3, 3)))
        model.add(Activation('relu'))
        model.add(Conv2D(128, (3, 3)))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2),name='feature'))

        model.add(Flatten())
        model.add(Dense(512))
        model.add(Activation('relu'))
        # model.add(Dense(256))
        # model.add(Activation('relu'))
        model.add(Dense(43))
        #model.add(Activation('softmax'))

        model.load_weights(restore)

        self.model = model

    def trojan_neuron(self, img):
        out = self.model.layers[-2].output
        model_new = Model(self.model.layers[0].input, out)

        return (model_new(img))

    def predict(self, data):
        return self.model(data)

    def feature(self,data):
        out = self.model.get_layer('feature').output
        model_new = Model(self.model.layers[0].input, out)
        return (model_new(data))

    def feature_predict(self,data):
        out = self.model.get_layer('feature').output
        model_new = Model(self.model.layers[0].input, out)
        return (model_new.predict(data))

class GTSRBModels:
    def __init__(self, restore, session=None):
        model = Sequential()

        model.add(Conv2D(32, (3, 3),
                         input_shape=[32,32,3]))
        model.add(Activation('relu'))
        model.add(Conv2D(32, (3, 3)))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        #model.add(Dropout(0.25))

        model.add(Conv2D(64, (3, 3)))
        model.add(Activation('relu'))
        model.add(Conv2D(64, (3, 3)))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        #model.add(Dropout(0.25))
        # model.add(Conv2D(params[4], (3, 3)))
        # model.add(Activation('relu'))
        # model.add(Conv2D(params[5], (3, 3)))
        # model.add(Activation('relu'))
        # model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Flatten())
        model.add(Dense(512))
        model.add(Activation('relu'))

        model.add(Dense(256))
        model.add(Activation('relu'))

        model.add(Dense(43))


        model.load_weights(restore)

        self.model = model

    def predict(self, data):
        return self.model(data)


    def pre(self,data):
        out = self.model.layers[-9].output
        model_new = Model(self.model.input, out)
        return (model_new(data))

class GTSRBModels2:
    def __init__(self, restore, session=None):
        model = Sequential()

        model.add(Conv2D(32, (3, 3),
                         input_shape=[32,32,3]))
        model.add(Activation('relu'))
        model.add(Conv2D(32, (3, 3)))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        #model.add(Dropout(0.25))

        model.add(Conv2D(64, (3, 3)))
        model.add(Activation('relu'))
        model.add(Conv2D(64, (3, 3)))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        #model.add(Dropout(0.25))
        # model.add(Conv2D(params[4], (3, 3)))
        # model.add(Activation('relu'))
        # model.add(Conv2D(params[5], (3, 3)))
        # model.add(Activation('relu'))
        # model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Flatten())
        model.add(Dense(256))
        model.add(Activation('relu'))

        # model.add(Dense(256))
        # model.add(Activation('relu'))

        model.add(Dense(43))

        model.load_weights(restore)

        self.model = model

    def predict(self, data):
        return self.model(data)


    def pre(self,data):
        out = self.model.layers[-9].output
        model_new = Model(self.model.input, out)
        return (model_new(data))

















class model_tf:

    def __init__(self, restore,session=None):


        model=keras.models.load_model(restore)



        self.model=model







    def predict(self,data):

        out = self.model.layers[-2].output

        model_new = Model(self.model.layers[0].input, out)
        return (model_new(data))

    def give(self,black):
        out = self.model.layers[-1].output
        model_new = Model(self.model.layers[0].input, out)
        return (model_new.predict(black))