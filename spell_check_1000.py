#!/usr/bin/env python3

import tensorflow as tf
import matplotlib.pyplot as plt
from keras.models import Model, Sequential
from keras.layers import Input, Lambda, TimeDistributed, Dropout, Permute, Reshape, LSTM, Conv2D, Dense, Activation, MaxPool2D, Flatten, Bidirectional, RepeatVector
from keras import backend as K
from keras import regularizers
import sys
import os
import numpy as np
import preprocess
import model_new
import argparse
import datetime

PATH_BASE = '/home/mlHTR3/' #'/Users/Sanjay/Documents/CS_V_Final_Project/'
HIDDEN_SIZE = 1000
OUTPUT_LEN = 15
ALPHABET_SIZE = 29
NUM_RECURRENT_LAYERS = 1

class SimpleSpellCheck():

    def __init__(self, mode='train', weights_file=None):

        self.weights_file = weights_file
        self.model = Sequential()
        #self.model.add(LSTM(HIDDEN_SIZE, name='lstm_input', input_shape=(OUTPUT_LEN, ALPHABET_SIZE), return_sequences=True))
        self.model.add(LSTM(HIDDEN_SIZE, name='lstm_next', input_shape=(OUTPUT_LEN, ALPHABET_SIZE), return_sequences=False))
        self.model.add(Dropout(0, name='dropout_input'))
        self.model.add(RepeatVector(OUTPUT_LEN))
        for i in range(NUM_RECURRENT_LAYERS):
            self.model.add(LSTM(HIDDEN_SIZE, return_sequences=True))
        #self.model.add(LSTM(HIDDEN_SIZE, name='lstm_output2', return_sequences=True))
        self.model.add(Dropout(0, name='dropout_output'))
        self.model.add(TimeDistributed(Dense(ALPHABET_SIZE, name='time_dist')))
        self.model.add(Activation('softmax'))

        self.model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

        if weights_file:
            try:
                self.model.load_weights(weights_file)
            except:
                print('Warning! Weights File Failed to Load! Neural Net Not Initialized with Weights!')
        
    def train(self, x, y, num_epochs=50):
        print(self.model.summary())
        self.model.fit(x, y, epochs=num_epochs, batch_size=32, validation_split=0.1)
        self.model.save_weights(self.weights_file)
        #print(self.model.summary())

    def predict(self, x):
        words = self.model.predict(x)
        #words = list(map(lambda x: preprocess.one_hot_decode(x), x))
        return words

    def evaluate(self, x, y):
        loss = self.model.evaluate(x, y)
        return loss

def prepare_data(data_dir_path, weights=None, out_file_path=None):
    htr = model_new.SimpleHTR(mode='test', weights_file=weights)
    responses, labels = htr.predict(data_dir_path)
    responses = np.array(np.array([np.array(preprocess.one_hot_encode(preprocess.numerical_decode(x)[:OUTPUT_LEN].ljust(OUTPUT_LEN))) for x in responses]))
    #print(type(responses))
    #print(type(responses[0]))
    #print(type(responses[0][0]))
    labels = np.array(np.array([np.array(preprocess.one_hot_encode(preprocess.numerical_decode(x)[:OUTPUT_LEN].ljust(OUTPUT_LEN))) for x in labels]))
    print(type(labels))
    print(type(labels[0]))
    print(type(labels[0][0]))
    print(np.shape(labels))
    print(np.shape(responses))
    #print(responses)
    #print(labels)
    return responses, labels

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('mode', help='Mode in which to operate the neural net, \'train\' or \'test\'')
    parser.add_argument('-e', '--epochs', help='Number of epochs to train, default 10', type=int)
    parser.add_argument('-w', '--weights', help='Optional pre-loaded weights')
    parser.add_argument('-d', '--data', help='directory of training data')
    parser.add_argument('-t', '--test_data', help='directory of test data')
    args = parser.parse_args()

    spellcheck = SimpleSpellCheck(weights_file=(PATH_BASE + 'mlHTR/' + args.weights if args.weights else None))
    #print(preprocess.one_hot_encode('abcdefgh'))
    print(PATH_BASE + 'mlHTR/' + 'weights_final_new.h5')
    responses, labels = prepare_data(PATH_BASE + 'data/words/' + (args.data if args.data else ''), weights=(PATH_BASE + 'mlHTR/' + 'weights_final_new.h5'))
    
    '''
    responses_decoded = list(map(lambda x: preprocess.one_hot_decode(x), list(responses)))
    print(responses_decoded)
    labels_decoded = list(map(lambda x: preprocess.one_hot_decode(x), list(labels)))
    print(labels_decoded)
    '''
    
    if (args.mode == 'train'):
        spellcheck.train(responses, labels, num_epochs=(args.epochs if args.epochs else 10))
    elif (args.mode == 'test'):
        #print(spellcheck.evaluate(responses, labels))
        words = spellcheck.predict(responses)
        for i in range(len(words)):
#            print(words)
#            print(labels)
            print(str(preprocess.one_hot_decode(words[i])) + '  --->  ' + str(preprocess.one_hot_decode(labels[i])))
#            print(np.amax(words[i] - labels[i]))
if __name__ == '__main__':
    main()




