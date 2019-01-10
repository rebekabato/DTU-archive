# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 14:31:05 2018

@author: bebi
"""

import numpy as np

import math

def singleBoxArea(xa, xb, ya, yb):
    return (xb - xa) * (yb - ya)

def intersectionArea(xa, xb, xc, xd, ya, yb, yc, yd):
    return max(0, min(xb, xd) - max(xa, xc)) * max(0, min(yb, yd) - max(ya, yc))

def boxArea(boxCorners, area):
    x1 = boxCorners[0]
    x2 = boxCorners[1]
    x3 = boxCorners[2]
    x4 = boxCorners[3]
    y1 = boxCorners[4]
    y2 = boxCorners[5]
    y3 = boxCorners[6]
    y4 = boxCorners[7]
    if area == "Box1":
        A = singleBoxArea(x1, x2, y1, y2)
    elif area == "Box2":
        A = singleBoxArea(x3, x4, y3, y4)
    elif area == "Intersection":
        A = intersectionArea(x1, x2, x3, x4, y1, y2, y3, y4)
    elif area == "Union":
        A = singleBoxArea(x1, x2, y1, y2) + singleBoxArea(x3, x4, y3, y4) - intersectionArea(x1, x2, x3, x4, y1, y2, y3, y4)
    return A
    
 # print (boxArea(np.array([5, 20, 14, 25, 12, 23, 5, 17]), "Intersection"))
    