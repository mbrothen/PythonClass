# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 07:35:48 2020
Extends employee and creates supervisor which changes pay calculations
and employee type
@author: mbrothen
"""

from employee import Employee


class Supervisor(Employee):

    # creates supervisor
    def __init__(self, employeeName, hoursWorked, payRate):
        try:
            self._employeeName = employeeName
            self._employeeType = "supervisor"
            self._hoursWorked = float(hoursWorked)
            self._payRate = float(payRate)
        except:
            # Return a value error if non numerical are entered
            return ValueError

    def calculatePay(self):
        return self._payRate / 52
