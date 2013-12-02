# -*- coding: utf-8 -*-
'''
Created on Dec 1, 2013

@author: alexandre
'''


from mlbench import util

info = {
    "url" : "http://archive.ics.uci.edu/ml/datasets/Annealing",
    "name": "Annealing",
    "y_type":"enum",
    "key":"annealing",
}

info['preprocessing'] = ""

x_type = ['enum']*38
for i in [3,4,8,32,33,34]:
    x_type[i] = 'float'
info['x_type'] = x_type

def convert(raw_dir="raw"):
    info['x'], info['y'] = util.convert_uci_classif(
        info['x_type'], info['y_type'], raw_dir,'anneal.data') 
    
    return info

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

if __name__ == "__main__":
    util.check_dict(convert())
