# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 19:37:27 2020

Check credit card number validity for 8 digit sample credit cards

The last digit of a credit card number is the check digit, which protects against transcription errors such as an error in a single digit or switching two digits. The following method is used to verify actual credit card numbers but, for simplicity, we will describe it for numbers with 8 digits instead of 16:

        Starting from the rightmost digit, form the sum of every other digit. For example, if the credit card number is 4358 9795, then you form the sum 5 + 7 + 8 + 3 = 23.
        Double each of the digits that were not included in the preceding step. Add all digits of the resulting numbers. For example, with the number given above, doubling the digits, starting with the next-to-last one, yields 18 18 10 8. Adding all digits in these values yields 1 + 8 + 1 + 8 + 1 + 0 + 8 = 27.
        Add the sums of the two preceding steps. If the last digit of the result is 0, the number is valid. In our case, 23 + 27 = 50, so the number is valid.


@author: mbrothen
"""
#Declare variables
evenPositionCounter = 7
oddPositionCounter = 6
evenPositionSum = 0
oddPositionSum = 0
finalTestNumber = 0
creditCardNumber = ""

print("Verify the value of a credit card")
while True and len(creditCardNumber) != 8:  #Get a valid input
    try:
        creditCardNumber = input("Enter and 8 digit credit card number: ")
    except ValueError:
        print("Enter a valid number")  
    else: 
        break

#Get everyother digit from the position 8 to 0 and sum
while evenPositionCounter >= 1:
    evenPositionSum = evenPositionSum + int(creditCardNumber[evenPositionCounter])
    evenPositionCounter -= 2 
    
while oddPositionCounter >= 0:
    #Get odd position values and multiply by 2
    currentNumber = int(creditCardNumber[oddPositionCounter]) * 2 
    #break down the value to the each digit value and add them to the sum of odd digits
    for i in range(0, len(str(currentNumber))):
       oddPositionSum = oddPositionSum + int(str(currentNumber)[i])
    oddPositionCounter -= 2
    
#add the two numbers
finalTestNumber = evenPositionSum + oddPositionSum
#If last digit is 0 the number is valid
if str(finalTestNumber)[len(str(finalTestNumber))-1] == "0" :
    print(creditCardNumber + " is a valid credit card number")
else:
    print(creditCardNumber + " is not a valid credit card numnber")
