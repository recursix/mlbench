# -*- coding: utf-8 -*-
'''
Created on Jan 16, 2014

@author: JF
'''



#from graalUtil.num import uHist
from mlbench import util
import gzip
from os import path

info = {
    "url" : "http://archive.ics.uci.edu/ml/datasets/KDD+Cup+1999+Data",
    "name": "KDD Cup 1999 Data",
    "key": "kddcup99",
    "y_type": "enum",  # the type of the y space. (will be enum for now)
    "x_type": None,  # If None, it will be inferred from the content of the column
    "preprocessing": "",  # briefly describes how the original dataset was transformed
}

src_url = "http://archive.ics.uci.edu/ml/machine-learning-databases/kddcup99-mld/"
file_name = "kddcup.data.gz"

def fetch(raw_dir):  # takes care of fetching all required files into raw_dir
    util.fetch(raw_dir, src_url, file_name)
    

def convert(raw_dir, max_features):
    
    # extract only one line out of 10 since the dataset fails to load in memory (using numpy.loadtxt with str data type)
    file_name_ = "kddcup_sub.data"
    with gzip.open( path.join(raw_dir, file_name ), 'r') as fd_read:
        with open(  path.join(raw_dir, file_name_), 'w') as fd_write:
            for i,line in enumerate(fd_read): 
                if i%10 == 0:
                    fd_write.write( line )
    
    return util.convert_uci_classif(info, raw_dir, file_name_)


info["description"] = """
Abstract:

This is the data set used for The Third International Knowledge Discovery and Data Mining Tools Competition, which was
held in conjunction with KDD-99 The Fifth International Conference on Knowledge Discovery and Data Mining. The
competition task was to build a network intrusion detector, a predictive model capable of distinguishing between
``bad'' connections, called intrusions or attacks, and ``good'' normal connections. This database contains a standard
set of data to be audited, which includes a wide variety of intrusions simulated in a military network environment.


Relevant Papers:

Salvatore J. Stolfo, Wei Fan, Wenke Lee, Andreas Prodromidis, and Philip K. Chan. Cost-based Modeling and Evaluation
for Data Mining With Application to Fraud and Intrusion Detection: Results from the JAM Project.


Papers That Cite This Data Set1:

Stephen D. Bay and Dennis F. Kibler and Michael J. Pazzani and Padhraic Smyth. The UCI KDD Archive of Large Data Sets
for Data Mining Research and Experimentation. SIGKDD Explorations, 2. 2000.


Citation Request:

Please refer to the Machine Learning Repository's citation policy
"""
