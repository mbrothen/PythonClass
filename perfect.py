# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 19:17:01 2020
Calculates all perfect numbers from 1 to 1000 and displays the results
A perfect number is a number where all numbers that evenly divide it 
add up to the number

@author: mbrothen
"""
#Declare Variables
currentNumber = 1

print ("These are the perfect numbers between 1 and 1000: ")
while currentNumber <= 1000:  #iterate through numbers 1 to 1000
    sum = 1 #placeholder sum for each number's divisors
    i = 2
    hasDivisors = False  #bool to flip when a number is able to be divided, prevents 1
    while i * i < currentNumber:
        #find numbers that divide into current numnber
        hasDivisors = True  #flags if number was able to be tested
        if currentNumber % i == 0:
            sum = sum + i + currentNumber/i #add divisors to sum
        i += 1
        
    if sum == currentNumber and hasDivisors:
        print(str(currentNumber) + " is a perfect number");
        
    currentNumber += 1