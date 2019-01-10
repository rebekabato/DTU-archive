#### BY MIKKEL & ZHAO

import numpy as np
import csv
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.pyplot import figure
from pandas import Series
import warnings
import matplotlib.cbook
from FinalGrade import computeFinalGrades 
from Graderounding import roundGrade
from ErrorCheck import ErrorCheck
from findnanrows import createGoodMatrix
from findnanrows import listErrorRowIDs
from Menu4Table import displayTable

warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)


def gradesPlot(grades, filename):
    #Import rounded grades
    roundedGrades = roundGrade(grades)
    # create a matrix containing only that rows where there is no missing data
    goodMatrix = createGoodMatrix(roundedGrades)
    # count the final grades for goodMatrix
    finalGrades = computeFinalGrades(goodMatrix)
    # add final grade array as a last column to goodMatrix, reset data to alphabetical order
    forTable = np.c_[goodMatrix, finalGrades]
    # create data frame with the grades and final grades
    finalgradesmatrix = displayTable(forTable, filename)
        
    #EXTRACT THE "FINAL GRADE COLUMN" from .CSV AND CONVERT TO NP.ARRAY
    finalgrades = np.array(list(map(int, finalgradesmatrix.iloc[1:,-1].tolist())))

    #ASSIGN COLUMN NAMES AND COUNT NUMBER OF GRADES
    gradesnames = ("12", "10", "7", "4","2","0","-3")   
    FinalCount = np.empty(7)
    FinalCount[0]  = np.count_nonzero(finalgrades == 12)
    FinalCount[1]  = np.count_nonzero(finalgrades == 10)
    FinalCount[2]  = np.count_nonzero(finalgrades == 7)
    FinalCount[3]  = np.count_nonzero(finalgrades == 4)
    FinalCount[4]  = np.count_nonzero(finalgrades == 2)
    FinalCount[5]  = np.count_nonzero(finalgrades == 0)
    FinalCount[6]  = np.count_nonzero(finalgrades == -3)

    # CHANGING SIZE OF FIGURE
    figure(num=None, figsize=(7, 6), dpi=100, facecolor='w', edgecolor='k')
    plt.bar(gradesnames, FinalCount)
    
    #MAKE STEP SIZE FOR Y-AXIS AT 1.09
    plt.yticks(np.arange(min(FinalCount),max(FinalCount)+1,1.0))  
    
    plt.xlabel('Grade')
    plt.ylabel('Number of Students')
    plt.title('Final grades distribution')
    plt.show()
    
    
    csvfile = csv.reader(open('gradesrounded.csv', encoding='utf-8'))  
    assignnum = pd.read_csv("gradesrounded.csv", sep=',')
    assignnum = len(assignnum.iloc[1,:])                                #to get the amount of assignments 
    y_pos1 = np.arange(assignnum-2)+1                                   #the xticks for the second graph
    list_x = []
    list_y = []

    for i in csvfile:
        #enmerate each row, only the data
        for k in range(2, assignnum):            
            if i[k] == 'nan':
                list_y.append(0)
            else:
                list_y.append(float(i[k]))
    
            t = np.random.uniform(-0.1, 0.1)
            list_x.append(k - 1 + t)   
            
    #COSTUMIZING FIGURE AND (SCATTER) PLOTTING GRADES
    figure(num=None, figsize=(7, 6), dpi=100, facecolor='w', edgecolor='k')
  
    # COMPUTING MEAN ASSIGNMENT GRADE
    avg = pd.read_csv("gradesrounded.csv", sep=',', header=None)
    new = np.array(avg.iloc[0:,2:], dtype=float)
    new = pd.DataFrame(new)
    avgVal = pd.DataFrame.mean(new)
    avgVal.index = avgVal.index + 1
    
    # CREATING THE PLOT
    colors = np.random.rand(len(list_x))                                     
    plt.scatter(list_x, list_y,c=colors, alpha=1)
    plt.xticks(y_pos1)
    plt.yticks([12, 10, 7, 4,2,0,-3])
    plt.ylim(ymin=-5)
    plt.ylim(ymax=13)
    plt.xlabel('Assignment')
    plt.ylabel('Grades')
    plt.title('Grade performance per assignment')
    plt.plot(avgVal, marker="_",linestyle='None', markersize=50, color='r',markeredgewidth=2.5)
    plt.legend(['AVERAGE'],markerscale=0.4)
    plt.show()
    return #""
    
# print (gradesPlot(grades, filename))
