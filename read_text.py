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

    line_dividers = [halves[i] for i in range(len(halves))]
    #print line_dividers

    lines = []
    for i in range(len(halves)-1):
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
    print(words)

    words = np.array(words)

    htr = model.SimpleHTR(mode='test', weights_file='weights_tiny_copy.h5')
    responses = htr.predict_from_array(words)
    for row in responses:
        print(preprocess.numerical_decode(row))

    
def main():

    parse_img('/home/mlHTR1/forms/a01-000u.png')

if __name__ == "__main__":
    main()
