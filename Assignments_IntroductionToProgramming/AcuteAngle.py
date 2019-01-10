# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 14:58:53 2018

@author: bebi
"""

import math

import numpy as np

def acuteAngle(v1, v2):
    theta = math.acos(np.dot(v1, v2))
    if theta > math.pi / 2:
        return math.pi - theta
    else:
        return theta
        
# print(acuteAngle(np.array([-4.0/5.0, 3.0/5.0]), np.array([20.0/29.0, 21.0/29.0])))