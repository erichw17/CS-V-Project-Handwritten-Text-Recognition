import cv2
import numpy as np
import os
import random
import matplotlib.pyplot as plt

file_name = "data/other/1.png"
file_name = "data/forms/"+random.choice(os.listdir("data/forms/"))
#print(file_name)

def show_contours(image):

#image = cv2.imread(file_name)
    image = cv2.resize(image, (500, 700))
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    
    ret, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)
    
    kernel = np.ones((5, 80), np.uint8)
    img_dilation = cv2.dilate(thresh, kernel, iterations=1)
    
    ctrs, h = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])
    
    
    for i, ctr in enumerate(sorted_ctrs):
        x, y, w, h = cv2.boundingRect(ctr)
        
        roi = image[y:y+h, x:x+w]
        cv2.rectangle(image, (x,y), ( x + w, y + h ), (90, 0, 255), 2)
        
    cv2.imshow('marked areas', image)
    cv2.waitKey(0)
