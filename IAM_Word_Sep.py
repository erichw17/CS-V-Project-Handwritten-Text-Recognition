import numpy as np
import cv2
import matplotlib.pyplot as plt

def word_seperator(img_path):   
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
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
            
    words = []
    tempFrontWord = 0 #considering if no gap between beginning of line and first word
    for i in range(len(switches)):
        sep_prev_minus_next = sep[switches[i]-1]-sep[switches[i]]
        if i == 0 and sep_prev_minus_next < 0: # if gap between beginning of line and first word
            tempFrontWord = switches[i]
        elif sep_prev_minus_next > 0:  # rather than -100, 100-0 signifies switch to blank space, while 0-100 signifies switch to words
            if i == len(switches)-1: # last index
                words.append([tempFrontWord,switches[i]])
            elif switches[i+1]-switches[i] > 25: # minimum distance between spaces to classify as word space = 25
                words.append([tempFrontWord,switches[i]])
                tempFrontWord = switches[i+1]
    if tempFrontWord > 0 and words[-1][0] != tempFrontWord: # if there is no gap at end of line, and tempFrontWord isn't being double counted
        words.append([tempFrontWord, img.shape[1]])
    
    return words
