# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 13:05:10 2020
Inches To Feet
@author: mbrothen
"""
INCHES_IN_FOOT = 12

inchesToCalculate = input("Enter a length in inches: ");

numberOfFeet = int(inchesToCalculate) // INCHES_IN_FOOT
numberOfInches = int(inchesToCalculate) % INCHES_IN_FOOT

print(inchesToCalculate + " inches is equal to " + str(numberOfFeet) + " feet and " + str(numberOfInches) + " inches")