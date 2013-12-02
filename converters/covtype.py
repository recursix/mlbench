# -*- coding: utf-8 -*-
'''
Created on Nov 30, 2013

@author: pascal
'''

import numpy as np
import os
import cPickle as pickle

filename = "covtype.data.gz"

info = {
        "name" : "Covertype",
        "url" : "http://archive.ics.uci.edu/ml/datasets/Covertype",
        "description" : "Predicting forest cover type from cartographic variables only",
        "x_type" : "reals",
        "y_type" : "classification"
        }

def convert(raw_dir="raw"):
    matrix = np.loadtxt( os.path.join(raw_dir, filename), delimiter=',', dtype=int )
    X = matrix[:,:-1]
    Y = matrix[:,-1]

    output_dict = info
    output_dict["x"] = X
    output_dict["y"] = Y
    output_dict["key"] = os.path.split(os.getcwd())[-1]
    return output_dict
    
