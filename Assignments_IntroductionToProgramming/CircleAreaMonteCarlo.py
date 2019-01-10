#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 00:07:03 2018

@author: rebeka
"""

import numpy as np

import math

def circleAreaMC(xvals, yvals):
    NgoodPoints = 0
    for i in range(np.size(xvals)):
        point = np.array([xvals[i], yvals[i]])
        if np.linalg.norm(point) < 1:
            NgoodPoints = NgoodPoints + 1
            
    return 4 * ( NgoodPoints / np.size(xvals))
    
#print(circleAreaMC(np.array([-0.1, 0.7, 0.8, 0.5, -0.4]), np.array([0.3, -0.1, 0.9, 0.6, -0.3])))