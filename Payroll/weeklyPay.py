# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 14:10:15 2020
Create employee objects and display pay statement
@author: mbrothen
"""

from employee import Employee
from supervisor import Supervisor


def main():

    def menu():
        # Display choice to continue adding employees after first employee
        choice = ""
        while choice != "n":
            while choice != "y" and choice != "n":
                choice = input("Enter another employee?  Y/N: ")
                choice = choice.lower()
            if choice == "y":
                createEmployee()

    def printEmployee(employee):
        # Display employee pay infomration.  Could have also been done
        # in the employee class
        print("-------WEEKLY PAY-------")
        print("Employee Name: " + employee.getName())
        print("Employee Type: " + employee.getEmployeeType())
        print("Hours Worked: " + str(employee.getHoursWorked()))
        print("Employee Pay Rate: $" + str(employee.getPayRate()))
        if employee.getEmployeeType() == "supervisor":
            print("Employee Pay Total: " + str(employee.calculatePay()))
        else:
            print("Employee Regular  Pay: $" + str(employee.regularPay()))
            print("Employee Overtime Pay: $" + str(employee.overTimePay()))
            print("Employee Total Pay:    $" + str(employee.totalPay()))
        menu()

    def createEmployee():
        # Create employee, choose object type based on entered information
        name = input("Enter employee name: ")
        empType = input("Enter employee type (employee or supervisor): ")
        payRate = input("Enter employee payrate: ")
        hoursWorked = input("Enter hours worked: ")
        try:
            if empType.lower() == "employee":
                newEmployee = Employee(name, hoursWorked, payRate)
            elif empType.lower() == "supervisor":
                newEmployee = Supervisor(name, hoursWorked, payRate)
        except:
            print("Invalid data entered, please re-enter")
            createEmployee()
        printEmployee(newEmployee)

    createEmployee()


main()
