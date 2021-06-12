# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 10:55:23 2020
Unit 2 Practice
@author: Matt Brothen
"""
#Variables and Constants
#Create a constant named TAX_RATE and assign it a value of .075
TAX_RATE = 0.075  
 #Create a variable named shippingCostPerBook and assign it a value of 2
shippingCostPerBook = 2 
# Use an input statement to ask the user for the number of books purchased and assign it to a variable numBooks
numBooks = input("Number of books purchased?: ") 
#Use an input statement to ask the user for the price for the book and assign it to a variable bookPrice
bookPrice = input("Price of each book?: ")

#Calculate the total price for the books by multiplying the variable that holds the number of
#books purchased by the variable that holds the price of the book. Assign this to a variable.
totalForBooks = int(numBooks) * float(bookPrice)
#Calculate the total tax by multiplying the variable that holds the number of books by the tax
#rate. Assign this to a variable.
totalTax = totalForBooks * TAX_RATE
#Calculate the total shipping by multiplying the variable that holds the number of books by the
#variable that holds the shipping cost per book.
totalShipping = int(numBooks) * shippingCostPerBook
#Calculate the total of the order by adding together the values you calculated above.
orderTotal = totalForBooks + totalTax + totalShipping

#Create the print statements you need to create the specified output. Use the “%.2f” % syntax to
#limit what is displayed to 2 decimal places.
print("**************Your Order Total**************")
print("Cost of Books:  " + str("%.2f" %(totalForBooks)))
print("Total Tax:      " + str("%.2f" %(totalTax)))
print("Total Shipping: " + str("%.2f" %(totalShipping)))
print("--------------------------------------------")
print("Order Total:    " + str("%.2f" %(orderTotal)))