# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 12:19:34 2020

@author: mbrot
"""
def isAdjacent(checkString):
    checkString = checkString.lower()
    if len(checkString) == 0:
        return "Empty string"
    i = 0
    while i < (len(checkString)-1):
        if checkString[i] == checkString[i+1]:
            return True
        i += 1
    if i == (len(checkString)-1):
        return False

print( isAdjacent("ApPle"))
print( isAdjacent("Python"))
print( isAdjacent(""))

def salesBonus():
    itemsSold = 5
    MIN_ITEMS = 4
    totalValue = 6
    MIN_VALUE = 5
    SALES_BONUS = 1000
    if itemsSold > MIN_ITEMS and totalValue >= MIN_VALUE:
        bonus = SALES_BONUS
        print(bonus)

salesBonus()