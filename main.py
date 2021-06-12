# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 07:21:21 2020
Implements car class
Creaets a car, adds gas and drives, then prints remaining fuel level
@author: mbrothen
"""


from car import Car

myHybrid = Car(50)
myHybrid.addGas(20)
myHybrid.drive(100)
print("Current fuel level: " + str(myHybrid.getGasLevel()))
