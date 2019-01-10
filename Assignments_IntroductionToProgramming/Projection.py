# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 21:34:33 2018

@author: bebi
"""

import numpy as np

import math

def computeProjection(a):
    b = np.ones(np.size(a))
    p = (np.dot(a, b) / np.dot(a, a)) * a
    return p
