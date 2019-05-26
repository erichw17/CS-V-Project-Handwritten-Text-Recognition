# -*- coding: utf-8 -*-
"""
Created on Fri May 10 08:47:41 2019

@author: Erich Woo
"""

import numpy as np
import matplotlib.pyplot as plt
import random
import os
import cv2
from IAM_Word_Sep import word_separator_from_array as wsep
from tensorflow.keras import models

def main():
    dir = "data/lines"
    for i in range(3):
        dir += "/" + random.choice(os.listdir(dir)) #there are 2 extra subfolders before png file 
    print(dir)
    #dir = "data/lines/n03/n03-103/n03-103-07.png"
    #dir = "data/lines/test1.png"
    img = cv2.imread(dir, cv2.IMREAD_GRAYSCALE)
    data = wsep(img,data=True)[1]
    model = models.load_model('wsep_model_11-10-9-8_lr001.h5')
    w_cuts = predict_next(model,data,data.shape[1])
    
    plt.imshow(255-np.array(img), cmap=plt.cm.binary)
    prev = 0
    
    new_cuts = []
    for cut in w_cuts:
        new_cuts.append([prev+cut[0],prev+cut[1]])
        plt.plot((prev+cut[0],prev+cut[0]),(0,img.shape[0]),'b')
        plt.plot((prev+cut[1],prev+cut[1]),(0,img.shape[0]),'b')
        prev += cut[1]
        #print(len(os.listdir("data/lines/")))
    print(new_cuts)

def predict_next(model,data,last):
    partial_img = np.zeros([5, 2500])
    partial_img[:, :data.shape[1]] = data
    d = partial_img.flatten()
    d = np.expand_dims(d, axis=0)
    d = np.expand_dims(d, axis=2)
    w_cut = model.predict(d)
    w_cut = np.squeeze(w_cut,axis=0)
    w_cut = [int(i) for i in w_cut]
    #print(w_cut)
    #print(last)
    #print(w_cut[1])
    if (w_cut[0] < 0):
        w_cut[0] = 0  #fix errors of slightly negative prediction
    if w_cut[1]-w_cut[0] < 40:
        print("cut is less than 40")
        return predict_next(model, data[:, w_cut[1]:, last-w_cut[1]])
    if abs(last-w_cut[1]) < 50:
        return [w_cut]
    else:
        return [w_cut] + predict_next(model, data[:, w_cut[1]:], last-w_cut[1])
main()