# -*- coding: utf-8 -*-
'''
Created on Nov 30, 2013

@author: alexandre
'''

import numpy as np
from datetime import datetime

mandatory_fields = """x
y
name
key
url
description
x_type
y_type
preprocessing""".split('\n')

from graalUtil.num import uHist
def check_dict(d):
    for attr in mandatory_fields:
        val = d[attr]
    for key in ['x','y']:
        print uHist( d[key],key)

def split_xy(xy):
    return xy[:,:-1], xy[:,-1]

def load_file(name,**kwargs):
    a = np.loadtxt(name, dtype=np.str, **kwargs)
            
    xy = np.empty(a.shape, dtype=np.float)
    
    for i,col in enumerate(a.T):
        col_ = col.copy()
        col_[ col == '?' ] = 'NaN'
        xy[:,i] = col_.astype(np.float)
    
    return split_xy(xy)

def convert_date(date):
    dt=datetime.strptime("1/31/1998","%m/%d/%Y")
    return float( dt.strftime("%s") )
