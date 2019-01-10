# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 17:48:04 2018

@author: bebi
"""

import numpy as np

def movingAvg(y):
    minusTwo = np.pad(y, (0, 2), 'constant', constant_values=(0, 0))[2:]
    minusOne = np.pad(y, (0, 1), 'constant', constant_values=(0, 0))[1:]
    Zero = y
    plusOne = np.pad(y, (1, 0), 'constant', constant_values=(0, 0))[0:len(y)]
    plusTwo = np.pad(y, (2, 0), 'constant', constant_values=(0, 0))[0:len(y)]
    
    Matrix = np.vstack((minusTwo, minusOne*2, Zero*3, plusOne*2, plusTwo))
    
    return np.array([np.sum(Matrix, axis=0)])/9
    
    
#print(movingAvg(np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7])))
