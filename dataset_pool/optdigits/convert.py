# -*- coding: utf-8 -*-
'''
Created on Nov 30, 2013

@author: jf
'''

import numpy as np
import os
import cPickle as pickle

train_file = "optdigits.tra"
test_file = "optdigits.tes"

info = {
    "url": "http://archive.ics.uci.edu/ml/datasets/Optical+Recognition+of+Handwritten+Digits",
    "name": "Optical Recognition of Handwritten Digits Data Set",
    "x_type": "reals",
    "y_type": "classification",
    "description": "We used preprocessing programs made available by NIST to extract normalized bitmaps of handwritten digits from a preprinted form. From a total of 43 people, 30 contributed to the training set and different 13 to the test set. 32x32 bitmaps are divided into nonoverlapping blocks of 4x4 and the number of on pixels are counted in each block. This generates an input matrix of 8x8 where each element is an integer in the range 0..16. This reduces dimensionality and gives invariance to small distortions.",
    "preprocessing": [""]
}


def convert(raw_dir="raw"):
    train_array = np.loadtxt(os.path.join(raw_dir, train_file), delimiter=",", dtype=int)
    test_array = np.loadtxt(os.path.join(raw_dir, test_file), delimiter=",", dtype=int)

    train_x = train_array[:, :-1]
    train_y = train_array[:, -1]
    test_x = test_array[:, :-1]
    test_y = test_array[:, -1]

    output_dict = info
    output_dict["x"] = np.vstack((train_x, test_x))
    output_dict["y"] = np.hstack((train_y, test_y))
    output_dict["train_indices"] = range(len(train_array))
    output_dict["test_indices"] = range(len(train_array), len(train_array) + len(test_array))
    output_dict["key"] = os.path.split(os.getcwd())[-1]

    return output_dict

