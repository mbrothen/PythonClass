# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 13:13:29 2020
Dollars.py  Finds the change brakedown for a given dollar value
@author: mbrothen
"""
#Consts
HUNDRED = 100
FIFTY = 50
TWENTY = 20
TEN = 10
FIVE = 5
ONE = 1

numberOfDollars = input("Enter dollars to make change for: ")

#Woudl be cleaner with loops...
numberOfDollars = int(numberOfDollars)  #convert to int once

numberOfHundreds = numberOfDollars // HUNDRED  #FInd number of Hundreds
remainingMoney = numberOfDollars - (numberOfHundreds * HUNDRED) #Get remaining dollar value

numberOfFifties = remainingMoney // FIFTY
remainingMoney = remainingMoney - (numberOfFifties * FIFTY)

numberOfTwenties = remainingMoney // TWENTY
remainingMoney = remainingMoney - (numberOfTwenties * TWENTY)

numberOfTens = remainingMoney // TEN
remainingMoney = remainingMoney - (numberOfTens * TEN)

numberOfFives = remainingMoney // FIVE
remainingMoney = remainingMoney - (numberOfFives * FIVE)

numberOfOnes = remainingMoney // ONE

print("$100 Bills: " + str(numberOfHundreds))
print("$50 Bills: " + str(numberOfFifties))
print("$20 Bills: " + str(numberOfTwenties))
print("$10 Bills: " + str(numberOfTens))
print("$5 Bills: " + str(numberOfFives))
print("$1 Bills: " + str(numberOfOnes))
