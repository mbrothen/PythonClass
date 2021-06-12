# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 07:14:51 2020
Calculates employee pay based on their job function, hours worked and pay rate
@author: mbrothen
"""
#Inputs
empName = input("Enter employee name: ")
empType = input("Enter employee type (employee or supervisor): ")

if (empType == "employee"):	
	empWage = input("Enter the employees hourly rate: ")
else:
	empWage = input("Enter the employees salary: ")


empHours = input("Enter the hours worked by employee: ")

#Calculations
#Convert to int for calculations
empWage = float(empWage)
empHours = float(empHours)

if empType == "supervisor":
	empPay = empWage/52
else:
	if empHours <= 40:
		empPay = empWage * empHours
	elif empHours > 40:
		empPay = (empWage * 40) + ((empWage * 1.5) * (empHours-40)) 
	
print(empName + "'s pay for working " + str(empHours) + " hours is: $" + str(empPay))