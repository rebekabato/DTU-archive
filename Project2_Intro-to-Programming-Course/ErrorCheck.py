#### BY MIKKEL & ZHAO

import numpy as np
import pandas as pd

def ErrorCheck(grades):
    print("CHECKING FOR ERRORS:")
    print("")
    stuID = np.array(grades.StudentID)
    studentnum = len(grades.StudentID) - 1
    for i in range(len(grades.StudentID) - 1):
        t = i + 1
        if stuID[i] == stuID[t]:         
            t = t + 1
            print("Dublicate student numbers conflict for:")
            print(grades.iloc[i,0])
            print("")

### HERE WE CHECK FOR ANY INVALID GRADES ENTRIES, THSES ARE GRADES NOT FOUND ON THE 7-SCALE    
    NP_grades = np.array(grades.iloc[0:,2:]) 
    for i in range(len(NP_grades)):
        for o in range(np.size(NP_grades,1)):
            if NP_grades[i,o] != float(-3) and NP_grades[i,o] != float(0) and NP_grades[i,o] != float(2) and NP_grades[i,o] != float(4) and NP_grades[i,o] != float(7) and NP_grades[i,o] != float(10) and NP_grades[i,o] != float(12):
                print("Invalid grade:",NP_grades[i,o],"for",grades.iloc[i,1])
    this = ("")
    return this
        
    
 