import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)

def dataPlot(PlotType):
    # LOAD THE NEWLY CREATED DATA
    matrix = pd.read_csv('PlotMatrix.csv', sep=',')
    matrix.columns = ["Temp", "Growth", "Strain"]   
   
    # SEPERATE DATA FOR THE TWO DIFFERENT PLOTS
    # PLOT 1 DATA
    BactOnly = np.transpose(matrix.iloc[:,2])
    BactNames = ('Salmonella enterica', 'Bacillus cereus', 'Listeria', 'Brochothrix thermosphacta')
    
    # PLOT 2 DATA
    Salmonella_data = matrix[matrix['Strain'] == 1].sort_values(by=['Temp'], ascending=True)
    Bacillus_data = matrix[matrix['Strain'] == 2].sort_values(by=['Temp'], ascending=True)
    Listeria_data = matrix[matrix['Strain'] == 3].sort_values(by=['Temp'], ascending=True)
    Brocho_data = matrix[matrix['Strain'] == 4].sort_values(by=['Temp'], ascending=True)
   
    # COUNT NUMBER OF DIFFERENT BACTERIAS
    BactCount = np.empty(4)
    BactCount[0]  = np.count_nonzero(BactOnly == 1)
    BactCount[1]  = np.count_nonzero(BactOnly == 2)
    BactCount[2]  = np.count_nonzero(BactOnly == 3)
    BactCount[3]  = np.count_nonzero(BactOnly == 4)
    
    if PlotType == "1":
        figure(num=None, figsize=(7, 6), dpi=100, facecolor='w', edgecolor='k')
        y_pos = np.arange(len(BactNames))
        plt.bar(y_pos, BactCount, align='center')
        plt.xticks(y_pos, BactNames)
        plt.ylabel('Count')
        plt.title('Bacteria Type')
        plt.show()

    elif PlotType =="2":
        figure(num=None, figsize=(7, 6), dpi=100, facecolor='w', edgecolor='k')
        plt.plot(Salmonella_data['Temp'],Salmonella_data['Growth'],'C9',label='Salmonella', linewidth=3)
        plt.plot(Bacillus_data['Temp'],Bacillus_data['Growth'],'C3',label='Bacillus', linewidth=3)
        plt.plot(Listeria_data['Temp'],Listeria_data['Growth'],'C2',label='Listeria', linewidth=3)
        plt.plot(Brocho_data['Temp'],Brocho_data['Growth'],'C1',label='Brocho', linewidth=3)
        plt.title('Temperature')
        plt.ylabel('Growth rate')
        plt.legend()
        plt.xlim(xmin=10)
        plt.xlim(xmax=60)
        plt.ylim(ymin=0)
        plt.ylim(ymax=1)

    plt.show()
        


    