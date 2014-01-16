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

verbose = 1

class DictToObj:
    """
    Just a wrapper around dict to make it behave like an object.
    >>> d = {'a':1,'b':3.0}
    >>> obj = DictToObj(d)
    >>> obj.a = 3
    >>> print d['a']
    3
    """
    def __init__(self, dict_):
        self.__dict__ = dict_

def check_dict(d):
    for attr in mandatory_fields:
        val = d[attr]
#    for key in ['x','y']:
#        print uHist( d[key],key)

def split_xy(xy, y_first=False):
    """
    y_first: True => first column contains labels; False => last column contains labels.
    """
    if y_first:
        return xy[:,1:], xy[:,0]
    else:
        return xy[:,:-1], xy[:,-1]

def convert_value(str_val):
    """
    Tries to convert to int, float or str and returns the first successful conversion.
    """
    try:                return int(str_val)
    except ValueError:  pass
    try:                return float(str_val)
    except ValueError:  pass
    return str(str_val)

def infer_column_type( str_list, verbose ):
    """
    A set of rules to infer the type of a given feature among 'float', 'int', 'enum'.
    It may return more than one type in case of ambiguity
    """
    
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

    unique = np.unique( str_list )
    unique_ratio = len(unique) / float(len(str_list))
    
    if verbose:
        if len(unique) <= 20:
            print 'unique : ', unique
        else: 
            print 'unique : %d values'%len(unique)
        print 'count : ', count
    
    assert sum(count.values()) == len(str_list)
    n = len(str_list) - count['missing']
    
    
    if count[int] == n: # only ints. This can be an enum or an int type
        
        if len(unique) <= 2:
            return 'enum','int' # highly likely to be an int
        if unique_ratio > 0.5:
            return 'int', # really unlikely to be an enum
        
        return 'int', 'enum' # can't distinguish between int or enum but int is more likely
    
    if count[float] + count[int] == n and count[float] > 0: 
        return 'float',
    
    if count[str] == n: # definetly an enum
        return 'enum',
    
    type_list = []
    if count[str] > 0:
        type_list.append( 'enum' )
    if count[int] > 0 and count[str] == 0:
        type_list.append( 'int' )
    
         
    return tuple(type_list)

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

def convert_uci_classif( info, raw_dir, file_name_list, delimiter=",", y_first=False, **kwargs ):
    """
    Some form of universal UCI converter. 
    """

    if isinstance( file_name_list, str ):
        file_name_list = [file_name_list]
    
    path_list = [ path.join( raw_dir, file_name ) for file_name in file_name_list ]
    
    xy, info['x_type'] = converter(info['x_type'], info['y_type'], path_list, delimiter=delimiter, y_first=y_first, **kwargs ) 
    info['x'], info['y'] = split_xy(xy, y_first)
    return info
    
def choose_type( type_, inferred_type, col ):
    if type_ is None:
        type_ = inferred_type[0]
        if len(inferred_type) > 1:
            print "***WARNING*** possible types for column %d are %s. Choosing %s"%(col, str(inferred_type), inferred_type[0] )
    else:
        if not type_ in inferred_type:
            print "***WARNING*** type %s specified for column %d but possible types are %s"%(type_, col, str(inferred_type) )

    return type_

def converter(x_type, y_type, path_list, delimiter=",", y_first=False, **kwargs):
    """
    y_first: True => first column contains labels; False => last column contains labels.
    """
    str_mat_list = []
    for file_path in path_list:
        str_mat_list.append(  np.loadtxt(file_path, dtype=np.str,delimiter=delimiter,**kwargs) )
    str_mat = np.vstack(str_mat_list)
    
    
    xy = np.empty(str_mat.shape, dtype=np.float)
    
    if x_type is None:
        x_type = [None]* (str_mat.shape[1]-1)
    else:
        x_type = list(x_type)
    
    type_list = x_type[:] # copy 
    
    if y_first:
        type_list.insert(0, y_type)
    else:
        type_list.append(y_type)

    assert str_mat.shape[1] == len(type_list),  'num col = %d, num type = %d'%( str_mat.shape[1] , len(type_list) )
    
    for i, col in enumerate(str_mat.T):
        verbose = type_list[i] is None

        inferred_types = infer_column_type(col, verbose)
        type_ = choose_type(type_list[i], inferred_types , i )
        if verbose:
            print 'type: proposed: %s, inferred: %s, chosen: %s'%( type_list[i], str(inferred_types), type_ )
            print 
        type_list[i] = type_


        col_ = col.copy()
        col_[ col == '?' ] = 'NaN'
        if type_ == 'enum':
            enum_map = build_enum_map(col_)
            xy[:,i] = map(enum_map.get, col_ )
        elif type_ in ['float', 'int']:
            xy[:,i] = col_.astype(np.float)
        else:
            raise ValueError('Unkown type : %s'%type_)
    return xy, type_list[:-1]

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
