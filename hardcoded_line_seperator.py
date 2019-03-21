import numpy as np
import cv2
import matplotlib.pyplot as plt

file_name =  "data/forms/a01-000u.png"


img = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)
img = 255-np.array(img)
#img = img[640:2777]
#img = cv2.resize(img, (100, 100))

size = img.shape[0]
maxes = np.max(img, axis=1)
means = np.mean(img, axis=1)
mult = maxes*means/30
sep = mult*1
sep[sep < 40] = 0
sep[sep >= 40] = 100
switch = np.roll(sep, 1)
switch = switch != sep
switch = switch.astype(int)*100
switches = []
for i in range(switch.shape[0]):
    if switch[i]:
        switch[i+1:i+40] = 0
        switches += [i]
lines = []
switches = switches[:2]
for i in range(len(switches)):
    pass    


#print(maxes.shape)
#print(img.shape)

#for i in range(1776, 1960):
 #   print(str(i) + ": " + str(mult[i]-mult[i-1]))
avg = np.zeros(mult.shape[0])
s = 10
for i in range(s, mult.shape[0]-s):
    for j in range(i-s, i+s+1):
        avg[i] += mult[j]
    avg[i] /= 21

m = 50
maximums = []
for i in range(mult.shape[0]):
    higher = True
    for j in range(i-m, i+m+1):
        if j >= 0 and j < mult.shape[0] and j <= j != i and mult[i] < mult[j]:
            higher = False
    if higher:
        maximums += [i]

halves = []
for i in range(len(maximums)-1):
    halves += [(maximums[i]+maximums[i+1])/2]

for half in halves:
    plt.plot((half, half), (0, img.shape[1]), "b")

x = np.arange(size)

plt.imshow(img.transpose(), cmap=plt.cm.binary)
plt.plot(x, maxes)
plt.plot(x, means)
plt.plot(x, mult)
#plt.plot(x, avg)
#plt.plot(x, np.sort(mult))
#plt.plot(x, sep)
#plt.plot(x, switch)
plt.show()

