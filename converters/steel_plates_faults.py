# -*- coding: utf-8 -*-
'''
Created on Jan 17, 2014

@author: alex
'''


from mlbench import util

info = {
    "url" : "http://archive.ics.uci.edu/ml/datasets/Steel+Plates+Faults", # url of a web page for the dataset
    "name": "Steel Plates Faults", # full name of the dataset
    "key":"steel_plates_faults", # short name of the dataset, complying with mudule naming in python (the name of the current module should be <key>.py)
    "y_type":"enum", # the type of the y space. (will be enum for now) 
    "x_type": None, # If None, it will be inferred from the content of the column
    "preprocessing": "", # breifly describes how the original dataset was transformed 
}

src_url = "http://archive.ics.uci.edu/ml/machine-learning-databases/00198/" 
file_name = 'Faults.NNA'
def fetch(raw_dir): # takes care of fetching all required files into raw_dir
    util.fetch(raw_dir, src_url, file_name)
    


def convert(raw_dir, max_features):
    """
    returns a dictionary containing the required fields for the dataset.
    """
    return util.convert_uci_classif( info, raw_dir, file_name, delimiter = None )
    

info["description"]= """
Source:

Semeion, Research Center of Sciences of Communication, Via Sersale 117, 00128, Rome, Italy. 
www.semeion.it


Data Set Information:

Type of dependent variables (7 Types of Steel Plates Faults): 
1.Pastry 
2.Z_Scratch 
3.K_Scatch 
4.Stains 
5.Dirtiness 
6.Bumps 
7.Other_Faults 


Attribute Information:

27 independent variables: 
X_Minimum 
X_Maximum 
Y_Minimum 
Y_Maximum 
Pixels_Areas 
X_Perimeter 
Y_Perimeter 
Sum_of_Luminosity 
Minimum_of_Luminosity 
Maximum_of_Luminosity 
Length_of_Conveyer 
TypeOfSteel_A300 
TypeOfSteel_A400 
Steel_Plate_Thickness 
Edges_Index 
Empty_Index 
Square_Index 
Outside_X_Index 
Edges_X_Index 
Edges_Y_Index 
Outside_Global_Index 
LogOfAreas 
Log_X_Index 
Log_Y_Index 
Orientation_Index 
Luminosity_Index 
SigmoidOfAreas 


Relevant Papers:

1.M Buscema, S Terzi, W Tastle, A New Meta-Classifier,in NAFIPS 2010, Toronto (CANADA),26-28 July 2010, 978-1-4244-7858-6/10 Â©2010 IEEE 
2.M Buscema, MetaNet: The Theory of Independent Judges, in Substance Use & Misuse, 33(2), 439-461,1998



Citation Request:

dataset provided by Semeion, Research Center of Sciences of Communication, Via Sersale 117, 00128, Rome, Italy. 
www.semeion.it
"""
