# -*- coding: utf-8 -*-
'''
Created on Jan 15, 2014

@author: JF
'''



#from graalUtil.num import uHist
from mlbench import util
import os

info = {
    "url" : "http://archive.ics.uci.edu/ml/datasets/PAMAP2+Physical+Activity+Monitoring",
    "name": "PAMAP2 Physical Activity Monitoring",
    "key": "pamap2",
    "y_type": "enum",  # the type of the y space. (will be enum for now)
    "x_type": ('float',)*40,  # If None, it will be inferred from the content of the column
    "preprocessing": 'Timestamp and "invalid" (according to the authors) features are removed. Only "Protocol" data files are used: "Optional" ones only contain "other" class.',  # briefly describes how the original dataset was transformed
}

src_url = "http://archive.ics.uci.edu/ml/machine-learning-databases/00231"
file_name = "PAMAP2_Dataset.zip"

def fetch(raw_dir): # takes care of fetching all required files into raw_dir
    util.fetch(raw_dir, src_url, file_name)
    

def convert(raw_dir, max_features):
    util.unzip(raw_dir, file_name)
    data_dir = os.path.join(os.path.join(raw_dir, "PAMAP2_Dataset"), "Protocol")

    file_name_list = ["subject10%d.dat" % x for x in range(1, 10)]

    # We remove features 0 (timestamp), 16-19, 33-36 and 50-53 (invalid).
    columns = range(1, 16) + range(20, 33) + range(37, 50)
    return util.convert_uci_classif(info, data_dir, file_name_list, stride=4, delimiter=" ", y_first=True, usecols=columns)


info["description"] = """
Source:

Attila Reiss, Department Augmented Vision, DFKI, Germany, attila.reiss '@' dfki.de
Date: August 2012.


Data Set Information:

The PAMAP2 Physical Activity Monitoring dataset contains data of 18 different physical activities (such as walking, cycling, playing soccer, etc.), performed by 9 subjects wearing 3 inertial measurement units and a heart rate monitor. The dataset can be used for activity recognition and intensity estimation, while developing and applying algorithms of data processing, segmentation, feature extraction and classification.

** Sensors **
3 Colibri wireless inertial measurement units (IMU):
- sampling frequency: 100Hz
- position of the sensors:
- 1 IMU over the wrist on the dominant arm
- 1 IMU on the chest
- 1 IMU on the dominant side's ankle
HR-monitor:
- sampling frequency: ~9Hz

** Data collection protocol **
Each of the subjects had to follow a protocol, containing 12 different activities. The folder â€œProtocolâ€ contains these recordings by subject.
Furthermore, some of the subjects also performed a few optional activities. The folder â€œOptionalâ€ contains these recordings by subject.

** Data files **
Raw sensory data can be found in space-separated text-files (.dat), 1 data file per subject per session (protocol or optional). Missing values are indicated with NaN. One line in the data files correspond to one timestamped and labeled instance of sensory data. The data files contain 54 columns: each line consists of a timestamp, an activity label (the ground truth) and 52 attributes of raw sensory data.


Attribute Information:

The 54 columns in the data files are organized as follows:
1.	 timestamp (s)
2.	 activityID (see below for the mapping to the activities)
3.	 heart rate (bpm)
4-20.	 IMU hand
21-37.	IMU chest
38-54.	IMU ankle

The IMU sensory data contains the following columns:
1.	 temperature (Â°C)
2-4.	 3D-acceleration data (ms-2), scale: Â±16g, resolution: 13-bit
5-7.	 3D-acceleration data (ms-2), scale: Â±6g, resolution: 13-bit
8-10.	 3D-gyroscope data (rad/s)
11-13.	3D-magnetometer data (Î¼T)
14-17.	orientation (invalid in this data collection)

List of activityIDs and corresponding activities:
1	lying
2	sitting
3	standing
4	walking
5	running
6	cycling
7	Nordic walking
9	watching TV
10	computer work
11	car driving
12	ascending stairs
13	descending stairs
16	vacuum cleaning
17	ironing
18	folding laundry
19	house cleaning
20	playing soccer
24	rope jumping
0	other (transient activities)


Relevant Papers:

The following two publications describe the dataset and provide a baseline benchmark on various tasks of physical activity recognition and intensity estimation:

[1] A. Reiss and D. Stricker. Introducing a New Benchmarked Dataset for Activity Monitoring. The 16th IEEE International Symposium on Wearable Computers (ISWC), 2012.
[2] A. Reiss and D. Stricker. Creating and Benchmarking a New Dataset for Physical Activity Monitoring. The 5th Workshop on Affect and Behaviour Related Assistance (ABRA), 2012.

Further information (detailed description of the protocol and the various activities, statistics of the dataset, the subjects, etc.) can be found in the documentation attached to the dataset. Please refer to the file readme.pdf.



Citation Request:

This dataset is freely available for academic research, there are no (legal or other) constraints on using the data for scientific purposes. We would appreciate referencing one of the below publications ([1] or [2]) if you use this dataset.
If you have any questions or suggestions, please contact Attila Reiss ([firstname].[lastname]@dfki.de). Also, please let us know if you have any publications that uses this dataset.
We recommend to refer to this dataset as the â€œPAMAP2 Datasetâ€ or the â€œPAMAP2 Physical Activity Monitoring Datasetâ€.

[1] A. Reiss and D. Stricker. Introducing a New Benchmarked Dataset for Activity Monitoring. The 16th IEEE International Symposium on Wearable Computers (ISWC), 2012.
[2] A. Reiss and D. Stricker. Creating and Benchmarking a New Dataset for Physical Activity Monitoring. The 5th Workshop on Affect and Behaviour Related Assistance (ABRA), 2012.
"""
