#!/usr/bin/env python3

import tensorflow as tf
import matplotlib.pyplot as plt
from keras.models import Model
from keras.layers import Input, Lambda, TimeDistributed, Dropout, Permute, Reshape, LSTM, Conv2D, Dense, Activation, MaxPool2D, Flatten, Bidirectional, GRU
from keras import backend as K
from keras import regularizers
import sys
import os
import numpy as np
import preprocess
import argparse
import matplotlib.pyplot as plt
import datetime
#a


#CHANGE LABEL_PATH AND IMG_DIR_PATH TO PATHS USED FOR LOCAL DIRECTORY
PATH_BASE = '/Users/Sanjay/Documents/CS_V_Final_Project/'
IMG_DIR_PATH = PATH_BASE + 'data/words/'
LABEL_PATH = PATH_BASE + 'data/words.txt'
IMG_SIZE = (1, 128, 32)
BATCH_SIZE = 30
NUM_RNNs = 2
HIDDEN_SIZE = 100
ALPHABET_SIZE = 30
INPUT_SEQUENCE_LENGTH = 150
LABEL_LENGTHS = 53
USE_DROPOUT = True
USE_REGULARIZER = False

class SimpleHTR():

    def __init__(self, mode='train', weights_file=None):
        """
        Set up the neural net model to train (or test)
        
        Keyword Arguments:
        mode -- the mode of operating the neural net (training or test)
        weights_file -- the set of weights with which to pre-initialize the neural net
        """

        #Layer parameters
        kernels = [5, 5, 3, 3, 3]
        pools = [(2, 2), (2, 1), (2, 1), (2, 2), (2, 1)]
        num_filters = [4, 8, 16, 32, 150]
        num_layers = len(pools)

            #self.model = Sequential()
        input_data = Input(name='input', shape=IMG_SIZE)    
        conv = input_data

        #Convolutional layers
        for i in range(0, num_layers):
            conv_name = 'conv' + str(i)
            max_pool_name = 'max_pool' + str(i)
            conv = Conv2D(name=conv_name, kernel_size=(kernels[i], kernels[i]), filters=num_filters[i], activation='relu', data_format='channels_first')(conv)
            conv = MaxPool2D(name=max_pool_name, pool_size=pools[i], strides=pools[i], data_format='channels_first')(conv)
        
        #self.model.add(Permute((2, 1), input_shape=(10, 64)))
        
        inner = Flatten(name='flatten', data_format='channels_first')(conv)
        inner = Reshape((-1, 1), name='reshape')(inner)
        #self.model.add(Permute((2, 1)))
        
        #Recurrent layers
        lstm1 = Bidirectional(GRU(HIDDEN_SIZE, name='lstm1', return_sequences=True))(inner)
        for i in range(NUM_RNNs - 1):
            lstm1 = Bidirectional(GRU(HIDDEN_SIZE, name=('lstm' + str(i)), return_sequences=True))(lstm1)
        

        #Use of different techniques to avoid overfitting
        if USE_DROPOUT:
            lstm2 = Dropout(0.1, name='dropout')(lstm1)
        time_dist = TimeDistributed(Dense(ALPHABET_SIZE), name='time_dist')(lstm2)
        inner2 = Dense(ALPHABET_SIZE, name='dense')(time_dist)
        if USE_REGULARIZER:
            inner2 = Dense(ALPHABET_SIZE, name='regularizer', kernel_regularizer=regularizers.l2(0.01))(inner2)
        y_pred = Activation('softmax', name='softmax')(inner2)

        assert mode == 'train' or mode == 'test'
        #Model(inputs = input_data, outputs=y_pred).summary()
        
        #If the neural net is set up to train, build in the loss function
        if mode == 'train':
            y_true = Input(name='labels',
                       shape=[LABEL_LENGTHS], dtype='float32')
            input_length = Input(name='input_length', shape=[1], dtype='int64')
            label_length = Input(name='label_length', shape=[1], dtype='int64')
            
            #BUILDS IN LOSS INTO THE HTR MODEL
            loss_out = Lambda(ctc_lambda_func, output_shape=(1,), name='ctc')([y_pred, y_true, input_length, label_length])

            self.model = Model(inputs=[input_data, y_true, input_length, label_length], outputs=loss_out)

            self.model.compile(loss={'ctc': lambda y_true, y_pred: y_pred}, optimizer='adam', metrics=['accuracy'])
            print(self.model.summary())

        #If the neural net is set up to test, make the output the prediction
        elif mode == 'test': 

           self.model = Model(inputs=[input_data], outputs=y_pred)
           #print(self.model.summary())

        #Try to initialize neural net with weights
        if weights_file != None:
            try:
                self.model.load_weights(weights_file, by_name=True)
            except:
                print("Warning! Weights file does not exist! Neural net not initialized with weights!")
                
    def train(self, data, batch_size=32, epochs=10, out_file=None):
        """
        Train the model on data
        
        Arguments:
        data -- the data (along with labels) on which the model trains
        
        Keyword Arguments:
        batch_size -- the training batch size
        epochs -- the number of epochs to train
        out_file -- the output file to which to save weights
        """
        dataset_size = list(data.values())[0].shape[0]
        true_vals_dummy = np.zeros(dataset_size)
        self.model.fit(x=data, y=true_vals_dummy, validation_split=0.1,  batch_size=batch_size, epochs=epochs, verbose=1)
        if out_file != None:
            self.model.save_weights(out_file)

    def predict(self, test_dir_path):
        """
        Predict the words given by the image files in a directory
        
        Arguments:
        test_dir_path -- the directory path
        """
        imgs = preprocess.get_data(LABEL_PATH, test_dir_path, imgs_to_labels=True, one_hot=False, return_list=True)['input']
        img = imgs[0].squeeze()
        print(img.shape)
        plt.imshow(img)
        plt.show()
        labels = preprocess.get_data(LABEL_PATH, test_dir_path, imgs_to_labels=True, one_hot=False, return_list=True)['labels']
        out = self.model.predict({'input': imgs})
        out = out[:, 2:, :]

        #print(out)

        return K.get_value(K.ctc_decode(out, input_length=np.ones(out.shape[0])*out.shape[1],
                                        greedy=True, beam_width=10, top_paths=2)[0][0]), labels

    def predict_from_array(self, imgs):
        """
        Predict the words given by an array corresponding to an image
        
        Arguments:
        imgs -- the image arrays
        """
        out = self.model.predict({'input': imgs})
        out = out[:, 2:, :]

        return K.get_value(K.ctc_decode(out, input_length=np.ones(out.shape[0])*out.shape[1],
                                        greedy=True, beam_width=10, top_paths=2)[0][0])

