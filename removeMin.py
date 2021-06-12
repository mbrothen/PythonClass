# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 07:27:03 2020
Gets a list of numbers, removes the minimum number
@author: mbrothen
"""


def main():

    def getNumbers(length):
        # Retrive X number if integers and builds the list
        i = 0
        numberList = []
        while i < length:
            number = int(input("Enter a number: "))
            numberList.append(number)
            i += 1
        return numberList

    def getListLength():
        # Get the length of list the user wants to test
        listLength = int(input("Enter the length of list: "))
        return(listLength)

    def removeMin(numberList):
        # Removes the lowest number from the list
        # Sets the first number to the min then tests all other list items
        # against the min, if the next item is lower set it as min for the rest
        min = numberList[0]
        for i in numberList:
            if i < min:
                min = i
        numberList.remove(min)
        return(numberList)

    numbers = getNumbers(
        getListLength()
        )
    numbers = removeMin(numbers)
    print(numbers)


main()
