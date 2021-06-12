# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 07:07:40 2020
Demonstration of numPy and pyplot
@author: mbrothen
"""

import numpy as np
import matplotlib.pyplot as pyplot

def main():

    def arrays():
        x = np.array([[1, 2, 3], [6, 7, 8]])
        print(x)
        printArrays(x)

        y = np.array([[1, 2, 3], ["cat", "dog", "ferret"]])
        print(y)
        printArrays(y)

    def printArrays(arr):
        # Total dimensions
        print("The number of dimensions in this array: ", end="")
        print(arr.ndim)

        # Shape
        print("The shape of this array is ", end="")
        print(arr.shape)

        # Data Types
        print("The data types in this array are ", end="")
        print(arr.dtype)

        # Bytes
        print("The number of bytes in each item: ", end="")
        print(arr.itemsize)
        print("Other Print")
        print(arr[0])
        print(arr[1])

    def rainChart(inches, months):
        pyplot.plot(months, inches)
        pyplot.title("Average Rainfall In Kenosha, Wi")
        pyplot.grid("on")
        pyplot.xlabel("Months")
        pyplot.ylabel("Rainfall in Inches")

    def barChart(inches, months):
        pyplot.bar(months, inches, color="blue")
        pyplot.title("Average Rainfall in Kenosha, Wi")
        pyplot.xlabel("Months")
        pyplot.xlabel("Rainfall in Inches")

    def scatterChart(inches, months):
        pyplot.scatter(months, inches, color="red")
        pyplot.title("Average Rainfall In Kenosha, Wi")
        pyplot.grid("on")
        pyplot.xlabel("Months")
        pyplot.ylabel("Rainfall in Inches")

    def charts():
        rainData = np.array([
            ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
             "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
            [1.76, 1.39, 2.57, 3.77, 3.94, 3.63,
             3.63, 4.05, 3.47, 2.99, 2.82, 2.12]
            ])
        # print(rainData[0], rainData[1])
        floatRainData = rainData[1].astype(float)
        # print(floatRainData)
        # rainChart(floatRainData, rainData[0])
        # barChart(floatRainData, rainData[0])
        scatterChart(floatRainData, rainData[0])

    # arrays()
    charts()


main()
