import numpy as np
from Graderounding import roundGrade
from FinalGrade import computeFinalGrades
from findnanrows import createGoodMatrix
from findnanrows import listErrorRowIDs
from Menu4Table import displayTable


def menu4funct(grades,filename):   
    input("You are about to display the list of rounded & final grades. Note: Students with ANY missing entries in an assignment will be discarded from this list. You can still view the original data by using menu 5. Press ENTER to continue.")
    # take the raw data and round the numbers to grades on 7-step scale
    roundedGrades = roundGrade(grades)
    # create a matrix containing only that rows where there is no missing data
    goodMatrix = createGoodMatrix(roundedGrades)
    # count the final grades for goodMatrix
    finalGrades = computeFinalGrades(goodMatrix)
    
    # add final grade array as a last column to goodMatrix, reset data to alphabetical order
    forTable = np.c_[goodMatrix, finalGrades]
    forTable = forTable[forTable[:, 1].argsort()]
                
    # display the grades and final grades for the user
    displayData = displayTable(forTable, filename)
    #print ()
    print(displayData.to_string())
                
    # save data to the user's computer
    np.savetxt("FinalGrades_Table.csv", displayData, fmt='%5s', delimiter=",", comments="")
    print(" ")
    print("Enjoy this overview of grades!")
    print(" ")
    print("Also a file named 'FinalGrades_Table.csv' has been generated in your working directory for your pleasure! Please check it out! Note: Any students listed after this message might have been disregarded from the list due to a NaN entry in their assignment(s):")
    print(" ")
    # provide the IDs for disregarded students
    ID = listErrorRowIDs(grades)
    for elem in ID:
        print (elem)
            
    input("Press ENTER to continue")

#print (menu4funct(grades,filename))