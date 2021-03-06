import numpy as np
import cv2
import matplotlib.pyplot as plt

def word_seperator(img_path):   
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    return (word_separator_from_array(img))
    
def word_separator_from_array(img,data=False):

    mean = np.mean(img).astype(np.int64) #above bc don't want to deal with 255-
    edges = cv2.Canny(img,2*mean/3,2*mean)
    col_mean = np.mean(edges,axis=0).astype(np.int64)
    left_margin_not_found = True
    right_margin_not_found = True
    left_margin = 0
    right_margin = 0
    for i in range(len(col_mean)):
        if col_mean[i] > 0:
            if left_margin_not_found:
                left_margin = i
                left_margin_not_found = False
            else:
                right_margin = i
                right_margin_not_found = False
    #print(left_margin)
    #print(right_margin)
    #plt.subplot(121),plt.imshow(img,cmap = 'gray')
    #plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    #plt.subplot(122),plt.imshow(edges,cmap = 'gray')
    #plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    #plt.show()

    img = 255-np.array(img)
    #width = img.shape[1]
    maxes = np.max(img,axis=0).astype(np.int64)
    means = np.mean(img,axis=0).astype(np.int64)
    mult = maxes**2   
    sep = mult*1
    sep[sep < 15000] =  0 #changed hardcode to 20 from 40; makes the threshold for visible black marks lower, can "see" lighter grey strokes
    sep[sep >= 15000] = 100

    next = np.roll(sep,1) #create new array shifted right by 1
    next = next != sep  #True if next_element is diff than sep_element at same index
     # convert next array to int 0 or 100

    switches = []
    for i in range(next.shape[0]):
        if next[i]: #get all moments, True, where element at index changes 
            switches.append(i)
                     
    words = []
    tempFrontWord = left_margin #considering if no gap between beginning of line and first word
    for i in range(len(switches)):
        if switches[i] >= left_margin and switches[i] <= right_margin: #within bounds of edges
            sep_prev_minus_next = sep[switches[i]-1]-sep[switches[i]]
            if sep_prev_minus_next > 0:  # rather than -100, 100-0 signifies switch to blank space, while 0-100 signifies switch to words
                if i == len(switches)-1: # last index
                    words.append([tempFrontWord,switches[i]])
                elif switches[i+1]-switches[i] > 25: # minimum distance between spaces to classify as word space = 25
                    words.append([tempFrontWord,switches[i]])
                    tempFrontWord = switches[i+1]
    if tempFrontWord > 0 and words[-1][0] != tempFrontWord: # if there is no gap at end of line, and tempFrontWord isn't being double counted
        words.append([tempFrontWord, right_margin])
    if data:
        test = np.array([maxes,means,mult,sep,next])
        return words, test
    return words