# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 12:44:18 2020
Prompts user for a student id.  Parses classes.txt for a list of classes
Checks each class listed for student ID
if Student ID is in class, display grade
@author: mbrothen
"""


def main():
    def getID():
        studentID = input("Enter a student id: ")
        openClasses(studentID)

    def openClasses(studentID):
        try:
            print("Student ID:\t" + studentID)
            classes = open(".\\Files\\classes.txt", "r")
            classLine = classes.readline()
            while classLine != "":
                classLine = classLine.rstrip()
                # print("Checking: " + classLine + " studen: " + studentID)
                checkClass(classLine, studentID)
                classLine = classes.readline()
        except IOError:
            print("Classes.txt not found!")
        except ValueError as exception:
            print("Error: " + str(exception))
        finally:
            classes.close()

    def checkClass(className, studentID):
        try:
            classFile = open(".\\Files\\" + className + ".txt", "r")
            studentLine = classFile.readline()
            while studentLine != "":
                currentStudent = studentLine.split()
                if currentStudent[0] == studentID:
                    print(className + ":\t" + str(currentStudent[1]))
                studentLine = classFile.readline()
        except IOError:
            print(className + ".txt not found!")
        except ValueError as exception:
            print("Error: " + str(exception))
        finally:
            classFile.close()

    getID()


main()
