# -*- coding: utf-8 -*-

from mlbench import util
from os import path

info = {
    "url" : "http://archive.ics.uci.edu/ml/datasets/Cylinder+Bands", # url of a web page for the dataset
    "name": "Cylinder Bands", # full name of the dataset
    "key":"cylinder_bands", # short name of the dataset, complying with mudule naming in python (the name of the current module should be <key>.py)
    "y_type":"enum", # the type of the y space. (will be enum for now) 
    "x_type":None, # x_type can be complex see below 
    "preprocessing": "", # breifly describes how the original dataset was transformed 
}

src_url = "http://archive.ics.uci.edu/ml/machine-learning-databases/cylinder-bands/" 
file_name = 'bands.data'
def fetch(raw_dir): # takes care of fetching all required files into raw_dir
    util.fetch(raw_dir, src_url, file_name)
    

# x_type is a tuple of primitives, taking values from "float", "int" and "enum". 
x_type = ['int'] + ['enum']*19 + ['float']*19
info['x_type'] = tuple(x_type)


def convert(raw_dir, max_features):
    """
    returns a dictionary containing the required fields for the dataset.
    """

    # In the data file, one instance is splitted over two lines.
    # The following code write a fixed file. 
    fixed_file_name = file_name + '2'    
    with open(path.join(raw_dir,file_name)) as f_in:
        with open(path.join(raw_dir,fixed_file_name),'w') as f_out:          
            for line in f_in.readlines():
                line = line.strip()              
                f_out.write(line)
                if len(line) > 0 and line[-1] != ',':
                    f_out.write('\n')
                
    info['x'], info['y'] = util.convert_uci_classif(
        info['x_type'], info['y_type'], raw_dir,fixed_file_name) 
    
    return info

info["description"]= """
1. Title: Cylinder bands

2. Sources:
    (a) Creator: Bob Evans
         RR Donnelley & Sons Co.
         Gallatin Division
          801 Steam Plant Rd
         Gallatin, Tennessee 37066-3396
         (615) 452-5170
    (b) Donor: same
    (c) Date: August, 1995

3. Past Usage:

    Evans, B., and Fisher, D. (1994). Overcoming process delays with
    decision tree induction. IEEE Expert , Vol. 9, No. 1, 60--66.

4. Relevant Information:n

Here's the abstract from the above reference:

ABSTRACT: Machine learning tools show significant promise for
knowledge acquisition, particularly when human expertise is
inadequate. Recently, process delays known as cylinder banding in
rotogravure printing were substantially mitigated using control rules
discovered by decision tree induction. Our work exemplifies a more
general methodology which transforms the knowledge acquisition task
from one in which rules are directly elicited from an expert, to one
in which a learning system is responsible for rule generation. The
primary responsibilities of the human expert are to evaluate the
merits of generated rules, and to guide the acquisition and
classification of data necessary for machine induction. These
responsibilities require the expert to do what an expert does best: to
exercise his or her expertise. This seems a more natural fit to an
expert's capabilities than the requirements of traditional
methodologies that experts explicitly enumerate the rules that they
employ.

5. Number of Instances: 512

6. Number of Attributes: 40 including the class attribute
   -- 20 attributes are numeric, 20 are nominal

7. Attribute Information:
     1. timestamp: numeric;19500101 - 21001231 
     2. cylinder number: nominal
     3. customer: nominal; 
     4. job number: nominal; 
     5. grain screened: nominal; yes, no 
     6. ink color: nominal;  key, type 
     7. proof on ctd ink:  nominal;  yes, no  
     8. blade mfg: nominal;  benton, daetwyler, uddeholm 
     9. cylinder division: nominal;  gallatin, warsaw, mattoon 
    10. paper type: nominal;  uncoated, coated, super 
    11. ink type: nominal;  uncoated, coated, cover 
    12. direct steam: nominal; use; yes, no *
    13. solvent type: nominal;  xylol, lactol, naptha, line, other 
    14. type on cylinder:  nominal;  yes, no  
    15. press type: nominal; use; 70 wood hoe, 70 motter, 70 albert, 94 motter 
    16. press: nominal;  821, 802, 813, 824, 815, 816, 827, 828 
    17. unit number: nominal;  1, 2, 3, 4, 5, 6, 7, 8, 9, 10 
    18. cylinder size: nominal;  catalog, spiegel, tabloid 
    19. paper mill location: nominal; north us, south us, canadian, 
                 scandanavian, mid european
    20. plating tank: nominal; 1910, 1911, other 
    21. proof cut: numeric;  0-100 
    22. viscosity: numeric;  0-100 
    23. caliper: numeric;  0-1.0 
    24. ink temperature: numeric;  5-30 
    25. humifity: numeric;  5-120 
    26. roughness: numeric;  0-2 
    27. blade pressure: numeric;  10-75 
    28. vafor i in [3,4,8,32,33,34]:
    x_type[i] = 'float'rnish pct: numeric;  0-100 
    29. press speed: numeric;  0-4000 
    30. ink pct: numeric;  0-100 
    31. solvent pct: numeric;  0-100 
    32. ESA Voltage: numeric;  0-16 
    33. ESA Amperage: numeric;  0-10 
    34. wax: numeric ;  0-4.0
    35. hardener:  numeric; 0-3.0 
    36. roller durometer:  numeric;  15-120 
    37. current density:  numeric;  20-50 
    38. anode space ratio:  numeric;  70-130 
    39. chrome content: numeric; 80-120 
    40. band type: nominal; class; band, no band *

8. Missing Attribute Values: yes, in 302 examples


9. Class Distribution: (out of 512 total instances)
    -- 312 No band
    -- 200 Band
"""
