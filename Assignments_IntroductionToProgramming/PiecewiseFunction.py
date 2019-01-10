# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 15:54:17 2018

@author: bebi
"""

import numpy as np

import math

G = 9.82
R = 6.371 * 10 ** 6

def gravitationalPull(x):
    
    if x >= R:
        g = G * R ** 2 / x ** 2
   
    if x < R:
        g = G * x / R
    return g
    
print(gravitationalPull(np.arange([0, 10e6, 1e4])))
