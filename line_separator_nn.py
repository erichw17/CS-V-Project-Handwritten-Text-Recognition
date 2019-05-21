import tensorflow as tf
from tensorflow.keras import datasets, layers, models, regularizers
import os
import numpy as np
import matplotlib.pyplot as plt
import random
import cv2
from IAM_Line_Sep import cutAndSeparate as sep

def pred_next(model, data, end):
    partial_img = np.zeros([4, 2500])
    partial_img[:, :data.shape[1]] = data
    d = partial_img.flatten()
    d = np.expand_dims(d, axis=0)
    d = np.expand_dims(d, axis=2)
    cut = model.predict(d)
    cut = int(cut)
    if cut < 1:
        print("warning: cut < 0")
        cut = 1
    if abs(end-cut) < 100:
        return [cut]
    else:
        return [cut] + pred_next(model, data[:, cut:], end-cut)

def cutAndSeparate(img, IAM):
    edges, halves, data = sep(img, data=True)
    print(edges)
        
    if not IAM:
        edges = [0, img.shape[0]]
    
    data = data[:, edges[0]:edges[1]]

    model = models.load_model("sep_model.h5")

    cuts = pred_next(model, data, edges[1]-edges[0])

     
    plt.imshow(255-np.array(img), cmap=plt.cm.binary)

    last = edges[0]
    halves = []

    for cut in cuts:
        last += cut
        halves += [last]

    if edges[1] - halves[-1] < 100:
        halves.pop()

    return edges, halves
