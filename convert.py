# -*- coding: utf-8 -*-
'''
Created on Dec 2, 2013

@author: alexandre
'''
from importlib import import_module
from os import path
import os
import util
from graalUtil.num import uHist
import json
import cPickle
import zlib
import sys

import numpy as np
        

def write_json( data, *file_path ):
    with open( path.join( *file_path ), 'w' ) as fd:
        json.dump( data, fd, indent=4 ) 

def write_pklz( obj, *file_path ):
    data = zlib.compress( cPickle.dumps(obj,cPickle.HIGHEST_PROTOCOL) )
    with open( path.join( *file_path ), 'w' ) as fd:
        fd.write(data)

def read_pklz( *file_path ):
    with open( path.join(*file_path), 'r' ) as fd:
        data = fd.read() 
    return cPickle.loads(zlib.decompress( data ))

def save_dataset( dataset, collection_dir,  non_info_fields = ('x','y') ):
    dataset_dict = dataset.__dict__
    ds_dir = path.join( collection_dir, dataset.key )
    if not path.exists(ds_dir): os.makedirs( ds_dir )
    
    dataset_info = {'n_samples':dataset_dict['x'].shape[0]}
    for key in dataset_dict.iterkeys():
        if key in non_info_fields: continue
        dataset_info[key]  = dataset_dict[key]
        
    write_json(dataset_info, ds_dir, 'dataset_info.json' )
    write_pklz(dataset_dict, ds_dir, 'dataset.pklz' ) 
    
def convert_missing( dataset ):
    for i, col in enumerate( dataset.x.T ):
        missing = np.isnan( col )
        
        if missing.all():
            dataset.x[:,i] = 0 # there is not much to do
            continue
        
        valid = col[~missing]
        if np.any( missing ):
            
            type_ = dataset.x_type[i]
            if type_ == 'enum':
                default_val = np.max(valid) +1 # creating a new class
                dataset.x[missing,i] = default_val
    
            elif type_ == 'int':
                default_val = np.round( np.mean(valid) ) 
                dataset.x[missing,i] = default_val
                
            elif type_ == 'float':
                default_val = np.mean(valid)  
                dataset.x[missing,i] = default_val
 
def fetch_and_convert(dataset_key, tmp_dir = '/tmp/mlbench'):
    
    print 'Converting %s.'%dataset_key
        
    module = import_module("converters.%s"%dataset_key)
    
    raw_dir = path.join(tmp_dir, dataset_key)
    if not path.exists(raw_dir): os.makedirs(raw_dir)
    
    print 'fetch dataset'
    module.fetch(raw_dir)
    
    print 'converting dataset'
    dataset_dict = module.convert(raw_dir, 500)
    assert dataset_key == dataset_dict['key']

    return util.DictToObj( dataset_dict ) # much easier to work with


def analyze_dataset( dataset ):
    
    util.check_fields(dataset.__dict__)

    print 'x.shape = ', dataset.x.shape
    print 'y.shape = ', dataset.y.shape

    for i, col in enumerate( dataset.x.T ):
        print uHist(col, 'col %d (%s)'%(i,dataset.x_type[i]))
        if len(np.unique(col)) == 1:
            print '***WARNING*** This feature is useless, it takes only one value'
    
    print uHist( dataset.y, 'y' )
    
    print
    
    
    

def convert_all( dataset_key_list, collection_dir, tmp_dir = '/tmp/mlbench'):
    for dataset_key in dataset_key_list:
        dataset = fetch_and_convert(dataset_key, tmp_dir)
        convert_missing( dataset )
        analyze_dataset( dataset )
        save_dataset(dataset, collection_dir ) 
        
            


if __name__ == "__main__":
    dataset_list = [
        'annealing',
        'biodeg',
        'census-income',
        'chess_KRKPA7',
        'connect_4',
        'covtype',
        'cylinder_bands',
        'ml_prove',
        'mushroom',
        'optdigits',
        'ozone',
        'spambase',
        'statlog_satimage',
        'wall-robot',
        'wdbc'
        ]
    
    collection_dir = path.expandvars( "$HOME/data/dataset_collection/classification" )

    if len(sys.argv) > 1:
        dataset_list = sys.argv[1].split(',')
    if len(sys.argv) > 2:
        collection_dir = sys.argv[2]
    
    convert_all(dataset_list, collection_dir)
    
    