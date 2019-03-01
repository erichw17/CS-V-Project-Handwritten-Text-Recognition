import sys
import os
import random
import numpy as np
import cv2
from sklearn.preprocessing import OneHotEncoder
#import model

IMAGE_SIZE = (128, 32)
PREDICTED_SEQUENCE_LENGTH = 256
MAX_LEN = 53

"""Source code from https://github.com/githubharald/SimpleHTR/blob/master/src/SamplePreprocessor.py consulted"""

def preprocess(img_path):

    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img = np.array(img)
    #print(img)
    #print(np.zeros(5))

    (wt, ht) = IMAGE_SIZE
    #print(IMAGE_SIZE)
    (h, w) = img.shape
    #print((w, h))
    target = 255*np.ones([ht, wt])
    s = max(w/wt, h/ht)
    newSize = (max(min(wt, int(w / s)), 1), max(min(ht, int(h/s)), 1))
    #print(newSize)
    img = cv2.resize(img, newSize)
    target[0:newSize[1], 0:newSize[0]] = img
    
    img = cv2.transpose(target)

    mean, std = cv2.meanStdDev(img)
    img = (img - mean) if std == 0 else (img - mean)/std
    img = np.array(img, ndmin=3)

    return img

def nested_list_dir(dir_path):
    dirlist = []
    for name in os.listdir(dir_path):
        if os.path.exists(dir_path + '/' + name):
            if not os.path.isdir(dir_path + '/' + name):
                dirlist.append(name)
            else:
                dirlist.extend([name + '/' + filename for filename in nested_list_dir(dir_path + '/' + name)])
        else:
            continue
    return dirlist

def preprocess_batch(img_dir_path):
    imgs = {}
    for filename in nested_list_dir(img_dir_path):
        try:
            img = preprocess(img_dir_path + '/' + filename)
            imgs[os.path.basename(filename).split('.')[0]] = img
        except:
            pass
    return imgs

def encode_char(char):
    if ord(char) == 32:
        return 0
    elif ord(char) == 46:
        return 1
    elif 97 <= ord(char) and ord(char) <= 122:
        return (ord(char) - 94)
    elif 65 <= ord(char) and ord(char) <= 90:
        return (ord(char) - 62)
    else:
        return 2

def string_encode(label):
    return np.array([encode_char(char) for char in list(label.ljust(MAX_LEN))])

def one_hot_encode(label):
    label = list(label.lower())
    encoded_labels = []
    for char in label:
        array = np.zeros(29)
        array[encode_char(char)] = 1
        encoded_labels.append(array)
    return np.array(encoded_labels)

def get_data(label_path, img_dir_path=None, imgs_to_labels=False, one_hot=False, return_list=True):

    labels = {}
    img_label_file = open(label_path, 'r')
    for line in img_label_file:
        if line[0] == '#':
            continue
        else:
            line = line.split(' ')
            if not one_hot:
                labels[line[0]] = string_encode(line[-1].strip('\n'))
            else:
                labels[line[0]] = one_hot_encode(line[-1].strip('\n'))

    if img_dir_path == None:
        if imgs_to_labels:
            raise ValueError()
        else:
            return labels
    else:
        assert os.path.isdir(img_dir_path)
        basenames = []
        for filename in nested_list_dir(img_dir_path):
            basename = os.path.basename(filename).split('.')[0]
            basenames.append(basename)

        labels_subset = {}
        for basename in basenames:
            if basename in labels:
                labels_subset[basename] = labels[basename]

        if imgs_to_labels:
            img_labels = {}
            imgs = preprocess_batch(img_dir_path)
            for basename in labels_subset:
                #print(basename)
                try:
                    img_labels[basename] = [np.array(imgs[basename]), np.array(labels_subset[basename]), PREDICTED_SEQUENCE_LENGTH, np.array(labels_subset[basename]).shape[0]]
                except KeyError:
                    pass
            if not return_list:
                return img_labels
            else:
                data_list = list(map(np.array, zip(*list(img_labels.values()))))
                return {'input': data_list[0], 'labels': data_list[1], 'input_length': data_list[2], 'label_length': data_list[3]}
        else: 
            return labels_subset



def main():

    img_dir_path= "/Users/Sanjay/Documents/CS_V_Final_Project/data/words/a01"#a01-030x"#/a01-030x-02-07.png
    #"/Users/Sanjay/Documents/CS_V_Final_Project/data/words/a01/a01-030x/a01-030x-02-07.png
    label_path = '/Users/Sanjay/Documents/CS_V_Final_Project/data/words.txt'
    #for i in range(0, 5): 
    #    print(preprocess(img_dir_path+'a01-000u-00-0'+str(i)+'.png'))

    #print(one_hot_encode("ABCDE"))
    #print(preprocess_batch(img_dir_path))
    #labels = get_labels(label_path)
    #len_labels = [len(labels[label]) for label in labels]
    #print(max(len_labels))
    #print(nested_list_dir(img_dir_path)[0:10])
    print(get_data(label_path, img_dir_path=img_dir_path, imgs_to_labels=True))

if __name__ == "__main__":
    main()
