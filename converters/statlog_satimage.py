# -*- coding: utf-8 -*-
'''
Created on Nov 30, 2013

@author: pascal
'''

import numpy as np
import os
import cPickle as pickle

train_file = "sat.trn"
test_file = "sat.tst"

info = {
    "url": "http://archive.ics.uci.edu/ml/datasets/Statlog+%28Landsat+Satellite%29",
    "name": "Statlog (Landsat Satellite)",
    "x_type": "reals",
    "y_type": "classification",
    "description": "Multi-spectral values of pixels in 3x3 neighbourhoods in a satellite image, and the classification associated with the central pixel in each neighbourhood",
}


def convert(in_dir="raw", out_dir="."):
    train_array = np.loadtxt(os.path.join(in_dir, train_file), delimiter=" ", dtype=int)
    test_array = np.loadtxt(os.path.join(in_dir, test_file), delimiter=" ", dtype=int)

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

