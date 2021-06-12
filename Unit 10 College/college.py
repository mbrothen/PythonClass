# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 19:21:21 2020
Tests the  person, student and instructor objects
@author: mbrothen
"""


from person import Person
from student import Student
from instructor import Instructor


def main():

    def makeStudent():
        student = Student("Matt", 1985, "Web Software Development")
        print("Student: " + student.getName())
        print("Year of Birth: " + str(student.getYearOfBirth()))
        print("College Major: " + student.getMajor())

    def makeInstructor():
        instructor = Instructor("Mike", 1999, 80000)
        print("Instructor: " + instructor.getName())
        print("Year of Birth: " + str(instructor.getYearOfBirth()))
        print("Salary: " + str(instructor.getSalary()))

    def makePerson():
        person = Person("Tom", 1919)
        print("Person: " + person.getName())
        print("Year of Birth: " + str(person.getYearOfBirth()))

    makeStudent()
    makeInstructor()
    makePerson()


main()
