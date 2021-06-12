# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 06:34:55 2020
Calculates the season based on an entered month and day
@author: mbrothen
"""
month = input("Enter a month number to find the season: ")
day = input("Enter the day of the month: ")
month = int(month) #convert month to an int
day = int(day)  #convert day to an int

if (month == 1 or month == 2 or month == 3):
	season = "Winter"
elif (month == 4 or month == 5 or month == 6):
	season = "Spring"
elif (month == 7 or month == 8 or month == 9):
	season = "Summer"
elif (month == 10 or month == 11 or month == 12):
	season = "Fall"
if (month % 3 == 0 and day >= 21):  #adjust season for the mid month change
	if season == "Winter":
		season = "Spring"
	elif season == "Spring":
		season = "Summer"
	elif season == "Summer":
		season == "Fall"
	else:
		season = "Winter"

#Display the resutlts
print("The season for " + str(month) + "/" + str(day) + " is: " + season)