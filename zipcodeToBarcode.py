# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 09:58:50 2020
Gets a 5 digit zip code and converts the zip code to a barcode
@author: mbrothen
"""


def main():
    def getDigit():
        # Gets the barcode from user
        validZip = False
        while not validZip:
            zipCode = input("Enter a 5 digit zipcode: ")
            try:
                # Verify int, ask again if not
                int(zipCode)
                if len(zipCode) != 5:
                    # Verify number is appropriate length, ask again if not
                    print("Make sure zipcode is 5 digits")
                    validZip = False
                else:
                    validZip = True
            except ValueError:
                print("Enter a number")
                validZip = False
        return zipCode

    def printDigit(d):
        # Output barcode for specific number
        conversionTable = [
            [1, 1, 0, 0, 0],  # 0
            [0, 0, 0, 1, 1],  # 1
            [0, 0, 1, 0, 1],  # 2
            [0, 0, 1, 1, 0],  # 3
            [0, 1, 0, 0, 1],  # 4
            [0, 1, 0, 1, 0],  # 5
            [0, 1, 1, 0, 0],  # 6
            [1, 0, 0, 0, 1],  # 7
            [1, 0, 0, 1, 0],  # 8
            [1, 0, 1, 0, 0],  # 9
            ]
        for i in conversionTable[int(d)]:
            if i == 1:
                print("|", end="")
            elif i == 0:
                print(":", end="")

    def checkDigit(zipCode):
        # Calculate the check digit
        total = 0
        checkDigit = 0
        for d in zipCode:
            total += int(d)
        while total % 10 != 0:
            total += 1
            checkDigit += 1
        printDigit(checkDigit)

    def printEncodedBarcode(zipCode):
        # Print the barcode
        # Print leading bar
        print(str(zipCode) + " is: ")
        # Print frame bar
        print("|", end="")
        # interate through barcode to print each digit
        for d in zipCode:
            printDigit(d)
        # Calculate and print check digit
        checkDigit(zipCode)
        # Print trailing frame bar
        print("|")

    zipCode = getDigit()
    printEncodedBarcode(zipCode)


main()
