import numpy as np
import pandas as pd

def dataStatistics(data, statistic):
    matrix = np.array(pd.read_csv('StatMatrix.csv', sep=',', header=None))

    # MEAN TEMPERATURE
    if statistic == "1":
        result = np.mean(matrix[:,0])
        StatType = "Mean Temperature"
    # MEAN GROWTH RATE    
    elif statistic == "2":
        result = np.mean(matrix[:,1])
        StatType = "Mean Growth Rate"
    # STD TEMPERATURE    
    elif statistic == "3":
        result = np.std(matrix[:,0])
        StatType = "Std Temperature"
    # STD GROWTH RATE    
    elif statistic == "4":
        result = np.std(matrix[:,1])
        StatType = "Std Growth Rate"
    # NUMBER OF ROWS
    elif statistic == "5":
        result = np.size(matrix, axis=0)
        StatType = "Number of rows"
    # MEAN COLD GROWTH RATE   
    elif statistic == "6":
        Temp = matrix[:,0]
        result = np.mean(Temp[Temp < 20])
        StatType = "Mean Cold Growth Rate"
    # MEAN HOT GROWTH RATE    
    elif statistic == "7":
        Temp = matrix[:,0]
        result = np.mean(Temp[Temp > 50])
        StatType = "Mean Hot Growth Rate"
    
    elif statistic == "8":
        print("")
        print("")
        print("ALL STATISTICS:")
        print("Mean Temperature:",np.mean(matrix[:,0]))
        print("Mean Growth Rate:",np.mean(matrix[:,1]))
        print("Std Temperature:",np.std(matrix[:,0]))
        print("Std Growth Rate:",np.std(matrix[:,1]))
        print("Number of Rows:",np.size(matrix, axis=0))
        Temp = matrix[:,0]
        print("Mean Cold Growth Rate:",np.mean(Temp[Temp < 20]))
        print("Mean Hot Growth Rate:",np.mean(Temp[Temp > 50]))
        StatType = ""
        result = ""
    print("")
    print(StatType)
    return result
