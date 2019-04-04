#!/usr/bin/python

import numpy as np
import cv2
import os
import random

def cutAndSeparate(img):
    img = 255-np.array(img)

    size = img.shape[0]
    maxes = np.max(img, axis=1)
    means = np.mean(img, axis=1)
    mult = maxes*means/30

    strip = img[:, 1100:1250]
    strip_means = np.mean(strip, axis = 1)
    strip_means += np.roll(strip_means, 1)
    strip_means += np.roll(strip_means, -1)
    strip_means[0] = 0
    strip_means[-1] = 0
    SM = strip_means

    topRange = mult[0:]
    topRange[topRange < 100] = 0
    top = 683+topRange.argmax()

    size = img.shape[0]
    maxes = np.max(img, axis=1)
    means = np.mean(img, axis=1)
    mult = maxes*means/30 

    m = 60
    maximums = []
    max_vals = []
    for i in range(mult.shape[0]):
        higher = True
        for j in range(i-m, i+m+1):
            if j >= 0 and j < mult.shape[0] and j <= j != i and mult[i] < mult[j]:
                higher = False
        if higher:
            maximums += [i]
            max_vals += [mult[i]]

    s = 60
    max_SM = []
    max_SM_vals = []
    for i in range(SM.shape[0]):
        higher = True
        for j in range(i-s, i+s+1):
            if j >= 0 and j < SM.shape[0] and j <= j != i and SM[i] < SM[j]:
                higher = False
        if higher:
            max_SM += [i]
            max_SM_vals += [SM[i]]

    top_3_ind = np.argsort(max_SM_vals)[-3:]
    top_3 = []
    for i in top_3_ind:
        top_3 += [max_SM[i]]
    edges = np.sort(top_3_ind)[1:]
    for i in range(2):
        edges[i] = max_SM[edges[i]]

    halves = []
    half_scores = []
    for i in range(len(maximums)-1):
        halves += [(maximums[i]+maximums[i+1])/2]
        half_scores += [(max_vals[i]+max_vals[i+1])/2]

    for maximum in maximums:
        if maximum > edges[0]+10 and mult[maximum] > 150:
            edges[0] = maximum
            break

    for i in range(len(halves)):
        if halves[i] < edges[0]:
            e = halves[i+1]*2-halves[i+2]
            j = i
    halves.pop(j)
    edges[0] = e+10

    for maximum in maximums:
        if maximum < edges[1] and mult[maximum] > 150:
            e = maximum
    edges[1] = e

    for i in range(len(halves)):
        if halves[i] > edges[1]:
            edges[1] = halves[i-1]*2-halves[i-2]
            break

    return edges, halves
