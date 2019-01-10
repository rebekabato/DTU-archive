# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 17:57:16 2018

@author: bebi
"""

def evaluateTaylor(x):
    y = (x - 1) - (1/2) * (x - 1) ** 2 + (1/3) * (x - 1) ** 3
    return y