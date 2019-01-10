# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 14:50:02 2018

@author: bebi
"""

import numpy as np
import pandas

def computeLanguageError(input):
    LetterFreq = pandas.read_csv("letter_frequencies.csv", usecols=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
    LetterFreq = np.transpose(np.asarray(LetterFreq))
    E = np.sum(np.transpose((input - LetterFreq)**2), axis=0) 
    return E