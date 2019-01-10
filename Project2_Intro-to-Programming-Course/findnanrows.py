# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 16:32:44 2018

@author: bebi
"""
import numpy as np
import pandas as pd


# findNanRows() useage: find the rows containing Nan in the data
# input: data loaded up by user
# output: vector of indices of rows containing Nan
# author: Bato
def findNanRows(grades):
    matrix = np.array(grades)
    NanRows = []
    i = 0
    
    for row in matrix:
        if np.isnan(row[2:].astype(float)).any() == True:
            NanRows.append(i)
        i += 1
    
    return NanRows
    
# createGoodMatrix() useage: build a matrix with only complete rows (no missing data) by excluding NanRows
# input: data loaded up by user and output of findNanRows()
# output: matrix with only complete rows (no missing data)
# Author: Bato
def createGoodMatrix(grades):
    NanRows = findNanRows(grades)
    matrix = np.array(grades)
    goodMatrix = []
    for i in range(len(matrix)):
        if not i in NanRows:
            goodMatrix.append(matrix[i])
            
    return np.array(goodMatrix)
            
                
    
# listErrorRowIDs() useage: list studentIDs where there are missing data
# input: data loaded up by user and output of findNanRows()
# output: vector of studentIDs
# Author: Bato
def listErrorRowIDs(grades):
    NanRows = findNanRows(grades)
    matrix = np.array(grades)
    errorRowIDs = []
    for i in range(len(matrix)):
        if i in NanRows:
            errorRowIDs.append(matrix[i][0])
            
    return np.array(errorRowIDs)

# print (findNanRows(grades))
# print (createGoodMatrix(grades))  
# print (listErrorRowIDs(grades))
