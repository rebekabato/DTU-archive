# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 21:05:22 2018

@author: bebi
"""
import math

def bacteriaGrowth(n0, alpha, K, N):
    NB = n0
    nt = 0
    if N < n0:
        nt
    
    while NB <= N:
        NB = (1.0 + alpha * (1.0 - (n0 / K))) * n0
        n0 = NB
        nt = nt + 1
    return nt

#print(bacteriaGrowth(100.0, 0.4, 1000.0, 500.0))