# -*- coding: utf-8 -*-

import numpy as np
import cv2
import os
from IAM_Word_Sep import word_separator_from_array as wsep

def main():
    #print(len(os.listdir("data/lines/")))
    i = 0 
    for head in sorted(os.listdir("data/lines/")):
        #print(head)
        if os.path.isdir("data/lines/"+head+"/"):
            for form in sorted(os.listdir("data/lines/"+head+"/")):
                #print(form)
                if os.path.isdir("data/lines/"+head+"/"+form+"/"):
                    for line in sorted(os.listdir("data/lines/"+head+"/"+form+"/")):
                        #print(head+"/"+form+"/"+line)
                        preprocess(head+"/"+form+"/"+line[:-4])
                        print(i)
                        i += 1

def preprocess(key):
    filename = "data/lines/" + key + ".png"
    print(filename)
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    words, data = wsep(img, data=True)
    new_key = key[-11:] # bc of IAM dataset naming w/ extra dirs, just takes img name
    if new_key[0] == '/':
      new_key = new_key[1:] # IAM dataset invariable, take out if img name 1 too long
    np.save("data/word_labels/"+new_key, words)
    np.save("data/word_data/"+new_key, data)

main()