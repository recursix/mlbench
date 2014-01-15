# -*- coding: utf-8 -*-
'''
Created on Nov 30, 2013

@author: jf, alex
'''

from mlbench import util

info = {
    "url" : "http://archive.ics.uci.edu/ml/datasets/Chess+%28King-Rook+vs.+King-Pawn%29", # url of a web page for the dataset
    "name": "King-Rook vs. King-Pawn", # full name of the dataset
    "key":"chess_KRKPA7", # short name of the dataset, complying with mudule naming in python (the name of the current module should be <key>.py)
    "y_type":"enum", # the type of the y space. (will be enum for now) 
    "x_type": None, # If None, it will be inferred from the content of the column
    "preprocessing": "changes class string to class number", # breifly describes how the original dataset was transformed 
}

src_url = "http://archive.ics.uci.edu/ml/machine-learning-databases/chess/king-rook-vs-king-pawn/" 
file_name = "kr-vs-kp.data"
def fetch(raw_dir): # takes care of fetching all required files into raw_dir
    util.fetch(raw_dir, src_url, file_name)
    

def convert(raw_dir, max_features):
    """
    returns a dictionary containing the required fields for the dataset.
    """
    return util.convert_uci_classif_( info, raw_dir, file_name ) 


info["description"]= """
Source:

Database originally generated and described by Alen Shapiro. 

Donor/Coder: 

Rob Holte (holte '@' uottawa.bitnet). 

The database was supplied to Holte by Peter Clark of the Turing Institute in Glasgow (pete '@' turing.ac.uk).


Data Set Information:

The dataset format is described below. Note: the format of this database was modified on 2/26/90 to conform with the format of all the other databases in the UCI repository of machine learning databases.


Attribute Information:

Classes (2): -- White-can-win ("won") and White-cannot-win ("nowin"). 

I believe that White is deemed to be unable to win if the Black pawn can safely advance. 

Attributes: see Shapiro's book.
"""