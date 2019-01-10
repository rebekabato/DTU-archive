import math
import numpy as np
import pandas as pd
import csv
import itertools

def dataLoad(filename):
    
    # LOAD FILE TO NUMPY MATRIX
    matrix = np.loadtxt(filename, usecols=range(3))
    print("")
    # PRINT ERROR MESSAGES & LABEL INVALID ENTIRES
    for i in range(0,len(matrix)):
        if matrix[i,0] < 10:
            print("Invalid low temperature in row:",i+1)
            matrix[i,0] = np.nan    
        elif matrix[i,0] > 60:
            print("Invalid high temperature in row:",i+1)
            matrix[i,0] = np.nan  
        if matrix[i,1] < 0:
            print("Invalid negativ growth rate in row:",i+1)
            matrix[i,1] = np.nan
        if matrix[i,2] != 1 and matrix[i,2] != 2 and matrix[i,2] !=3 and matrix[i,2] !=4:
            matrix[i,2] = np.nan
            print("Invalid unknown bacteria in row:",i+1)
            
    # REMOVE THE NANS      
    matrix=matrix[~np.isnan(matrix).any(axis=1)]
    np.savetxt("matrix.csv", matrix, delimiter=",",header= "Temp,Growth,Strain",comments="")
    np.savetxt("clean.txt", matrix, delimiter=",")