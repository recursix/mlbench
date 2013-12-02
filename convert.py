# -*- coding: utf-8 -*-
'''
Created on Dec 2, 2013

@author: alexandre
'''
from importlib import import_module
from os import path
import os

def convert( dataset_key_list ):
    for dataset_key in dataset_key_list:
        module = import_module("converters.%s"%dataset_key)
        
        raw_dir = path.join('/tmp', dataset_key)
        if not path.exists(raw_dir): os.mkdir(raw_dir)
        module.fetch(raw_dir)
        dataset_dict = module.convert(raw_dir)
        print dataset_dict.keys()
        
        
convert( ['annealing' ])