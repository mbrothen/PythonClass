# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 07:10:44 2020
10 numbers, reads 10 numbers and cmopares them to a list of numbers.
If the numbers are not in a list it adds them to the list.
@author: mbrothen
"""


def main():

    numberList = []

    def getNumber():
        number = int(input("Enter a number: "))
        return number

    def printList(numbers):
        # Print the list after it is 10 units long
        print("Final number list")
        x = 1
        for i in numbers:
            print(str(x) + ": " + str(i))
            x += 1

    def checkList():
        # Get numbers until the list is 10 units long, only add new numbers
        while len(numberList) < 10:
            number = getNumber()
            if number not in numberList:
                numberList.append(number)
        printList(numberList)

    checkList()


main()
