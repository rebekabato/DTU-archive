import numpy as np


# computeFinalGrades() useage: calculate the final grades for all students
# input: N (students) x M (assignments) matrix containing ID, student names, grades on 7-step-scale
# output: vector containing the means of the assignments for all students
# Author: Bato
def computeFinalGrades(grades):
    matrix = np.array(grades)[:,2:].astype(float)
    gradesFinal = np.array([])
    res = []

    # if there is only one assignment, copy the column
    if np.size(matrix, 1) == 1:
        gradesFinal = np.reshape(np.repeat(matrix, 1, axis=1), -1)

    # if there are more than 1 assignment
    elif np.size(matrix, 1) > 1:
        for row in matrix:
            if -3 in row:
                gradesFinal = np.append([gradesFinal], [-3])
                        
            # other rows
            else:
                # sort elements of a row in ascending order, cut down the lowest and take the mean for the rest
                gradesFinal = np.append([gradesFinal], [np.mean(np.delete(sorted(row), [0]))])

    for elem in gradesFinal:
        if elem >= 10:
            if abs(12 - elem) <= abs(elem - 10):
                elem = 12
            else:
                elem = 10
        if (elem >= 7) and (elem < 10):
            if abs(10 - elem) <= abs(elem - 7):
                elem = 10
            else:
                elem = 7
        if (elem >= 4) and (elem < 7):
            if abs(7 - elem) <= abs(elem - 4):
                elem = 7
            else:
                elem = 4
        if (elem >= 2) and (elem < 4):
            if abs(4 - elem) <= abs(elem - 2):
                elem = 4
            else:
                elem = 2
        if (elem >= 0) and (elem < 2):
            if abs(2 - elem) <= abs(elem - 0):
                elem = 2
            else:
                elem = 0
        if (elem >= -3) and (elem < 0):
            if abs(0 - elem) <= abs(elem + 3):
                elem = 0
            else:
                elem = -3
        if (elem < -3):
            elem = -3
        
        res.append(elem)
            
    gradesFinal = res
                
    return gradesFinal

#print (computeFinalGrades(grades))