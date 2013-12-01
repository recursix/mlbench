# -*- coding: utf-8 -*-
'''
Created on Dec 1, 2013

@author: alexandre
'''

import numpy as np
from os import path
#from graalUtil.num import uHist
from mlbench import util

info = {
    "url" : "http://archive.ics.uci.edu/ml/datasets/First-order+theorem+proving#",
    "name": "First-order theorem proving",
    "x_type":"reals",
    "y_type":"classification",
    "key":"ml_prove",
}

info['preprocessing'] = "Merging train, valid and test."

def convert(raw_dir="raw"):
    
    xy_list = [np.loadtxt(path.join(raw_dir,name),delimiter=",") 
        for name in ['test.csv','train.csv','validation.csv'] ]
    
    xy = np.vstack(xy_list)
    
    info['x'], info['y'] = util.split_xy(xy)
    
    return info

info["description"]= """
1. Title: First-order theorem proving

2. Sources:

   (a) James P Bridge, Sean B Holden and Lawrence C Paulson

       University of Cambridge
       Computer Laboratory
       William Gates Building
       15 JJ Thomson Avenue
       Cambridge CB3 0FD
       UK 

       +44 (0)1223 763500 
       forename.surname@cl.cam.ac.uk

   (b) Sean B Holden - details as (a).

   (c) Date: 17th April 2013

3. Past Usage:

   (a) Machine learning for first-order theorem proving: learning to
       select a good heuristic James P Bridge, Sean B Holden and
       Lawrence C Paulson Submitted for publication in the Journal of
       Automated Reasoning, Springer 2012/13.

       Please include a citation if you use this data.

   (b) We wish to predict which of a set of five heuristics will
       provide the fastest proof, given features derived from a
       theorem to be proved. A sixth possible prediction is to decline
       to attempt a proof, should the theorem be assessed as too
       difficult.

   (c) In prediction terms this is a challenging problem. However we
       can do better than any individual heuristic and obtain
       performance comparable to that of a hand-crafted selection
       mechanism employing around 75 addition heuristics. The ability
       to decline a proof is also beneficial.

4. Relevant Information Paragraph:

   Files:

   Expanding the tarball ml-prove.tar produces a directory ml-prove/ 
   containing the files:

   all-data-raw.csv            - raw data used to derive training, 
                                 validation and test data.
   all-data-raw-statistics.txt - min, max, mean and standard deviation 
                                 for raw data. (Tabulated below.)
   train.csv                   - actual training, validation and test 
   validation.csv                sets used.
   test.csv
   all-data-statistics.txt     - min, max and correlation data for 
                                 combined actual data. (Tabulated below.) 

   Raw data: 

   Columns 1 to 14 are the static features and columns 15 to 53 are
   the dynamic features. (See the paper for a description of static
   and dynamic features.) The final five columns denote the time in
   seconds taken by each of the five heuristics to prove the relevant
   theorem. There was a time limit of 100 seconds.  An entry of -100
   denotes failure to obtain a proof within the time limit.  The first
   half of this data corresponds to the training data used. The second
   half was permuted and split to obtain the validation and test sets.

   Training, validation and test data: 

   These are the sets used in the reported experiments. Two redundant
   features (static feature 5 and dynamic feature 21 in the raw data)
   were removed. The features in the training set are normalised to
   zero mean and unit variance. Validation/test data was normalized
   using the coefficients computed for the training set. Labels are in
   the final six columns. The first five of those correspond to the
   five heuristics (H1 to H5) and contain +1 if the corresponding
   heuristic found a proof and was the fastest to do so, and -1
   otherwise. The final column contains +1 where no heuristic finds a
   proof within the time limit and -1 otherwise (H0 in the paper).

5. Number of Instances: 

   6118 in the raw data.

   The training, validation and test sets have 3059, 1529 and 1530
   respectively.

6. Number of Attributes:

   There are 13 static and 38 dynamic features for each instance. (See
   the paper for details regarding static/dynamic features. The raw 
   data has two more features, which are redundant.) Columns 1
   to 13 contain static features and columns 14 to 51 dynamic
   features.

7. Description of attributes:

   The full names for each attribute are provided in the paper, tables
   2 and 3.
   
   Raw data: all attributes are numeric. Attributes 5, 9, 11, 13
   and 35 are integer-valued. All other attributes are continuous.

   Training, validation and test data: all data are numeric and
   continuous on account of being normalized.

8. Missing Attribute Values: 

   There are no missing values.

9. Class Distribution: number of positive instances in the sets for
   each heuristic (H1 to H5) and the "decline" option H0.

                     H1   H2   H3   H4   H5   H0
   Training set:     556  229  373  303  312  1286
   Validation set:   260  133  187  146  159  644
   Test set:         273  124  188  168  153  624

"""

if __name__ == "__main__":
    util.check_dict(convert())
