# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 08:45:54 2018

@author: bebi
"""

import numpy as np

def textToNato(plainText):
    natoText = ""
    NATOAlphabet = np.array(["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliet", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor", "Whiskey", "Xray", "Yankee", "Zulu"])
    for i in range(len(plainText)):
        for j in range(np.size(NATOAlphabet)):
            if (plainText[i]).lower() == ((NATOAlphabet[j])[0]).lower():            
                if (i > 0):
                    natoText = "-".join((natoText, NATOAlphabet[j]))
                else:
                    natoText += NATOAlphabet[j]
            
    return natoText
        

#print(textToNato("hllo"))