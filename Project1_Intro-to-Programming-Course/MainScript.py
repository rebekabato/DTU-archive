###############################################################
### Welcome to PROJECT 1. This program will help you        ###
### filter, plot and perform basic statistics on bacterial  ###
### data. Your input MUST be in the form of a .txt file     ###
### with columns in the order: temperature, growth rate     ###
### and bacterial strain with row entries similar to the    ###
### data test set. After loading the data will be cleaned   ###
### meaning invalid rows removed according to the described ###
### assignment parameters for valid data. Enjoy!            ###
###############################################################
### BY MIKKEL, ZHAO & REBEKA

### WE IMPORT THE NECESSARY MODULES AND NECESSARY SCRIPTS
import numpy as np
import pandas as pd
from DataStatistics import *
from LoadAndErrorRemove import *
from DataPlot import *
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import os

### WE SET UP VARIABLES USED TO KEEP TRACK OF THE INTERFACE INTERACTIONS
Menu = "0"
Loaded = "no"
dataStatus = "Ready to load data."
BacFilterStatus = "No Bacteria filter."
GroFilterStatus = "No Growth filter."
BactSelectionlast = "0"
low = float(0)
high = float(1)
lowerboundry = float(-2)
upperboundry = float(2)
StrainSelected = "no"

### START OF PROGRAM
print("")
print("(>^_^)>  WELCOME TO PROJECT 1  <(^_^<)")
input("Press ENTER to start")


### INITIATION OF MENU
while Menu == "0":
    print("")
    print("------MENU------")
    print("1. Load / Overwrite data")
    print("2. Filter options")
    print("3. Display statistics")
    print("4. Generate plots")
    print("5. Show current data")
    print("6. Guide lines")
    print("7. Exit") 
    print("")
    if BacFilterStatus == "No Bacteria filter." and GroFilterStatus == "No Growth filter.":
        print("Status:",dataStatus)
        print("Filter: No filters applied.")
    else:
        print("Status:",dataStatus)
        print("Filters:",BacFilterStatus,GroFilterStatus)
    Menu = input("Please Choose 1-7: ")
    while Menu != "1" and Menu != "2" and Menu != "3" and Menu != "4" and Menu != "5" and Menu != "6" and Menu != "7":
        print(" ")
        print("Invalid! You must select 1-7")
        Menu = input("Please type a number to select: ")
    
### HERE WE NAVIGATE LOADING OF THE DATA
        
    while Menu == "1":
        fileMenu = input("Enter filename (only .txt): ")
        try:
            print(dataLoad(fileMenu))
            matrix = pd.read_csv('matrix.csv', sep=',')
            originalmatrix = matrix
            pdMatrix = matrix
            print("")
            print("Well done! Invalid rows may be listed above this message and will have removed from your data.")
            input("Press ENTER to continue with the cleaned up data.")
            dataStatus = "Data succesfully loaded!"
            Menu = "0"
            Loaded = "yes"                        
        except:
            print("")
            print("Ohhh no :(! Something is wrong. Make sure: 1) The file is in same folder as script 2) Must end with .txt. 3) Data entires follows the guidelines given in description in the guide lines. Please try again.")
            input("Press ENTER to continue")
            Menu = "0"

### HERE WE NAVIGATE FILTERING OF THE DATA

    while Menu == "2":
        if Loaded != "yes":
            dataStatus = "Unable to add filters, you did not load data yet."
            Menu = "0"
        elif Loaded == "yes":
            print("")
            print("")
            print("CHOOSE FILTER TO APPLY:")
            print("1. Bacterial Strain filter")
            print("2. Growth Rate filter")
            print("3. Disable Filters")
            print("4. Back to Menu")
            print("")
            print("Current filter(s):",BacFilterStatus,GroFilterStatus)
            FilterSelection = input("Please choose 1-4: ")
            if (FilterSelection != "1") and (FilterSelection != "2") and (FilterSelection != "3") and (FilterSelection != "4"):
                print("")
                print("Invalid filter selection, choose 1-4: ")
            elif FilterSelection == "4":
                Menu = "0"
            
            
### IF THE OPTION FOR DISABLING FILTERS IS CHOSEN, THIS CODE WILL RESET ASSOCIATED VARIABLES
                
            elif FilterSelection =="3":
                BacFilterStatus = "No Bacteria filter."
                GroFilterStatus = "No Growth filter." 
                matrix = originalmatrix
                Menu = "0"
                lowerboundry = float(-2)
                upperboundry = float(2)
                StrainSelected = "no"
                
                     
