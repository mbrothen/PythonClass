# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 11:30:14 2020
Unit2 Practice Postage
@author: mbrothen
"""
#Create a constant named POSTAGE_COST. Assign it the value of 0.42 (0.42 dollars) or 42 (42
#pennies) - your choice how you want to handle this. Using pennies can help avoid rounding
#errors, but later you need to divide your results by 100 to return to dollars and cents.
POSTAGE_COST = 0.42


#Ask the user for the weight of the letter. The weight is always measured in ounces, for
#example 3.2 ounces or 15 ounces.
letterWeight = input("Enter the weight of a letter in ounces: ")

#Create a variable named totalLetterCost.
#Calculate the total cost to mail the letter - totalLetterCost - by multiplying the weight of the
#letter by the cost of postage and assign the result to variable totalLetterCost
totalLetterCost = POSTAGE_COST * float(letterWeight)

#Display the value of totalLetterCost in this sentence “Your letter will cost $nn.nn to mail”
#Display the value you calculated instead of nn.nn. Limit the display to 2 decimal places and be
#sure to include the dollar sign

print("Your letter will cost $" + str("%.2f" %(totalLetterCost)) + " to mail")
