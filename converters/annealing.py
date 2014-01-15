# -*- coding: utf-8 -*-
'''
Created on Dec 1, 2013

@author: alexandre
'''


from mlbench import util

info = {
    "url" : "http://archive.ics.uci.edu/ml/datasets/Annealing", # url of a web page for the dataset
    "name": "Annealing", # full name of the dataset
    "key":"annealing", # short name of the dataset, complying with mudule naming in python (the name of the current module should be <key>.py)
    "y_type":"enum", # the type of the y space. (will be enum for now) 
    "x_type": None, # If None, it will be inferred from the content of the column
    "preprocessing": "", # breifly describes how the original dataset was transformed 
}

src_url = "http://archive.ics.uci.edu/ml/machine-learning-databases/annealing/" 
file_name = 'anneal.data'
def fetch(raw_dir): # takes care of fetching all required files into raw_dir
    util.fetch(raw_dir, src_url, file_name)
    


def convert(raw_dir, max_features):
    """
    returns a dictionary containing the required fields for the dataset.
    """
    return util.convert_uci_classif_( info, raw_dir, file_name ) 
    

info["description"]= """
1. Title of Database: Annealing Data

2. Source Information: donated by David Sterling and Wray Buntine.

3. Past Usage: unknown

4. Relevant Information:
   -- Explanation: I suspect this was left by Ross Quinlan in 1987 at the
      4th Machine Learning Workshop.  I'd have to check with Jeff Schlimmer
      to double check this.

5. Number of Instances: 798

6. Number of Attributes: 38
   -- 6 continuously-valued
   -- 3 integer-valued
   -- 29 nominal-valued

7. Attribute Information:
    1. family:        --,GB,GK,GS,TN,ZA,ZF,ZH,ZM,ZS
    2. product-type:    C, H, G
    3. steel:        -,R,A,U,K,M,S,W,V
    4. carbon:        continuous
    5. hardness:    continuous
    6. temper_rolling:    -,T
    7. condition:    -,S,A,X
    8. formability:    -,1,2,3,4,5
    9. strength:    continuous
   10. non-ageing:    -,N
   11. surface-finish:    P,M,-
   12. surface-quality: -,D,E,F,G
   13. enamelability:    -,1,2,3,4,5
   14. bc:        Y,-
   15. bf:        Y,-
   16. bt:        Y,-
   17. bw/me:        B,M,-
   18. bl:        Y,-
   19. m:        Y,-
   20. chrom:        C,-
   21. phos:        P,-
   22. cbond:        Y,-
   23. marvi:        Y,-
   24. exptl:        Y,-
   25. ferro:        Y,-
   26. corr:        Y,-
   27. blue/bright/varn/clean:        B,R,V,C,-
   28. lustre:        Y,-
   29. jurofm:        Y,-
   30. s:        Y,-
   31. p:        Y,-
   32. shape:        COIL, SHEET
   33. thick:        continuous
   34. width:        continuous
   35. len:        continuous
   36. oil:        -,Y,N
   37. bore:        0000,0500,0600,0760
   38. packing:    -,1,2,3
   classes:        1,2,3,4,5,U
 
   -- The '-' values are actually 'not_applicable' values rather than
      'missing_values' (and so can be treated as legal discrete
      values rather than as showing the absence of a discrete value).
"""
