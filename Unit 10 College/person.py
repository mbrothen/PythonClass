# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 19:02:58 2020
Person Object, creates person with name and year of birth
@author: mbrothen
"""


class Person(object):

    # creates emplyee
    def __init__(self, name, yearOfBirth):
        try:
            self._name = name
            self._yearOfBirth = yearOfBirth
        except:
            return ValueError

    # Set Name
    def setName(self, name):
        self._name = name

    # Set employee type
    def setYearOfBirth(self, yearOfBirth):
        self._yearOfBirth = yearOfBirth

    # get name
    def getName(self):
        return self._name

    # Get year of birth
    def getYearOfBirth(self):
        return self._yearOfBirth