### HERE WE MANAGE THE SELECTION OF WHICH BATERIA TO FILTER FOR
            
            elif FilterSelection =="1":
                print("")
                print("")
                print("CHOOSE A STRAIN TO USE IN FILTER:")
                print("1.Salmonella enterica")
                print("2.Bacillus cereus")
                print("3.Listeria")
                print("4.Brochothrix thermosphacta")
                print("5.Back to filter options")
                print("")
                print("Current filter(s):",BacFilterStatus,GroFilterStatus)
                BactSelection = input("Please choose 1-5:")
                while BactSelection != "1" and BactSelection != "2" and BactSelection != "3" and BactSelection != "4" and BactSelection != "5":
                    print("Invalid Selection...")
                    BactSelection = input("Please choose 1-5:")
                if BactSelection == "1":
                    matrix = pdMatrix[pdMatrix['Strain'] == 1]
                    BacFilterStatus = "Salmonella filter applied."
                elif BactSelection == "2":
                    matrix = pdMatrix[pdMatrix['Strain'] == 2]
                    BacFilterStatus = "Basillus filter applied." 
                elif BactSelection =="3":
                    matrix = pdMatrix[pdMatrix['Strain'] == 3]
                    BacFilterStatus = "Listeria filter applied." 
                elif BactSelection == "4":
                    matrix = pdMatrix[pdMatrix['Strain'] == 4]
                    BacFilterStatus = "Brochothrix filter applied." 
                
                
### HERE WE APPLY ANY EXISTING GROWTH FILTER (IF ANY IS APPLIED) TO THE NEW SELECTION
                matrix = matrix[matrix['Growth'] >= lowerboundry]
                matrix = matrix[matrix['Growth'] <= upperboundry]
                
                Menu = "0"
                StrainSelected = "yes"    
                
                
### HERE WE MANAGE SELECTION OF THE GROWTH RATE FILTERS    
                
            elif FilterSelection =="2":
                lowerboundry = float(-2)
                upperboundry = float(2)                
                while lowerboundry < low or lowerboundry >= high:
                    try:
                        lowerboundry = float(input("Type lower boundry between 0 and < 1: "))
                        if lowerboundry < low or lowerboundry >= high:
                            print("Invalid range! Please try again.")
                    except:
                        print("Only numbers man! Please try again.")
                    
                while upperboundry < lowerboundry or upperboundry > high:
                    try:
                        print("")
                        print("Now set upper boundry above:",lowerboundry," and <= 1")
                        upperboundry = float(input("Upper boundry: "))
                    except:
                        print("Invalid! Please try again.")     
                
                if StrainSelected == "yes":
                    matrix = pdMatrix[pdMatrix['Strain'] == int(BactSelection)]
                    matrix = matrix[matrix['Growth'] >= lowerboundry]
                    matrix = matrix[matrix['Growth'] <= upperboundry]
                else:
                    matrix = pdMatrix[pdMatrix['Growth'] >= lowerboundry]
                    matrix = pdMatrix[pdMatrix['Growth'] <= upperboundry]
         
                print("")
                print("")
                print("YOU ARE ABOUT TO APPLY GROWTH RATE FILTER WITH:")
                print("Lower boundry:",lowerboundry)
                print("Upper boundry:",upperboundry)
                input("Press ENTER to apply")
                
### FIX "UNABLE TO ADD BOUNDRIES" IF
                matrix = matrix.drop(matrix[matrix.Growth < lowerboundry].index)
                matrix = matrix.drop(matrix[matrix.Growth > upperboundry].index)
                
                GroFilterStatus = "Growth filter applied."
                Menu = "0"


