# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 19:48:35 2019

@author: bebi
"""

def convertTemperature(T, unitFrom, unitTo):
    if unitFrom == "Celsius":
        if unitTo == "Fahrenheit":
            N = 1.8 * T + 32
        elif unitFrom == "Kelvin":
            N = T + 273.15

    if unitFrom == "Fahrenheit":
        if unitTo == "Celsius":
            N = (T - 32) / 1.8
        elif unitTo == "Kelvin":
            N = (T + 459.67) / 1.8

    if unitFrom == "Kelvin":
        if unitTo == "Celsius":
            N = T - 273.15
        elif unitTo == "Fahrenheit":
            N = 1.8 * T - 459.67
    return N