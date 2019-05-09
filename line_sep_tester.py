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
    if abs(end-cut) < 100:
        return [cut]
    else:
        return [cut] + pred_next(model, data[:, cut:], end-cut)

file_name = "data/forms/"+random.choice(os.listdir("data/forms/"))
img = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)
edges, halves, data = sep(img, data=True)

data = data[:, edges[0]:edges[1]]

model = models.load_model("sep_model.h5")

cuts = pred_next(model, data, edges[1]-edges[0])

 
plt.imshow(255-np.array(img), cmap=plt.cm.binary)

last = edges[0]

for cut in cuts:
    last += cut
    plt.plot((0, img.shape[1]), (last, last), "b")
    
for edge in edges:
    plt.plot((0, img.shape[1]), (edge, edge), "k")


plt.show()
