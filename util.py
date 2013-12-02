# -*- coding: utf-8 -*-
'''
Created on Nov 30, 2013

@author: alexandre
'''

import numpy as np
from datetime import datetime
from warnings import warn
#from graalUtil.num import uHist
from os import path
import subprocess as sp

mandatory_fields = """x
y
name
key
url
description
x_type
y_type
preprocessing""".split('\n')


def check_dict(d):
    for attr in mandatory_fields:
        val = d[attr]
#    for key in ['x','y']:
#        print uHist( d[key],key)

def split_xy(xy):
    return xy[:,:-1], xy[:,-1]


def wget(url, raw_dir):
    sp.check_call(['wget', url, '-P',raw_dir])
    

def convert_uci_classif( x_type, y_type, raw_dir, file_name, delimiter=",", **kwargs ):
    type_list = x_type + [y_type]
    xy = converter( type_list, path.join( raw_dir, file_name), delimiter=delimiter, **kwargs )
    return split_xy(xy)
    

def converter(type_list, file_path, delimiter=",", **kwargs):
    
    a = np.loadtxt(file_path, dtype=np.str,delimiter=delimiter,**kwargs)
   
    xy = np.empty(a.shape, dtype=np.float)
    
    for i, (type_, col) in enumerate(zip(type_list,a.T)):

        
        col_ = col.copy()
        col_[ col == '?' ] = 'NaN'
        if type_ == 'enum':
            enum_map = build_enum_map(col_)
            print 'column %2d:'%i, type_, enum_map
            xy[:,i] = map(enum_map.get, col_ )
        elif type_ in ['float', 'int']:
            print i, type_
            xy[:,i] = col_.astype(np.float)
        else:
            raise ValueError('Unkown type : %s'%type_)
    return xy

def build_enum_map(col_str):
    """
    finds the unique values and assign an integer
    to each of these classes.
    """
    
    values = np.unique(col_str)

    if len(values) > len(col_str) / 2.:
        warn("Unusually high amount of classes, probably not an enum.")
        
    classes = np.arange(len(values))
    return dict( zip( values, classes ))

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
