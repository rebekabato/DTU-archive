# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 17:49:55 2018

@author: bebi
"""

import numpy as np

def fermentationRate(measuredRate, lowerBound, upperBound):
    measuredRateSum = 0
    n = 0
    for i in range(np.size(measuredRate)):
        if measuredRate[i] > lowerBound and measuredRate[i] < upperBound:
            measuredRateSum = measuredRateSum + measuredRate[i] # measuredRateSum += measureRate[i]
            n = n + 1
    averageRate = measuredRateSum / n
    return averageRate
            
#print (fermentationRate(np.array([20.1, 19.3, 1.1, 18.2, 19.7, 121.1, 20.3, 20.0]), 15, 25))
            
def fermentationRate(measuredRate, lowerBound, upperBound):
# Returns average of elements of vector measuredRate greater than
# lowerBound and less than upperBound
    goodRates = (measuredRate > lowerBound) & (measuredRate < upperBound)
    averageRate = np.mean(measuredRate[goodRates])
    return averageRate