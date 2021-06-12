# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 14:45:10 2020
Gets string input and checks if the string is a palindrome
@author: mbrothen
"""
palindrome = True
i = 0

#Get string to check

checkString = input("Enter a word to check if it's a palindrome: ")


# Process string and check for palindrome

#Loop through the string from 0 to half the length of the string
while i < (len(checkString)/2) and palindrome == True:
    #compare letter at the current counter with the letter at the oposite end
    # if they're not the same return false to not a palindrome
    if checkString[i] != checkString[len(checkString)-i-1]:
        palindrome = False
    i += 1
        
#Print results based on value of palindrome
if palindrome == False:
    print (checkString + " is not a palindrome")
else:
    print(checkString + " is a palindrome")
    