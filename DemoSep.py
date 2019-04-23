import numpy as np
import cv2
import matplotlib.pyplot as plt
import os, random
from IAM_Word_Sep import word_separator_from_array as WS
from IAM_Line_Sep import cutAndSeparate as LS

file_name = "data/forms/"+random.choice(os.listdir("data/forms/"))
print(file_name)

img = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)
edges, halves = LS(img)
print(edges, halves)
cuts = [edges[0]] + halves + [edges[1]]
word_cuts = []
for i in range(len(cuts)-1):
    line = img[int(cuts[i]):int(cuts[i+1])]
    word_cuts += [WS(line)]



plt.imshow(255-img, cmap=plt.cm.binary)
for i in range(len(cuts)-1):
    plt.plot((img.shape[1], 0), (cuts[i], cuts[i]), "b")
    for j in word_cuts[i]:
        for x in j:
            plt.plot((x, x), (cuts[i], cuts[i+1]), "b")
plt.plot((img.shape[1], 0), (cuts[-1], cuts[-1]), "b")
plt.show()
