# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 23:08:20 2018

@author: bebi
"""

import numpy as np

import math

def removeIncomplete(id):
    MaximumId = math.floor(max(id))
    toDelete = []
    for i in range(1, MaximumId):
        n = 0
        for j in range(np.size(id)):
            if i == math.floor(id[j]):
                n = n + 1
        if n < 3:         
            for k in range(np.size(id)):
                 if i == math.floor(id[k]):
                     toDelete.append(id[k])
                     
    idList = id.tolist();
    difference = [item for item in idList if item not in toDelete]
                     
    return difference
            
#print(removeIncomplete(np.array([1.3, 2.2, 2.3, 4.2, 5.1, 3.2, 5.3, 3.3, 2.1, 1.1, 5.2, 3.1])))         
    