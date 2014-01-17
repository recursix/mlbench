# -*- coding: utf-8 -*-
'''
Created on Jan 17, 2014

@author: alex
'''


from mlbench import util

info = {
    "url" : "http://archive.ics.uci.edu/ml/datasets/Thyroid+Disease", # url of a web page for the dataset
    "name": "Thyroid Disease", # full name of the dataset
    "key":"thyroid", # short name of the dataset, complying with mudule naming in python (the name of the current module should be <key>.py)
    "y_type":"enum", # the type of the y space. (will be enum for now) 
    "x_type": None, # If None, it will be inferred from the content of the column
    "preprocessing": "Only ann-train.data and ann-test.data were used. All other databases were ignored.", # breifly describes how the original dataset was transformed 
}

src_url = "http://archive.ics.uci.edu/ml/machine-learning-databases/thyroid-disease/" 
file_name_list = [ 'ann-train.data', 'ann-test.data' ]
def fetch(raw_dir): # takes care of fetching all required files into raw_dir
    util.fetch(raw_dir, src_url, *file_name_list)
    


def convert(raw_dir, max_features):
    """
    returns a dictionary containing the required fields for the dataset.
    """
    return util.convert_uci_classif( info, raw_dir, file_name_list, delimiter = None )
    

info["description"]= """
Source:

Ross Quinlan


Data Set Information:

# From Garavan Institute 
# Documentation: as given by Ross Quinlan 
# 6 databases from the Garavan Institute in Sydney, Australia 
# Approximately the following for each database: 

** 2800 training (data) instances and 972 test instances 
** Plenty of missing data 
** 29 or so attributes, either Boolean or continuously-valued 

# 2 additional databases, also from Ross Quinlan, are also here 

** Hypothyroid.data and sick-euthyroid.data 
** Quinlan believes that these databases have been corrupted 
** Their format is highly similar to the other databases 

# 1 more database of 9172 instances that cover 20 classes, and a related domain theory 
# Another thyroid database from Stefan Aeberhard 

** 3 classes, 215 instances, 5 attributes 
** No missing values 

# A Thyroid database suited for training ANNs 

** 3 classes 
** 3772 training instances, 3428 testing instances 
** Includes cost data (donated by Peter Turney) 



Attribute Information:

N/A


Relevant Papers:

Quinlan,J.R., Compton,P.J., Horn,K.A., & Lazurus,L. (1986). Inductive knowledge acquisition: A case study. In Proceedings of the Second Australian Conference on Applications of Expert Systems. Sydney, Australia. 
[Web Link] 

Quinlan,J.R. (1986). Induction of decision trees. Machine Learning, 1, 81--106. 
[Web Link]
"""
