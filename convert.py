#!/usr/bin/env python
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


def analyze_dataset( dataset, min_features = 20, max_features=500 ):
    
    
    util.check_fields(dataset.__dict__)
    
    for i, col in enumerate( dataset.x.T ):
        print uHist(col, 'col %d (%s)'%(i,dataset.x_type[i]))
        if len(np.unique(col)) == 1:
            print '***WARNING*** Feature %d is constant across the whole dataset.'%(i)
    
    print uHist( dataset.y, 'y' )
    
    n_features = dataset.x.shape[1]
    assert n_features >= min_features, "Dataset %s is having %d < %d features"%(dataset.key, n_features, min_features)
    assert n_features <= max_features, "Dataset %s is having %d > %d features"%(dataset.key, n_features, max_features)
    
    
    print
    
def shuffle_and_subsample( dataset, max_samples=10000 ):
    m = dataset.x.shape[0]
    
    idx = np.arange(m)
    np.random.shuffle(idx)
    if m > max_samples:
        print 'sub sampling x from %d to %d.'%(m, max_samples)
        idx = idx[:max_samples] # shuffle instead of subsampling to void duplicate samples
        
    dataset.x = dataset.x[idx,:]
    dataset.y = dataset.y[idx]
    

def convert_all( dataset_key_list, collections_dir, max_samples= 10000):
    collection_dir = path.join(collections_dir,'classification')
    src_dir = path.join(collections_dir,'classification_src')
    for dataset_key in dataset_key_list:
        try:
            dataset = fetch_and_convert(dataset_key, src_dir)
            convert_missing( dataset )
            shuffle_and_subsample( dataset, max_samples)
            analyze_dataset( dataset )
            save_dataset( dataset, collection_dir )
            
        except KeyboardInterrupt:
            print 'Cancelling convert'
            break 
        
        
def get_dataset_keys():
    converters_dir = path.join( path.dirname(__file__), 'converters' )
    dataset_key_list = []
    for file_name in os.listdir(converters_dir):
        if file_name.startswith('_'): continue 
        key, ext = path.splitext(file_name)
        if ext == '.py': dataset_key_list.append( key )
    return dataset_key_list
    
if __name__ == "__main__":
    collection_dir = path.expandvars( "$HOME/data/dataset_collection" )

    if len(sys.argv) > 1:
        dataset_key_list = sys.argv[1].split(',')
    else:
        dataset_key_list = get_dataset_keys()

    if len(sys.argv) > 2:
        collection_dir = sys.argv[2]
    
    convert_all(dataset_key_list, collection_dir)
    
    
