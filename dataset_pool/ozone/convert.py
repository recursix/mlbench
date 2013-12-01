# -*- coding: utf-8 -*-
'''
Created on Nov 30, 2013

@author: alexandre
'''

from os import path
#from graalUtil.num import uHist
from mlbench.util import load_file, convert_date, check_dict

info = {
    "url" : "http://archive.ics.uci.edu/ml/datasets/Ozone+Level+Detection",
    "name": "Ozone Level Detection",
    "x_type":"reals",
    "y_type":"classification",
    "key":"ozone",
}

info["description"]= """

"""
info['preprocessing'] = "using eighthr.data (eight hour data) and ignoring onehr.data"



def convert(raw_dir="raw"):
    x,y = load_file(path.join(raw_dir,"eighthr.data"),delimiter=",",
        converters={0:convert_date})
    
    info['x'] = x
    info['y'] = y
    
    return info


if __name__ == "__main__":
    check_dict(convert())
