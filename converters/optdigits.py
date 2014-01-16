# -*- coding: utf-8 -*-
'''
Created on Nov 30, 2013

@author: jf, alex
'''




from mlbench import util

info = {
    "url": "http://archive.ics.uci.edu/ml/datasets/Optical+Recognition+of+Handwritten+Digits",
    "key": "optdigits",
    "name": "Optical Recognition of Handwritten Digits Data Set",
    "y_type":"enum", # the type of the y space. (will be enum for now) 
    "x_type": ('int',)*64, 
    "preprocessing": ["Two versions of the dataset are provided. The preprocessed version is used."],
}



src_url = "http://archive.ics.uci.edu/ml/machine-learning-databases/optdigits/" 
file_name_list= ['optdigits.tes', 'optdigits.tra' ]
def fetch(raw_dir): # takes care of fetching all required files into raw_dir
    util.fetch(raw_dir, src_url, *file_name_list)


def convert(raw_dir, max_features):
    """
    returns a dictionary containing the required fields for the dataset.
    """
    return util.convert_uci_classif( info, raw_dir, file_name_list )
    

info["description"]= """
Source:

E. Alpaydin, C. Kaynak 
Department of Computer Engineering 
Bogazici University, 80815 Istanbul Turkey 
alpaydin '@' boun.edu.tr


Data Set Information:

We used preprocessing programs made available by NIST to extract normalized bitmaps of handwritten digits from a preprinted form. From a total of 43 people, 30 contributed to the training set and different 13 to the test set. 32x32 bitmaps are divided into nonoverlapping blocks of 4x4 and the number of on pixels are counted in each block. This generates an input matrix of 8x8 where each element is an integer in the range 0..16. This reduces dimensionality and gives invariance to small distortions. 

For info on NIST preprocessing routines, see M. D. Garris, J. L. Blue, G. T. Candela, D. L. Dimmick, J. Geist, P. J. Grother, S. A. Janet, and C. L. Wilson, NIST Form-Based Handprint Recognition System, NISTIR 5469, 1994.


Attribute Information:

All input attributes are integers in the range 0..16. 
The last attribute is the class code 0..9


Relevant Papers:

C. Kaynak (1995) Methods of Combining Multiple Classifiers and Their Applications to Handwritten Digit Recognition, MSc Thesis, Institute of Graduate Studies in Science and Engineering, Bogazici University. 
[Web Link] 

E. Alpaydin, C. Kaynak (1998) Cascading Classifiers, Kybernetika. [Web Link] 
[Web Link]
"""

