#!/usr/bin/python

import model
import preprocess
import IAM_Line_Sep as lsep
import IAM_Word_Sep as wsep
import sys
import os
import cv2
import numpy as np


def parse_img(img_path):

    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img = np.array(img)
    #print(img.shape)

    edges, halves = lsep.cutAndSeparate(img)

    line_dividers = [(int(halves[i]) if (halves[i] > edges[0] and halves[i] < edges[1]) else None)  for i in range(len(halves))]
    #print(line_dividers)
    line_dividers = [x for x in line_dividers if x != None]
    #print(line_dividers)
    line_dividers = [edges[0]] + line_dividers + [edges[1]]

    lines = []
    for i in range(len(line_dividers)-1):
        lines.append(img[line_dividers[i]:line_dividers[i+1], :])

    lines = np.array(lines)
    #print(lines)

    words = []
    for line in lines:
        word_ends = wsep.word_separator_from_array(line)
        for i in range(len(word_ends)):
            word = line[:, word_ends[i][0]:word_ends[i][1]]
            word = preprocess.preprocess_from_array(word)
            words.append(word)
    #print(words)

    words = np.array(words)

    htr = model.SimpleHTR(mode='test', weights_file='weights_tiny.h5')
    responses = htr.predict_from_array(words)
    for row in responses:
        decoded_row = preprocess.numerical_decode(row)
        if (decoded_row != '_'):
            print(decoded_row)

    
def main():

    parse_img('/Users/Sanjay/Documents/CS_V_Final_Project/data/forms/a01-000x.png')

if __name__ == "__main__":
    main()
