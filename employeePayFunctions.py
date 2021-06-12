# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 06:15:05 2020
Calclualates an employees paycheck based on employee type, hours work and wage
@author: mbrothen
"""


def main():
    def getInfo():
        # Inputs
        empName = input("Enter employee name: ")
        empType = input("Enter employee type (employee or supervisor): ")

        if (empType == "employee"):
            empWage = input("Enter the employees hourly rate: ")
        else:
            empWage = input("Enter the employees salary: ")

        empHours = input("Enter the hours worked by employee: ")
        # convert strings to float
        empWage = float(empWage)
        empHours = float(empHours)

        return [empName, empType, empWage, empHours]

    def calculatePay(data):
        # Calculations
        # Convert to int for calculations
        empWage = data[2]
        empHours = data[3]
        empType = data[1]
        # Calculate supervisor wages, salary/52
        if empType == "supervisor":
            empPay = empWage/52
            overtimePay = 0
            # Calculate employee type pay
        else:
            # Calculate no overtime rate* hours worked
            if empHours <= 40:
                empPay = empWage * empHours
                overtimePay = 0
            # calculate overtime
            elif empHours > 40:
                overtimePay = ((empWage * 1.5) * (empHours-40))
                empPay = (empWage * 40)
        return data.extend([empPay, overtimePay])

    def displayPay(data):
        print("Employee:    " + data[0].rjust(10))
        print("Hours Worked:" + str(data[3]).rjust(10))
        if data[1] == "employee":
            print("Hourly Rate: " + str("${:,.2f}".format(data[2])).rjust(10))
            print("Regular Pay: " + str("${:,.2f}".format(data[4])).rjust(10))
            print("Overtime Pay:" + str("${:,.2f}".format(data[5])).rjust(10))
        else:
            print("Annual Wage: " + str("${:,.2f}".format(data[2])).rjust(10))
            print("Weekly Pay:  " + str("${:,.2f}".format(data[4])).rjust(10))
        print("=======================")
        print("Total Pay:   " + str("${:,.2f}".format(data[4]+data[5])).rjust(10))

    data = getInfo()
    calculatePay(data)
    displayPay(data)


main()