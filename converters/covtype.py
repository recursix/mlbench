# -*- coding: utf-8 -*-
'''
Created on Nov 30, 2013

@author: pascal
'''


from mlbench import util

info = {
    "url" : "http://archive.ics.uci.edu/ml/datasets/Covertype",
    "name": "Covertype", # full name of the dataset
    "key":"covtype", # short name of the dataset, complying with mudule naming in python (the name of the current module should be <key>.py)
    "y_type":"enum", # the type of the y space. (will be enum for now) 
    "x_type": None, # If None, it will be inferred from the content of the column
    "preprocessing": "", # breifly describes how the original dataset was transformed 
}

src_url = "http://archive.ics.uci.edu/ml/machine-learning-databases/covtype/" 
file_name = "covtype.data.gz"
def fetch(raw_dir): # takes care of fetching all required files into raw_dir
    util.fetch(raw_dir, src_url, file_name)
    

def convert(raw_dir, max_features):
    """
    returns a dictionary containing the required fields for the dataset.
    """
    return util.convert_uci_classif_( info, raw_dir, file_name ) 
    



info["description"]= """
Source:

Original Owners of Database: 

Remote Sensing and GIS Program 
Department of Forest Sciences 
College of Natural Resources 
Colorado State University 
Fort Collins, CO 80523 
(contact Jock A. Blackard, jblackard '@' fs.fed.us or Dr. Denis J. Dean, denis.dean '@' utdallas.edu) 

Donors of database: 

1. Jock A. Blackard (jblackard '@' fs.fed.us) 
GIS Coordinator 
USFS - Forest Inventory & Analysis 
Rocky Mountain Research Station 
507 25th Street 
Ogden, UT 84401 

2. Dr. Denis J. Dean (denis.dean '@' utdallas.edu) 
Professor 
Program in Geography and Geospatial Sciences 
School of Economic, Political and Policy Sciences 
800 West Campbell Rd 
Richardson, TX 75080-3021 

3. Dr. Charles W. Anderson (anderson '@' cs.colostate.edu) 
Associate Professor 
Department of Computer Science 
Colorado State University 
Fort Collins, CO 80523 USA


Data Set Information:

Predicting forest cover type from cartographic variables only (no remotely sensed data). The actual forest cover type for a given observation (30 x 30 meter cell) was determined from US Forest Service (USFS) Region 2 Resource Information System (RIS) data. Independent variables were derived from data originally obtained from US Geological Survey (USGS) and USFS data. Data is in raw form (not scaled) and contains binary (0 or 1) columns of data for qualitative independent variables (wilderness areas and soil types). 

This study area includes four wilderness areas located in the Roosevelt National Forest of northern Colorado. These areas represent forests with minimal human-caused disturbances, so that existing forest cover types are more a result of ecological processes rather than forest management practices. 

Some background information for these four wilderness areas: Neota (area 2) probably has the highest mean elevational value of the 4 wilderness areas. Rawah (area 1) and Comanche Peak (area 3) would have a lower mean elevational value, while Cache la Poudre (area 4) would have the lowest mean elevational value. 

As for primary major tree species in these areas, Neota would have spruce/fir (type 1), while Rawah and Comanche Peak would probably have lodgepole pine (type 2) as their primary species, followed by spruce/fir and aspen (type 5). Cache la Poudre would tend to have Ponderosa pine (type 3), Douglas-fir (type 6), and cottonwood/willow (type 4). 

The Rawah and Comanche Peak areas would tend to be more typical of the overall dataset than either the Neota or Cache la Poudre, due to their assortment of tree species and range of predictive variable values (elevation, etc.) Cache la Poudre would probably be more unique than the others, due to its relatively low elevation range and species composition.


Attribute Information:

Given is the attribute name, attribute type, the measurement unit and a brief description. The forest cover type is the classification problem. The order of this listing corresponds to the order of numerals along the rows of the database. 

Name / Data Type / Measurement / Description 

Elevation / quantitative /meters / Elevation in meters 
Aspect / quantitative / azimuth / Aspect in degrees azimuth 
Slope / quantitative / degrees / Slope in degrees 
Horizontal_Distance_To_Hydrology / quantitative / meters / Horz Dist to nearest surface water features 
Vertical_Distance_To_Hydrology / quantitative / meters / Vert Dist to nearest surface water features 
Horizontal_Distance_To_Roadways / quantitative / meters / Horz Dist to nearest roadway 
Hillshade_9am / quantitative / 0 to 255 index / Hillshade index at 9am, summer solstice 
Hillshade_Noon / quantitative / 0 to 255 index / Hillshade index at noon, summer soltice 
Hillshade_3pm / quantitative / 0 to 255 index / Hillshade index at 3pm, summer solstice 
Horizontal_Distance_To_Fire_Points / quantitative / meters / Horz Dist to nearest wildfire ignition points 
Wilderness_Area (4 binary columns) / qualitative / 0 (absence) or 1 (presence) / Wilderness area designation 
Soil_Type (40 binary columns) / qualitative / 0 (absence) or 1 (presence) / Soil Type designation 
Cover_Type (7 types) / integer / 1 to 7 / Forest Cover Type designation


Relevant Papers:

Blackard, Jock A. and Denis J. Dean. 2000. "Comparative Accuracies of Artificial Neural Networks and Discriminant Analysis in Predicting Forest Cover Types from Cartographic Variables." Computers and Electronics in Agriculture 24(3):131-151. 
[Web Link] 

Blackard, Jock A. and Denis J. Dean. 1998. "Comparative Accuracies of Neural Networks and Discriminant Analysis in Predicting Forest Cover Types from Cartographic Variables." Second Southern Forestry GIS Conference. University of Georgia. Athens, GA. Pages 189-199. 

Blackard, Jock A. 1998. "Comparison of Neural Networks and Discriminant Analysis in Predicting Forest Cover Types." Ph.D. dissertation. Department of Forest Sciences. Colorado State University. Fort Collins, Colorado. 165 pages.
"""



