# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 08:17:58 2018

@author: bebi
"""
import pandas as pd
import numpy as np

# displayTable useage: give header for the matrix for displaying
# input: matrix containing IDs, student names, rounded grades, final grades (forTable), raw data uploaded by user (filename)
# output: matrix with final grades in the last column and header
# Author: Bato
def displayTable(forTable, filename):
    keepHeader = pd.read_csv(filename, header=None)
    headerFromRawData = np.array(keepHeader)[0,0:]
    newHeader = np.append(headerFromRawData, "Final Grades")
    matrix = np.vstack((newHeader, forTable))
    
     
    return pd.DataFrame(matrix)
    
# print (displayTable(forTable, filename))