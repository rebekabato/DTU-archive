import math
import numpy as np
import pandas as pd


def roundGrade(gradesRounded):
    res=[]
    original = gradesRounded
    grades = np.array(gradesRounded)
    MatrixSize  = np.size(grades)
    nRows  = len(gradesRounded.StudentID)
    GradeMatrixSize  = int((MatrixSize - 2 * nRows) / nRows)
    grades = grades[:,2:MatrixSize]
    grades = np.reshape(grades,-1)    
    for i, n in enumerate(grades):
        if n >= 10:
            if abs(12 - n) <= abs(n - 10):
                n = 12
            else:
                n = 10
        if (n >= 7) and (n < 10):
            if abs(10 - n) <= abs(n - 7):
                n = 10
            else:
                n = 7
        if (n >= 4) and (n < 7):
            if abs(7 - n) <= abs(n - 4):
                n = 7
            else:
                n = 4
        if (n >= 2) and (n < 4):
            if abs(4 - n) <= abs(n - 2):
                n = 4
            else:
                n = 2
        if (n >= 0) and (n < 2):
            if abs(2 - n) <= abs(n - 0):
                n = 2
            else:
                n = 0
        if (n >= -3) and (n < 0):
            if abs(0 - n) <= abs(n + 3):
                n = 0
            else:
                n = -3
        if (n < -3):
            n = -3
        res.append(n)
    gradesRounded = res
    gradesRounded = np.reshape(gradesRounded,(nRows,GradeMatrixSize))
    Id = original.iloc[:,0:2]
    Id = np.array(Id)
    Id = np.reshape(Id,(nRows,2))
    #Header = original.iloc[]
    gradesRounded = np.hstack((Id,gradesRounded))
    
    np.savetxt("gradesrounded.csv", gradesRounded, fmt='%5s',delimiter=",",comments="")
    return gradesRounded
    
# print (roundGrade(gradesRounded))