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

def convert_value(str_val):
    try:                return int(str_val)
    except ValueError:  pass
    try:                return float(str_val)
    except ValueError:  pass
    return str_val

def infer_column_type( str_list ):
    count = {
        int : 0,
        float : 0, 
        str : 0,
        "missing" : 0,
        }
    
    for str_val in str_list:
        if str_val == '?':
            count['missing'] += 1
        else:
            val = convert_value(str_val)
            count[type(val)] += 1

    assert sum(count.values()) == len(str_list)
    n = len(str_list) - count['missing']
    

def wget(url, raw_dir):
    sp.check_call(['wget', '-N', url, '-P',raw_dir])

def fetch( raw_dir, url_folder, *file_name_list ):
    for file_name in file_name_list:
        wget( '%s/%s'%(url_folder, file_name), raw_dir )

def uncompress(raw_dir, src, dst ):
    with open( path.join(raw_dir,dst),'w') as fd:
        sp.check_call(['gunzip', '-c', src ], cwd =raw_dir, stdout= fd )

def untar( raw_dir, src ):
    sp.check_call(['tar', '-xf',  src ], cwd=raw_dir)

def convert_uci_classif( x_type, y_type, raw_dir, file_name, delimiter=",", **kwargs ):
    type_list = x_type + (y_type,)
    xy = converter( type_list, path.join( raw_dir, file_name), delimiter=delimiter, **kwargs )
    return split_xy(xy)
    

def converter(type_list, file_path, delimiter=",", **kwargs):
    print file_path
    a = np.loadtxt(file_path, dtype=np.str,delimiter=delimiter,**kwargs)
    xy = np.empty(a.shape, dtype=np.float)
    
    assert a.shape[1] == len(type_list),  'num col = %d, num type = %d'%( a.shape[1] , len(type_list) )
    
    for i, (type_, col) in enumerate(zip(type_list,a.T)):

        col_ = col.copy()
        col_[ col == '?' ] = 'NaN'
        if type_ == 'enum':
            enum_map = build_enum_map(col_)
            xy[:,i] = map(enum_map.get, col_ )
        elif type_ in ['float', 'int']:
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
    dt=datetime.strptime(date,"%m/%d/%Y")
    return float( dt.strftime("%s") )
