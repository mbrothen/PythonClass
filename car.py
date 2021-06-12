# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 06:49:23 2020

@author: mbrothen

Car class.  Creates a car object with fuel effeciency, gas level and a drive
method to simpulate driving
"""


class Car:
    # constructor, requires fuel effeciency, gas level at 0
    def __init__(self, fuelEffeciency):
        self._fuelEffeciencey = fuelEffeciency
        self._gasLevel = 0

    # Get the MPG value
    def getMPG(self):
        return self._MPG

    # Get current fuel level
    def getGasLevel(self):
        return self._gasLevel

    # Change the fuelEffeciency measured in Miles/Gallon
    def setMPG(self, fuelEffeciency):
        self._fuelEffeciencey = fuelEffeciency

    # Sets gas level
    def addGas(self, gasLevel):
        self._gasLevel = gasLevel

    # Simulates driving, takes distance driven and subtracts fuel based on
    # loaded fuel effeciency
    def drive(self, distance):
        self._gasLevel = self._gasLevel - (distance / self._fuelEffeciencey)
