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

def save_dataset( dataset, ds_dir ):
    if not path.exists(ds_dir): os.makedirs( ds_dir )
    
    ds_info = {'n_samples':dataset['x'].shape[0]}
    for key in dataset.iterkeys():
        if key in ['x','y']: continue
        ds_info[key]  = dataset[key]
        
    write_json(ds_info, ds_dir, 'dataset_info.json' )
    write_pklz(dataset, ds_dir, 'dataset.pklz' ) 
    
def convert_missing( dataset ):
    for col, type_ in enumerate( dataset['x'].T ):
        pass
    pass  

def convert( dataset_key_list, collection_dir=None ):
    for dataset_key in dataset_key_list:
        
        print 'Converting %s.'%dataset_key
        
        module = import_module("converters.%s"%dataset_key)
        
        raw_dir = path.join('/tmp/mlbench', dataset_key)
        if not path.exists(raw_dir): os.mkdir(raw_dir)
        
        print 'fetch dataset'
        module.fetch(raw_dir)
        
        print 'converting dataset'
        dataset_dict = module.convert(raw_dir, 500)
        util.check_dict(dataset_dict)
        dataset = util.DictToObj( **dataset_dict ) # much easier to work with

        
        print 'x.shape = ', dataset.x.shape
        print 'y.shape = ', dataset.y.shape

        for i, col in enumerate( dataset.x.T ):
            print uHist(col, 'col %d (%s)'%(i,dataset.x_type[i]))
        
        print uHist( dataset.y, 'y' )
        print
        
        if collection_dir is not None:
            ds_dir =path.join( collection_dir, dataset_key)
            save_dataset(dataset_dict, ds_dir ) 
            
            


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
        'optdigits',
        'ozone',
        'spambase',
        'statlog_satimage',
        'wall-robot'
        ]
    
    collection_dir = path.expandvars( "$HOME/data/dataset_collection/classification" )

    if len(sys.argv) > 1:
        dataset_list = sys.argv[1].split(',')
    if len(sys.argv) > 2:
        collection_dir = sys.argv[2]
    
    convert(dataset_list, collection_dir)
    
    