# -*- coding: utf-8 -*-
'''
Created on Dec 2, 2013

@author: alexandre
'''
from importlib import import_module
from os import path
import os
import util

def convert( dataset_key_list ):
    for dataset_key in dataset_key_list:
        module = import_module("converters.%s"%dataset_key)
        
        raw_dir = path.join('/tmp', dataset_key)
        if not path.exists(raw_dir): os.mkdir(raw_dir)
        module.fetch(raw_dir)
        dataset_dict = module.convert(raw_dir, 500)
        print dataset_dict.keys()
        util.check_dict(dataset_dict)
        print 'x.shape = ', dataset_dict['x'].shape
        print 'y.shape = ', dataset_dict['y'].shape


if __name__ == "__main__":
    convert( ['annealing' ])