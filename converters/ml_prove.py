# -*- coding: utf-8 -*-
'''
Created on Dec 1, 2013

@author: alexandre
'''


from mlbench import util
import os
import numpy as np

info = {
    "url" : "http://archive.ics.uci.edu/ml/datasets/First-order+theorem+proving#",
    "key":"ml_prove",
    "name": "First-order theorem proving",
    "y_type":"enum", # the type of the y space. (will be enum for now) 
    "x_type": ('float',)*56, # it also contains integers, but for simplicity, I've just put floats
    "preprocessing": "", # breifly describes how the original dataset was transformed 
}

src_url = "http://archive.ics.uci.edu/ml/machine-learning-databases/00249/" 
file_name = "ml-prove.tar.gz"
def fetch(raw_dir): # takes care of fetching all required files into raw_dir
    util.fetch(raw_dir, src_url, file_name)
    util.untar(raw_dir, file_name )

def convert(raw_dir, max_features):
    
    data_dir = os.path.join( raw_dir, 'ml-prove' )
    
    data_list = []
    for file_name in ['test.csv', 'validation.csv', 'train.csv' ]:
        data_list.append( util.convert_uci_classif( 
            info['x_type'], info['y_type'], data_dir, file_name) )
    
    
    x_list, y_list = zip( *data_list )
    
    info['x'] = np.vstack(x_list)
    info['y'] = np.concatenate(y_list)
    
    return info

info["description"]= """
Source:

James P Bridge, Sean B Holden and Lawrence C Paulson 

University of Cambridge 
Computer Laboratory 
William Gates Building 
15 JJ Thomson Avenue 
Cambridge CB3 0FD 
UK 

+44 (0)1223 763500 
forename.surname '@' cl.cam.ac.uk


Data Set Information:

See the file bridge-holden-paulson-details.txt in the submitted tarball.


Attribute Information:

The attributes are a mixture of static and dynamic features derived from theorems to be proved. See the paper for full details.


Relevant Papers:

Machine learning for first-order theorem proving: learning to select a good heuristic 
James P Bridge, Sean B Holden and Lawrence C Paulson 
Submitted for publication in the Journal of Automated Reasoning, Springer 2012/13. 
"""