### HERE WE NAVIGATE THE STATISTIC MENU
    while Menu == "3":
        if Loaded != "yes":
            dataStatus = "Unable to performe statistic, you did not load data yet.."
            Menu = "0"
        else:
            print("")
            print("")
            print("CHOOSE STATISTIC(S) TO BE PERFORMED:")
            print("1. Mean Temperature")
            print("2. Mean Growth Rate")
            print("3. Std Temperature")
            print("4. Std Growth Rate")
            print("5. Number of Rows")
            print("6. Mean Cold Growth Rate")
            print("7. Mean Hot Growth Rate")
            print("8. SHOW ALL")
            print("9. Back to Menu")
            print("")
            print("Current filter(s):",BacFilterStatus,GroFilterStatus)
            
            StatChoose = input("Please select 1-9: ")
            while StatChoose != "1" and StatChoose != "2" and StatChoose != "3" and StatChoose != "4" and StatChoose != "5" and StatChoose != "6" and StatChoose != "7" and StatChoose != "8" and StatChoose != "9":
                print("Invalid Selection")
                StatChoose = input("Please select 1-9: ")
            if StatChoose == "9":
                Menu = "0"
            else:
                StatTry = "try"
                while StatTry == "try":
                    try:
                        np.savetxt("StatMatrix.csv", matrix, delimiter=",")
                        print(dataStatistics(matrix,StatChoose))
                        print("")
                        print("Current filter(s):",BacFilterStatus,GroFilterStatus)
                        input("Press ENTER to continue:")
                        print("")
                        StatTry = "no"
                        Menu = "3"
                    except: 
                        print("Insufficient data to perform the chosen statistic. Please verify you didn't filter away all the data. This can be done by choosing 'Show current data' from the main menu.")
                        input("Press ENTER to continue:")
                        StatTry = "no"                      
                        Menu = "3"

### HERE WE MANAGE PLOTTING OPTIONS
                
    if Menu == "4":
        if Loaded != "yes":
            dataStatus = "Unable to generate plots, you did not load data yet."
            Menu = "0"
        elif Loaded == "yes":
            np.savetxt("PlotMatrix.csv", matrix, delimiter=",")
            print("")
            print("")
            print("CHOOSE PLOT TYPE")
            print("1. Bacteria count - BAR PLOT")
            print("2. Bacteria growth rate - GRAPH")
            print("3. Back to Menu")
            print("")
            print("Current filter(s):",BacFilterStatus,GroFilterStatus)
            
            PlotType = input("Choose 1 or 2: ")
            while PlotType != "1" and PlotType != "2" and PlotType != "3":
                print("Invalid selection. Please select 1-3: ")
                PlotType = input("Choose 1-3: ")
            if PlotType == "1" or PlotType =="2":
                PlotTry = "yes"
                while PlotTry == "yes":
                    try:
                        print(dataPlot(PlotType))
                        input("Enjoy This Beautiful Plot! Press ENTER to continue.")
                        print(PlotType)
                        Menu = "0"
                        PlotTry = "no"
                    except:
                        print("")
                        print("Oops! There was an error :( Please verify you didn't filter away all the data. This can be done by choosing 'Show current data' from the main menu.")
                        input("Press ENTER to continue")
                        PlotTry = "no"
                        Menu = "0"                       
            else:
                Menu = "0"


### HERE WE GIVE THE OPTION TO SHOW THE CURRENT DATA WITH THE CURRENT FILTERING SETTINGS:
                
    if Menu == "5":
        if Loaded != "yes":
            dataStatus = "Unable to show data, you did not load data yet."
            Menu ="0"
        
        else:
            print(matrix)
            print("")
            print("Current filter(s):",BacFilterStatus,GroFilterStatus)
            input("Lovely, press ENTER to continue")
            Menu = "0"       
        
    if Menu == "6":
        print("Welcome to PROJECT 1. This program will help you filter, plot and perform basic statistics on bacterial data. Your input MUST be in the form of a .txt file with columns in the order: temperature, growth rate and bacterial strain with row entries (including bacteria strain notation) similar to the test.txt data set available on DTU inside. As you load data the program will seek to clean the data – this meaning invalid rows will be removed according to the described assignment parameters for valid data. As you perform various filter, loading and statistic within the program several temporary '.csv' files will be create in the script folder. These shouldn’t be touched and will be deleted upon closing the program via the interface exit function in the main menu.")
        
        input("Press ENTER to continue.")
        Menu = "0"

### EXITING THE MENU, TEMPORARY FILES WILL BE ATTEMPTED TO BE REMOVED ASWELL
    if Menu == "7":
        try:
            os.remove("clean.txt")
            os.remove("matrix.csv")
            os.remove("PlotMatrix.csv")
            os.remove("StatMatrix.csv")
            exit(0)
        except:
            exit(0)