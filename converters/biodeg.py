# -*- coding: utf-8 -*-
'''
Created on Nov 30, 2013

@author: pascal
'''

import numpy as np
import os
import cPickle as pickle

filename = "biodeg.csv"

info = {
        "name" : "QSAR biodegradation",
        "url" : "http://archive.ics.uci.edu/ml/datasets/QSAR+biodegradation",
        "description" : "Data set containing values for 41 attributes (molecular descriptors) used to classify 1055 chemicals into 2 classes (ready and not ready biodegradable).",
        "x_type" : "reals",
        "y_type" : "classification",
        "preprocessing" : "class RB=>0, class NRB=>1"
        }

def convert(raw_dir="raw"):
    matrix = np.loadtxt( os.path.join(raw_dir, filename), delimiter=';', dtype=float,converters = {41: lambda s: 0 if s=='RB' else 1} )
    X = matrix[:,:-1]
    Y = matrix[:,-1]

    output_dict = info
    output_dict["x"] = X
    output_dict["y"] = Y
    output_dict["key"] = os.path.split(os.getcwd())[-1]
    return output_dict
    
