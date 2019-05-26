#!/usr/bin/python

import datetime
import argparse
import model_original
import model_new
import spell_check_1000 as spell_check
import preprocess
import line_separator_nn as lsep
import IAM_Word_Sep as wsep
import sys
import os
import cv2
import cv2_sep
import matplotlib.pyplot as plt
import numpy as np
from spell_check_1000 import OUTPUT_LEN

PATH_BASE = '/Users/Sanjay/Documents/CS_V_Final_Project/'

def parse_img(img_path, IAM, out_directory=None):

    #print(img_path)

    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img = np.array(img)
    #print(img.shape)

    edges, halves = lsep.cutAndSeparate(img, IAM)

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
    for j in range(len(lines)):
        word_ends = wsep.word_separator_from_array(lines[j])
        for i in range(len(word_ends)):
            word = lines[j][:, word_ends[i][0]:word_ends[i][1]]
            #if i == 0 and j == 0:
            #    cv2_sep.show_contours(words.squeeze())
            #if i == 0 and j == 0:
                #print(word)
            try:
                word_transpose = cv2.transpose(word)
                word_edges = wsep.word_separator_from_array(word_transpose)
                #print(word_edges)
                word_transpose = word_transpose[:, word_edges[0][0]:word_edges[0][1]]
                word = cv2.transpose(word_transpose)
            except:
                pass
            #if i == 0 and j == 0:
            #    plt.imshow(word_trimmed.squeeze())
            #    plt.show()
            #    plt.imshow(word.squeeze())
            #    plt.show()
            word = preprocess.preprocess_from_array(word)
            words.append(word)
    #print(words)

    words = np.array(words)
    #plt.imshow(words[24].squeeze())
    #plt.show()
    #cv2_sep.show_contours(words[0].squeeze())
    #htr = model_new.SimpleHTR(mode='test', weights_file='weights_final_new.h5')
    #responses = htr.predict_from_array(words)
    #print(responses)
    htr = model_new.SimpleHTR(mode='test', weights_file='weights_final_new.h5')
    responses = htr.predict_from_array(words)
    responses = np.array(np.array([np.array(preprocess.one_hot_encode(preprocess.numerical_decode(x)[:OUTPUT_LEN].ljust(OUTPUT_LEN))) for x in responses]))
    #print(responses)

    spell_checker = spell_check.SimpleSpellCheck(weights_file='spell_check_weights_alternate_1000_2_no_dropout_all.h5')
    responses = spell_checker.predict(responses)
    out_file_name =  os.path.join((out_directory if out_directory else ''), os.path.basename(img_path).split('.')[0] + '_DECODED.txt')
    print(out_file_name)
    with open(out_file_name, 'w') as f:
        
        f.write('******************************\n')
        f.write('File ' + img_path + ' decoded on ' + str(datetime.datetime.now()) + ':\n\n')

        for i in range(len(responses)):
        #decoded_row = preprocess.numerical_decode(row)
        #if (decoded_row != '_'):
            f.write(preprocess.one_hot_decode(responses[i]) + ' ')

        f.write('\n******************************\n')
        f.close()

    
def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--IAM', help='Use IAM data')
    parser.add_argument('-d', '--data', help='directory of data')
    parser.add_argument('-o', '--out_directory', help='directory of output file')
    args = parser.parse_args()

    if (args.IAM):
        parse_img(PATH_BASE + 'data/forms/' + (args.data if args.data else 'a01-000x') + '.png', args.IAM, out_directory=args.out_directory)
    else:
        assert args.data
        parse_img(PATH_BASE + 'data/forms/' + args.data, args.IAM)

if __name__ == "__main__":
    main()
