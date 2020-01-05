# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 17:28:24 2020

@author: Admin
"""

import pandas as pd
import numpy as np

train_set = pd.read_csv("database.csv")
test_set = pd.read_csv("test_cases.csv")

test_set = np.array(test_set)

str = test_set[4, 5]
print(str)

i = 0
# creating and passsing series to new column 
for col in train_set["Services"]:
    if col==str:
        index = i
        timeline_arr = np.array(train_set["Timeline months"])
        pred_timeline = timeline_arr[i]
        print(pred_timeline)
        break
    i += 1
    

