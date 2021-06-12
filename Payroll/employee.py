# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 07:35:48 2020
Creates employee class
@author: mbrothen
"""


class Employee(object):

    # creates emplyee
    def __init__(self, employeeName, hoursWorked, payRate):
        try:
            self._employeeName = employeeName
            self._employeeType = "employee"
            self._hoursWorked = float(hoursWorked)
            self._payRate = float(payRate)
        except:
            # Return a value error if non numerical are entered
            return ValueError

    # Set Name
    def setName(self, employeeName):
        self._name = employeeName

    # Set employee type
    def setEmployeeType(self, employeeType):
        self._employeeType = employeeType

    # Set hours worked
    def sethoursWorked(self, hoursWorked):
        self._hoursWorked = float((hoursWorked))

    # Set Pay Rate
    def setPayRate(self, payRate):
        self._payRate = float(payRate)

    # get name
    def getName(self):
        return self._employeeName

    # get employee type
    def getEmployeeType(self):
        return self._employeeType

    # get hours worked
    def getHoursWorked(self):
        return self._hoursWorked

    # Get Payrate
    def getPayRate(self):
        return self._payRate

    # Calulate employees pay
    def totalPay(self):
        # calcualte base pay
        pay = self._payRate * self._hoursWorked
        # Calculate overtime pay
        if self._hoursWorked > 40:
            pay = pay + ((self._hoursWorked - 40) * (self._payRate * .5))
        return pay

    # Calculate and return pay for hours below 40
    def regularPay(self):
        # caclulate regular pay
        if self._hoursWorked > 40:
            return self._payRate * 40
        else:
            return self._payRate * self._hoursWorked

    # Calculate pay for hours over 40
    def overTimePay(self):
        # Calcualte overtime pay
        if self._hoursWorked > 40:
            return self._payRate * (self._hoursWorked - 40)
        else:
            return 0
