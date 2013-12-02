# -*- coding: utf-8 -*-
'''
Created on Nov 30, 2013

@author: alexandre
'''


import numpy as np
from os import path
#from graalUtil.num import uHist
from mlbench import util

info = {
    "url" : "http://archive.ics.uci.edu/ml/datasets/Connect-4",
    "name": "Connect-4",
    "x_type":"reals",
    "y_type":"classification",
    "key":"connect_4",
}

info['preprocessing'] = "converting o,b,x to 0,1,2 and loss, draw, win to 0,1,2"


        
def convert(raw_dir="raw"):
    str_mat = np.loadtxt(path.join(raw_dir,"connect-4.data"),delimiter=",",dtype=np.str)

    str_mat[str_mat == 'o'] = 0
    str_mat[str_mat == 'b'] = 1
    str_mat[str_mat == 'x'] = 2
    str_mat[str_mat == 'loss'] = 0
    str_mat[str_mat == 'draw'] = 1
    str_mat[str_mat == 'win'] = 2

    xy = str_mat.astype(np.float)
    
    info['x'], info['y'] = util.split_xy(xy)
    
    return info

info["description"]= """
Data Set Information:

This database contains all legal 8-ply positions in the game of connect-4 in which neither player has won yet, and in which the next move is not forced. 

x is the first player; o the second. 

The outcome class is the game theoretical value for the first player.


Attribute Information:

Attribute Information: (x=player x has taken, o=player o has taken, b=blank) 

The board is numbered like: 
6 . . . . . . . 
5 . . . . . . . 
4 . . . . . . . 
3 . . . . . . . 
2 . . . . . . . 
1 . . . . . . . 
a b c d e f g 

1. a1: {x,o,b} 
2. a2: {x,o,b} 
3. a3: {x,o,b} 
4. a4: {x,o,b} 
5. a5: {x,o,b} 
6. a6: {x,o,b} 
7. b1: {x,o,b} 
8. b2: {x,o,b} 
9. b3: {x,o,b} 
10. b4: {x,o,b} 
11. b5: {x,o,b} 
12. b6: {x,o,b} 
13. c1: {x,o,b} 
14. c2: {x,o,b} 
15. c3: {x,o,b} 
16. c4: {x,o,b} 
17. c5: {x,o,b} 
18. c6: {x,o,b} 
19. d1: {x,o,b} 
20. d2: {x,o,b} 
21. d3: {x,o,b} 
22. d4: {x,o,b} 
23. d5: {x,o,b} 
24. d6: {x,o,b} 
25. e1: {x,o,b} 
26. e2: {x,o,b} 
27. e3: {x,o,b} 
28. e4: {x,o,b} 
29. e5: {x,o,b} 
30. e6: {x,o,b} 
31. f1: {x,o,b} 
32. f2: {x,o,b} 
33. f3: {x,o,b} 
34. f4: {x,o,b} 
35. f5: {x,o,b} 
36. f6: {x,o,b} 
37. g1: {x,o,b} 
38. g2: {x,o,b} 
39. g3: {x,o,b} 
40. g4: {x,o,b} 
41. g5: {x,o,b} 
42. g6: {x,o,b} 
43. Class: {win,loss,draw}
"""

if __name__ == "__main__":
    util.check_dict(convert())
