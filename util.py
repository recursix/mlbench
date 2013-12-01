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
preprocessing
""".split('\n')

def check_dict(d):
    for attr in mandatory_fields:
        val = d[attr]

def load_file(name,**kwargs):
    a = np.loadtxt(name, dtype=np.str, **kwargs)
            
    xy = np.empty(a.shape, dtype=np.float)
    
    for i,col in enumerate(a.T):
        col_ = col.copy()
        col_[ col == '?' ] = 'NaN'
        xy[:,i] = col_.astype(np.float)
    
    x = xy[:,:-1]
    y = xy[:,-1]
    return x,y

def convert_date(date):
    dt=datetime.strptime("1/31/1998","%m/%d/%Y")
    return float( dt.strftime("%s") )
