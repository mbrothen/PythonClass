# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 19:18:58 2020

@author: mbrot
"""


from person import Person


class Instructor(Person):

    # creates emplyee
    def __init__(self, name, yearOfBirth, salary):
        try:
            super().__init__(name, yearOfBirth)
            self._salary = salary
        except:
            return ValueError

    # Set Name
    def setSalary(self, salary):
        self._salary = salary

    # get name
    def getSalary(self):
        return self._salary
