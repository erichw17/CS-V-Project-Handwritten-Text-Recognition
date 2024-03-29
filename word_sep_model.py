# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import os
import tensorflow as tf
from tensorflow.keras import models, layers

def main():
    data, labels = Data()
    
    model = models.Sequential()
    model.add(layers.MaxPooling1D(5, input_shape=(11350, 1)))
    model.add(layers.Flatten())
    #model.add(layers.Dense(4096, activation='relu'))
    model.add(layers.Dense(2048, activation='relu'))
    model.add(layers.Dense(1024, activation='relu'))
    model.add(layers.Dense(512, activation='relu'))
    model.add(layers.Dense(256, activation='relu'))
    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dense(2))
    
    model.compile(loss='mean_squared_error',
                  optimizer=tf.keras.optimizers.Adam(lr=.001),
                  metrics=['mean_absolute_error'])
    
    print(model.summary())
    
    history = model.fit(data, labels, batch_size=512, epochs=170, validation_split=0.2, verbose=1)
    
    model.save('wsep_model.h5')
    
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.show()
    
def Data():
    data = []
    labels = []
    
    #print(len(os.listdir("data/word_data/")))
    for key in sorted(os.listdir("data/word_data/")):
        stats = np.load("data/word_data/"+key)
        data += [stats]
        w_cuts = np.load("data/word_labels/"+key)
        labels += [w_cuts]
    
    new_data = []
    new_labels = []    
   
    #for each line file
    for i in range(len(labels)):
        prev = 0
        
        #w_cuts is shape (2,)
        for w_cuts in labels[i]:
            w_cuts = [int(i) for i in w_cuts]
            img = data[i][:,prev:]
            img_sect = np.zeros([5, 2270])
            img_sect[:,:img.shape[1]] = img
            new_data += [img_sect.flatten()]
            new_labels.append([w_cuts[0]-prev,w_cuts[1]-prev])
            prev = w_cuts[1]
    new_data = np.array(new_data)
    new_labels = np.array(new_labels)
    new_data = new_data[:, :, np.newaxis]
    return new_data, new_labels
                
main()