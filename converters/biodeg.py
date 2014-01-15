# -*- coding: utf-8 -*-
'''
Created on Nov 30, 2013

@author: pascal, alexandre
'''

from mlbench import util

info = {
    "url" : "http://archive.ics.uci.edu/ml/datasets/Annealing", # url of a web page for the dataset
    "name": "QSAR biodegradation Data Set", # full name of the dataset
    "key":"biodeg", # short name of the dataset, complying with mudule naming in python (the name of the current module should be <key>.py)
    "y_type":"enum", # the type of the y space. (will be enum for now) 
    "x_type": None, # If None, it will be inferred from the content of the column
    "preprocessing": "", # breifly describes how the original dataset was transformed 
}

src_url = "http://archive.ics.uci.edu/ml/machine-learning-databases/00254/" 
file_name = "biodeg.csv"
def fetch(raw_dir): # takes care of fetching all required files into raw_dir
    util.fetch(raw_dir, src_url, file_name)
    

def convert(raw_dir, max_features):
    """
    returns a dictionary containing the required fields for the dataset.
    """
    return util.convert_uci_classif_( info, raw_dir, file_name, delimiter=';' ) 



info["description"]= """
Source:

Kamel Mansouri, Tine Ringsted, Davide Ballabio (davide.ballabio '@' unimib.it), Roberto Todeschini, Viviana Consonni, Milano Chemometrics and QSAR Research Group (http://michem.disat.unimib.it/chm/), UniversitÃ  degli Studi Milano â€“ Bicocca, Milano (Italy)


Data Set Information:

The QSAR biodegradation dataset was built in the Milano Chemometrics and QSAR Research Group (UniversitÃ  degli Studi Milano â€“ Bicocca, Milano, Italy). The research leading to these results has received funding from the European Communityâ€™s Seventh Framework Programme [FP7/2007-2013] under Grant Agreement n. 238701 of Marie Curie ITN Environmental Chemoinformatics (ECO) project. 
The data have been used to develop QSAR (Quantitative Structure Activity Relationships) models for the study of the relationships between chemical structure and biodegradation of molecules. Biodegradation experimental values of 1055 chemicals were collected from the webpage of the National Institute of Technology and Evaluation of Japan (NITE). Classification models were developed in order to discriminate ready (356) and not ready (699) biodegradable molecules by means of three different modelling methods: k Nearest Neighbours, Partial Least Squares Discriminant Analysis and Support Vector Machines. Details on attributes (molecular descriptors) selected in each model can be found in the quoted reference: Mansouri, K., Ringsted, T., Ballabio, D., Todeschini, R., Consonni, V. (2013). Quantitative Structure - Activity Relationship models for ready biodegradability of chemicals. Journal of Chemical Information and Modeling, 53, 867-878.


Attribute Information:

41 molecular descriptors and 1 experimental class: 
1) SpMax_L: Leading eigenvalue from Laplace matrix 
2) J_Dz(e): Balaban-like index from Barysz matrix weighted by Sanderson electronegativity 
3) nHM: Number of heavy atoms 
4) F01[N-N]: Frequency of N-N at topological distance 1 
5) F04[C-N]: Frequency of C-N at topological distance 4 
6) NssssC: Number of atoms of type ssssC 
7) nCb-: Number of substituted benzene C(sp2) 
8) C%: Percentage of C atoms 
9) nCp: Number of terminal primary C(sp3) 
10) nO: Number of oxygen atoms 
11) F03[C-N]: Frequency of C-N at topological distance 3 
12) SdssC: Sum of dssC E-states 
13) HyWi_B(m): Hyper-Wiener-like index (log function) from Burden matrix weighted by mass 
14) LOC: Lopping centric index 
15) SM6_L: Spectral moment of order 6 from Laplace matrix 
16) F03[C-O]: Frequency of C - O at topological distance 3 
17) Me: Mean atomic Sanderson electronegativity (scaled on Carbon atom) 
18) Mi: Mean first ionization potential (scaled on Carbon atom) 
19) nN-N: Number of N hydrazines 
20) nArNO2: Number of nitro groups (aromatic) 
21) nCRX3: Number of CRX3 
22) SpPosA_B(p): Normalized spectral positive sum from Burden matrix weighted by polarizability 
23) nCIR: Number of circuits 
24) B01[C-Br]: Presence/absence of C - Br at topological distance 1 
25) B03[C-Cl]: Presence/absence of C - Cl at topological distance 3 
26) N-073: Ar2NH / Ar3N / Ar2N-Al / R..N..R 
27) SpMax_A: Leading eigenvalue from adjacency matrix (Lovasz-Pelikan index) 
28) Psi_i_1d: Intrinsic state pseudoconnectivity index - type 1d 
29) B04[C-Br]: Presence/absence of C - Br at topological distance 4 
30) SdO: Sum of dO E-states 
31) TI2_L: Second Mohar index from Laplace matrix 
32) nCrt: Number of ring tertiary C(sp3) 
33) C-026: R--CX--R 
34) F02[C-N]: Frequency of C - N at topological distance 2 
35) nHDon: Number of donor atoms for H-bonds (N and O) 
36) SpMax_B(m): Leading eigenvalue from Burden matrix weighted by mass 
37) Psi_i_A: Intrinsic state pseudoconnectivity index - type S average 
38) nN: Number of Nitrogen atoms 
39) SM6_B(m): Spectral moment of order 6 from Burden matrix weighted by mass 
40) nArCOOR: Number of esters (aromatic) 
41) nX: Number of halogen atoms 
42) experimental class: ready biodegradable (RB) and not ready biodegradable (NRB)
"""