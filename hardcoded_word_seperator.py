import numpy as np
import cv2
import matplotlib.pyplot as plt

file_name =  "data/lines/a01/a01-000u/a01-000u-00.png"

img = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)
img = 255-np.array(img)

width = img.shape[1]
maxes = np.max(img,axis=0)
means = np.mean(img,axis=0)
mult = maxes*means/30

sep = mult*1
sep[sep < 40] =  0
sep[sep >= 40] = 100

next = np.roll(sep,1) #create new array shifted right by 1
next = next != sep  #True if next_element is diff than sep_element at same index
next = next.astype(int)*100 # convert next array to int 0 or 100

switches = []
for i in range(next.shape[0]):
    if next[i]: #get all moments, True, where element at index changes 
        switches.append(i)

gaps = []
halves = []
for i in range(len(switches)-1):
    if sep[switches[i]-1]-sep[switches[i]] > 0:  # rather than -100, 100-0 signifies switch to blank space, while 0-100 signifies switch to words
        if switches[i+1]-switches[i] > 25: # minimum distance between spaces to classify as word space = 25
            halves += [(switches[i]+switches[i+1])/2]
            gaps += [switches[i+1]-switches[i]]
print(gaps)

for half in halves:
    plt.plot((half, half), (0, img.shape[0]), "b")

x = np.arange(width)

plt.imshow(img, cmap=plt.cm.binary)
plt.plot(x, maxes)
plt.plot(x, means)
plt.plot(x, mult)
plt.plot(x, sep)
plt.show()
