# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 16:53:48 2020
Retreive a list of books from the Hur machine and display the results
@author: mbrothen
"""
import urllib.request
import urllib.parse
import json

# Book API URL
url = "http://apollo.gtc.edu/~hurc/152-081/unit8/api/"

webData = urllib.request.urlopen(url)
results = webData.read().decode()
webData.close()

# Covert json result to dictionary
books = json.loads(results)

# print the results
bookNumber = 1
for book in books:
    print("------------------------------------")
    print("----------Book Number "+ str(bookNumber) + "-------------")
    print("------------------------------------")

    for field in book:
        print(field + ": " + str(book[field]))
    print("\n")
    bookNumber += 1
