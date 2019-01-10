# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 14:34:35 2018

@author: bebi
"""

def pH2Category(pH):
    category = ""
    if 0.0 <= pH and pH < 3.0:
        category = 'Strongly acidic'  
    elif pH >= 3.0 and pH < 6.0:
         category = 'Weakly acidic'    
    elif pH >= 6.0 and pH <= 8.0:
         category = 'Neutral'   
    elif pH > 8.0 and pH <= 11.0:
         category = 'Weakly basic'
    elif pH > 11.0 and pH <= 14.0:
         category = 'Strongly basic'
    else:
         category = 'pH out of range'
    return category
    
#print(pH2Category(2.3))