def ctc_lambda_func(args):
    """
    Calculate the ctc loss between predicted and true word values
    
    Arguments:
    args -- a tuple containing all the input data and labels
    """
    y_pred, y_true, input_length, label_length = args
    y_pred = y_pred[:, 2:, :]
    return K.ctc_batch_cost(y_true, y_pred, input_length, label_length)                                                                            


def main():
    """Method to run neural net from command line"""
    
    #Command line argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', help='Mode in which to operate the neural net, \'train\' or \'test\'')
    parser.add_argument('-e', '--epochs', help='Number of epochs to train, default 10', type=int)
    parser.add_argument('-w', '--weights', help='Optional pre-loaded weights')
    parser.add_argument('-d', '--data', help='directory of training data')
    parser.add_argument('-t', '--test_data', help='directory of test data')
    args = parser.parse_args()

    sess = tf.Session()
    with sess.as_default():

        #Set up to verify test set
        if (args.mode=='test'):
            htr = SimpleHTR(mode='test', weights_file=(args.weights if args.weights else None))
            test_dir_path = IMG_DIR_PATH + (args.test_data if args.test_data else 'a01/a01-000u')
            responses, labels = htr.predict(test_dir_path)
            for i in range(len(responses)):
                print(preprocess.numerical_decode(responses[i]) + ' ---> ' + preprocess.numerical_decode(labels[i], should_spell_check=False))
                
        #Set up to train on data
        elif args.mode == 'train':
            htr = SimpleHTR(mode='train', weights_file=(args.weights if args.weights else None))
            data = preprocess.get_data(LABEL_PATH, img_dir_path=(IMG_DIR_PATH+args.data if args.data else IMG_DIR_PATH), imgs_to_labels=True, one_hot=False, return_list=True)
            htr.train(data, epochs=(args.epochs if args.epochs else 10), out_file=(args.weights if args.weights else None))
            
            print('\n*********************************\n Training Complete: ' + str(datetime.datetime.now()) + '\n*********************************\n\n')
                            
        else:
            raise InvalidArgumentError('No valid mode of operating neural net specified!')

if __name__ == '__main__':
    main()
