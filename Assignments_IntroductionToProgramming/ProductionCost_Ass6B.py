# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 14:23:57 2018

@author: bebi
"""

import numpy as np


def computeItemCost(resourceItemMatrix, resourceCost):
    itemCost = np.array([])
    for i in range(len(resourceItemMatrix[0,:])):
        a = np.dot(resourceItemMatrix[:, i], resourceCost)
        itemCost = np.append(itemCost, a)
        
    return itemCost
    
#print(computeItemCost(np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]]), np.array([101.25,84.00,75.50])))