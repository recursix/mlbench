# -*- coding: utf-8 -*-
'''
Created on Nov 30, 2013

@author: alexandre
'''


import numpy as np
from os import path
#from graalUtil.num import uHist
from mlbench import util

info = {
    "url" : "http://archive.ics.uci.edu/ml/datasets/Spambase",
    "name": "Spambase",
    "x_type":"reals",
    "y_type":"classification",
    "key":"spambase",
}

info['preprocessing'] = ""



def convert(raw_dir="raw"):
    xy = np.loadtxt(path.join(raw_dir,"spambase.data"),delimiter=",")
    x,y = util.split_xy(xy)
    info['x'] = x
    info['y'] = y
    
    return info

info["description"]= """
"""

if __name__ == "__main__":
    util.check_dict(convert())
