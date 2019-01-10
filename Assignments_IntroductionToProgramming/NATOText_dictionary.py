# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 09:35:18 2018

@author: bebi
"""
import numpy as np

def textToNato(plainText):
    natoText = ""
    codes = {'A':'Alpha', 'B':'Bravo','C':'Charlie', 'D':'Delta', 'E':'Echo', 'F':'Foxtrot', 'G':'Golf',"H":"Hotel", 'I':'India', 'J':'Juliet', 'K':'Kilo', 'L':'Lima', 'M':'Mike', 'N':'November', 'O':'Oscar', 'P':'Papa', 'Q':'Quebec', 'R':'Romeo', 'S':'Sierra', 'T':'Tango', 'U':'Uniform', 'V':'Victor', 'W':'Whiskey', 'X':'Xray', 'Y':'Yankee', 'Z':'Zulu'}
    for i in range(len(plainText)):
        if (i > 0 and i < len(plainText)):
            natoText = "-".join((natoText, codes[plainText[i].upper()] ))
        else:
            natoText += codes[plainText[i].upper()]
            
    return natoText
        

print(textToNato("helllo"))