# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 16:05:07 2020
Gets an integer input and converts it to binary 
@author: mbrothen
"""
#Decalre Variables
i = 0
numberInBinary = ""
quotient = 0

#Get input number until a valid number is entered
while True:
    try:
        numberToConvert = input("Enter a number to convert to binary: ")
        testInputForNumber = int(numberToConvert)  #fails if nonnumber
    except ValueError:
        print("Enter a valid integer")  
    else: 
        break
#convert the int to binary
"""
Conversion steps:
    Divide the number by 2.
    Get the integer quotient for the next iteration.
    Get the remainder for the binary digit.
    Repeat the steps until the quotient is equal to 0.
    https://www.rapidtables.com/convert/number/decimal-to-binary.html
"""
quotient = int(numberToConvert)  #Get working var while saving original input
while quotient != 0:
    if (quotient % 2 == 0):
        #add a 0 to the front of the string if no remainder
        numberInBinary = "0"+ numberInBinary 
    else:
        #add a 1 to front of string if there is a remainder
        numberInBinary = "1" + numberInBinary
    quotient = quotient // 2   #Get remainder to test for next digit
    
#Display Results    
print(numberToConvert + " in binary is: " + numberInBinary)