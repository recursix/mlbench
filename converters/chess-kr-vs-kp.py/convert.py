# -*- coding: utf-8 -*-
'''
Created on Nov 30, 2013

@author: jf
'''

import numpy as np
import os

data_file = "kr-vs-kp.data"

info = {
    "key": "chess-kr-vs-kp",
    "url": "http://archive.ics.uci.edu/ml/datasets/Chess+%28King-Rook+vs.+King-Pawn%29",
    "name": "Chess (King-Rook vs. King-Pawn)",
    "x_type": "reals",
    "y_type": "classification",
    "description": "Chess End-Game -- King+Rook versus King+Pawn on a7 (usually abbreviated KRKPA7). The pawn on a7 means it is one square away from queening. It is the King+Rook's side (white) to move.",
    "preprocessing": ["Original string features and classes have been converted to integers following this mapping: {'f': 0, 'l': 1, 'n': 2, 't': 3, 'w': 4, 'b': 5, 'g': 6, 'nowin': 0, 'won': 1}"],
}

def convert(raw_dir="raw"):
    data_string_array = np.loadtxt(os.path.join(raw_dir, data_file), delimiter=",", dtype=np.str)
    data_array = np.empty(data_string_array.shape, dtype=np.int)

    string_conversion_dict = {
        "f": 0,
        "l": 1,
        "n": 2,
        "t": 3,
        "w": 4,
        "b": 5,
        "g": 6,
        "nowin": 0,
        "won": 1,
    }

    for i, line in enumerate(data_string_array):
        line_ = line.copy()
        for key, value in string_conversion_dict.iteritems():
            line_[line == key] = value

        data_array[i] = line_.astype(np.int)

    x = data_array[:, :-1]
    y = data_array[:, -1]

    output_dict = info
    output_dict["x"] = x
    output_dict["y"] = y

    return output_dict