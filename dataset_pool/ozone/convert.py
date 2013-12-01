# -*- coding: utf-8 -*-
'''
Created on Nov 30, 2013

@author: alexandre
'''

import numpy as np
from os import path
from graalUtil.num import uHist
from mlbench.util import load_file, convert_date

info = {
    "url" : "http://archive.ics.uci.edu/ml/datasets/Ozone+Level+Detection",
    "name": "Ozone Level Detection",
    "x_type":"reals",
    "y_type":"classification",
}

info['preprocessing'] = "using eighthr.data (eight hour data) and ignoring onehr.data"

def convert(in_dir="raw", out_dir="."):
    x,y = load_file(path.join(in_dir,"eighthr.data"),delimiter=",",
        converters={0:convert_date})
    print uHist(x)
    print uHist(y)
    

