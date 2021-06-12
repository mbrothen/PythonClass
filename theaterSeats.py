# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 08:53:29 2020
Allows user to purchase tickets either by seat number or by a price point
keeps track of purchased seats with the seat list

@author: mbrothen
"""


def main():
    # Reversed the order of the seats so they are filled from front to back and
    #  the row numbers make sense
    seats = [
        # 1   2   3   4   5   6   7   8   9  10          Seat#
        [30, 40, 50, 50, 50, 50, 50, 50, 40, 30],  # 1   Row#
        [20, 20, 30, 30, 40, 40, 30, 30, 20, 20],  # 2
        [20, 20, 30, 30, 40, 40, 30, 30, 20, 20],  # 3
        [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],  # 4
        [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],  # 5
        [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],  # 6
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],  # 7
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],  # 8
    ]

    def goodbye():
        print("Enjoy the show!")

    def displaySeats(seats):
        # Display the seats as a table
        seatNumber = 1
        rowCounter = 1
        print("\n\n\n")
        print("              AVAILABLE SEATS")
        for i in seats:
            if rowCounter == 1:
                print("Seat # ", end="")
                while seatNumber <= len(seats[0]):
                    print(" " + str(seatNumber), end=", ")
                    seatNumber += 1
                print()

            print("Row " + str(rowCounter) + " " + str(i))
            rowCounter += 1

    def displayMenu():
        # Display the main menu and get input
        displaySeats(seats)
        print("Welcome to the theater!")
        print("Buy a ticket.  Enter either: ")
        print("1: A price you'd like to pay, 10, 20, 30, 40, or 50")
        print("2: a specific seat in (row,seat)")
        print("3 X to exit")
        userOption = input("Enter your choice: ")
        checkInput(userOption)

    def checkInput(option):
        # process user input, call appropriate function
        exitOptions = ["x", "X", "exit", "EXIT"]
        seatPrices = ["10", "20", "30", "40", "50"]

        if option in exitOptions:
            goodbye()
        elif option in seatPrices:
            findOpenSeat(int(option))
        elif "," in option:
            splitOption(option)
        else:
            print("Invlaid Option")
            displayMenu()

    def findOpenSeat(option):
        # find the best seat for the price
        # best is the closest to the front
        seatFound = False
        for i in range(len(seats)):
            for j in range(len(seats[i])):
                if seats[i][j] == option and not seatFound:
                    print("You just purchased seat: " + str(i+1) +
                          "," + str(j+1))
                    seats[i][j] = 00
                    seatFound = True
        if seatFound:
            print("No seats available in that price, pick a new price")

        displayMenu()

    def splitOption(option):
        # convert option into seat and row
        row, seat = option.split(',')
        row = int(row)
        seat = int(seat)
        checkSeat(row, seat, seats)

    def checkSeat(row, seat, seats):
        # check if seat is available
        if seats[row-1][seat-1] != 00:
            seats[row-1][seat-1] = 00
            print("You just purchased seat " + str(row) +
                  "," + str(seat) + "!")
            displayMenu()
        else:
            print("Seat " + str(row) + "," + str(seat) + " is not avaiable. " +
                  "Please make a new selection")
            displayMenu()

    displayMenu()


main()
