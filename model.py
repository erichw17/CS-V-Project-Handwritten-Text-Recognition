import tensorflow as tf
import matplotlib.pyplot as plt
from keras.models import Model
from keras.layers import Input, Lambda, TimeDistributed, Dropout, Permute, Reshape, LSTM, Conv2D, Dense, Activation, MaxPool2D, Flatten
from keras import backend as K
import sys
import os
import numpy as np
import preprocess

#print(tf.VERSION)

#CHANGE LABEL_PATH AND IMG_DIR_PATH TO PATHS USED FOR LOCAL DIRECTORY

IMG_DIR_PATH = '/Users/Sanjay/Documents/CS_V_Final_Project/data/words/a01'
LABEL_PATH = '/Users/Sanjay/Documents/CS_V_Final_Project/data/words.txt'
IMG_SIZE = (1, 128, 32)
BATCH_SIZE = 500
HIDDEN_SIZE = 100
ALPHABET_SIZE = 30
INPUT_SEQUENCE_LENGTH = 256
LABEL_LENGTHS = 53
USE_DROPOUT = True

class SimpleHTR():

    def __init__(self, batch_size):

        self.batch_size = batch_size

        kernels = [5, 5, 3, 3, 3]
        pools = [(2, 2), (2, 1), (2, 1), (2, 2), (2, 1)]
        num_filters = [32, 64, 128, 128, 256]
        num_layers = len(pools)

            #self.model = Sequential()
        input_data = Input(name='input', shape=IMG_SIZE)    
        conv = input_data

        for i in range(0, num_layers):
            conv = Conv2D(kernel_size=(kernels[i], kernels[i]), filters=num_filters[i], activation='relu', data_format='channels_first')(conv)
            conv = MaxPool2D(pool_size=pools[i], strides=pools[i], data_format='channels_first')(conv)
        
        #self.model.add(Permute((2, 1), input_shape=(10, 64)))
        
        inner = Flatten(data_format='channels_first')(conv)
        inner = Reshape((-1, 1))(inner)
        #self.model.add(Permute((2, 1)))
        lstm1 = LSTM(HIDDEN_SIZE, return_sequences=True)(inner)
        lstm2 = LSTM(HIDDEN_SIZE, return_sequences=True)(lstm1)
        if USE_DROPOUT:
            lstm2 = Dropout(0.3)(lstm2)
        time_dist = TimeDistributed(Dense(ALPHABET_SIZE))(lstm2)
        inner2 = Dense(ALPHABET_SIZE)(time_dist)
        y_pred = Activation('softmax')(inner2)

        #Model(inputs = input_data, outputs=y_pred).summary()

        y_true = Input(name='labels',
                   shape=[LABEL_LENGTHS], dtype='float32')
        input_length = Input(name='input_length', shape=[1], dtype='int64')
        label_length = Input(name='label_length', shape=[1], dtype='int64')
        
        #BUILDS IN LOSS INTO THE HTR MODEL
        loss_out = Lambda(ctc_lambda_func, output_shape=(1,), name='ctc')([y_pred, y_true, input_length, label_length])

        self.model = Model(inputs=[input_data, y_true, input_length, label_length], outputs=loss_out)

        self.model.compile(loss={'ctc': lambda y_true, y_pred: y_pred}, optimizer='adam', metrics=['accuracy'])
        print(self.model.summary())
    
    def calc_y_true(self):
        return np.zeros(ALPHABET_SIZE)

    def calc_input_length(self):
        #return np.zeros(self.batch_size)
        return np.zeros(1)

    def calc_label_length(self):
        #return np.zeros(self.batch_size)
        return np.zeros(1)

def ctc_lambda_func(args):
    y_pred, y_true, input_length, label_length = args
    y_pred = y_pred[:, 2:, :]
    return K.ctc_batch_cost(y_true, y_pred, input_length, label_length)                                                                            


def main():
    htr1 = SimpleHTR(5)

    data = preprocess.get_data(LABEL_PATH, img_dir_path=IMG_DIR_PATH, imgs_to_labels=True, one_hot=False, return_list=True)
    dataset_size = data['input'].shape[0]

    true_vals = np.zeros(dataset_size)
    htr1.model.fit(x=data,y=true_vals,batch_size=32,epochs=10,verbose=2)

if __name__ == '__main__':
    main()
