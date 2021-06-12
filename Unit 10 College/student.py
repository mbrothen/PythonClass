# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 19:15:37 2020
Extends class person to add student value of major
@author: mbrothen
"""


from person import Person


class Student(Person):

    # creates emplyee
    def __init__(self, name, yearOfBirth, major):
        try:
            super().__init__(name, yearOfBirth)
            self._major = major
        except:
            return ValueError

    # Set Name
    def setMajor(self, major):
        self._major = major

    # get name
    def getMajor(self):
        return self._major
