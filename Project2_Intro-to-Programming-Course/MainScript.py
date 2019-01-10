
###################################################
### WELCOME TO PROJECT 2 - STUDENT GRATES       ###
###                                             ###
### We are happy to see you again! Make sure to ### 
### read all the program guidelines! <(^_^<)    ###
###                                             ###
###     CODE CONTRIBUTIONS:                     ###
###     MainScript.py MIKKEL                    ###
###     ErrorCheck.py MIKKEL & ZHAO             ###
###     Plotfunction.py MIKKEL & ZHAO           ###
###     Graderounding.py ZHAO                   ###
###     FindNanRows.py REBEKA                   ###
###     FinalGrade.py REBEKA                    ###
###     Menu4Table.py REBEKA                    ###
###     Menu4funct.py REBEKA                    ###
###                                             ###
###################################################

### IMPORT MODULES
import numpy as np
import pandas as pd
import os

### IMPORT EXTERNAL SCRIPTS
from Graderounding import roundGrade
from FinalGrade import computeFinalGrades
from ErrorCheck import ErrorCheck
from findnanrows import createGoodMatrix
from findnanrows import listErrorRowIDs
from Menu4Table import displayTable
from Menu4funct import menu4funct
from PlotFunction import gradesPlot

### WE SET UP VARIABLES USED TO KEEP TRACK OF THE INTERFACE INTERACTIONS
Menu = "0"
Loaded = "no"
dataStatus = "No data loaded."

### START THE PROGRAM
print("")
print("(^u^) PROJECT 2 (^u^)")
print(" --STUDENT GRADES--")
print("")
print("Make sure to follow the guide lines!")
input("Press ENTER to start!")
print("")
print("")


### INITIATION MAIN MENU
while Menu == "0":
    print("")
    print("------MENU------")
    print("1. Load New Data")
    print("2. Check for data errors")
    print("3. Generate Plots")
    print("4. Display list of grades")
    print("5. Preview Current Data")
    print("6. Guide lines")
    print("7. (^｡◕‿‿◕｡)^")
    print("8. Exit")
    print("")
    print("Status:",dataStatus)  
    Menu = input("Please Choose 1-8: ")       
    while Menu != "1" and Menu != "2" and Menu != "3" and Menu != "4" and Menu != "5" and Menu != "6" and Menu!= "7" and Menu!= "8":
        print(" ")
        print("Invalid! You must select 1-8")
        Menu = input("Please type a number to select: ")
 
    
### NAVIGATION TO LOADING NEW DATA    
    while Menu =="1":
        filename = input("Enter filename (only .csv): ")
        try:
            grades = pd.read_csv(filename, sep=',',header=0)
            print("")
            print("Well done!")
            input("Press ENTER to continue! ")
            dataStatus = "Data successfully loaded!"
            # 
            Loaded ="yes"
            Menu = "0"
        except:
            print("")
            print("Ohhh no :(! Something is wrong. Make sure: 1) The file is in same folder as script 2) Must end with .csv 3) Data entires follows the guidelines given in 'Menu 6'. Please try again.")
            input("Press ENTER to continue! ")
            Menu = "0"
   
    
### NAVIGATION TO PLOTTING OF THE DATA        
    while Menu == "2":
        if Loaded != "yes":
            print("")
            print("You did not load any data yet! Please load data.")
            input("Press ENTER to continue! ")
            Menu = "0"
        else:
            print(ErrorCheck(grades))
            input("Possible errors are displayed above this message. Press ENTER to continue! ")
            Menu = "0"


### NAVIGATION TO PLOT THE DATA              
    while Menu == "3":
        if Loaded != "yes":
            print("")
            print("You did not load any data yet! Please load data.")
            input("Press ENTER to continue")
            Menu = "0"

        elif Loaded == "yes":
            print(gradesPlot(grades, filename))
            input("Enjoy these beautiful graphs! Press ENTER to continue! ")
            Menu = "0"
            
            
### NAVIGATION TO DISPLAY THE LIST OF GRADES          
    while Menu =="4":
        if Loaded != "yes":
            print("")
            print("You did not load any data yet! Please load data.")
            input("Press ENTER to continue!")
            Menu = "0"
        
        elif Loaded == "yes":
            print(menu4funct(grades,filename))
            Menu = "0"
            
            
### DISPLAYING A PREVIEW OF THE LOADED DATA 
    while Menu =="5":
        if Loaded != "yes":
            print("")
            print("You did not load any data yet! Please load data.")
            input("Press ENTER to continue")
            Menu = "0"   
        else:
            print(grades)
            input("Press ENTER to continue!")
            Menu ="0"


### SHOWING THE GUIDELINES           
    while Menu == "6":
        print("")
        print("GUIDELINES: Your input MUST follow the structure of the attached testfile 'testGrades.csv'. Your file must be in a .csv (UTF-8 encoding) format and located in the directory of this script.")
        print("")
        print("MENU OPTION 1: This option lets you load any new .csv file into this program. Your file MUST follow the format described above.")
        print("")
        print("MENU OPTION 2: This option will search your original loaded data for dublicate student IDs & will list any grade entires that is not one of the whole numbers found on the danish 7-grade-scale.")
        print("")
        print("MENU OPTION 3: This option make a bar-plot of the distribution of the final grades (note: We include only students with entires for all assignments. Run Menu option 4 to list the disregarded entires.")
        print("")
        print("MENU OPTION 4: This option will round the grades found in your data set and display them along with the final grade. Note: We include only students with entires for ALL assignments.")
        print("")
        print("MENU OPTION 5: This option gives you a preview of the raw data file that you have loaded into the program. Including students with NaN entires.")
        print("")
        print("MENU OPTION 6: This option makes these guide lines appear.")
        print("")
        print("MENU OPTION 7: (づ｡◕‿‿◕｡)づ Try and see!")
        print("")
        print("MENU OPTION 8: This option will exit the program")
        print("")
        print("Thanks for reading the guidelines!")
        input("Press ENTER to continue! ")
        Menu = "0"
    
    
### EXITING THE PROGRAM
    if Menu == "8":
        try:
            os.remove("gradesrounded.csv")
            exit(0)
        except:
            exit(0)
    
    
### CHRISTMAS SURPRISE <(^_^<)
    if Menu == "7":    
        print("     ")
        print("     ")
        print("     ")
        print("     ")
        print("     ")
        print("     ")
        print("     ")
        print("     ")
        print("     ")
        print("     ")
        print("     ")
        print("     ")
        print("     ")
        print("     ")
        print("     *     ")
        print("    ***    ")
        print("   *o*o*   ")
        print("  ***V***  ")
        print(" ********* ")
        print("   L   L ")
        input("Merry Christmas from Rebeka, Mikkel & Zhao!")
        print("     ")
        print("     *     ")
        print("    ***    ")
        print("   *X*X*   ")
        print("  ***_***  ")
        print(" ********* ")
        print("   L   L ")
        input("Are you trying to leave? Please stay!")
        print("     ")
        print("     *     ")
        print("    ***    ")
        print("\__*ʘ*ʘ*__/  ")
        print("  ***∩***  ")
        print(" ********* ")
        print("   L   L ")
        input("Really?")
        Menu = "0"
        


        

