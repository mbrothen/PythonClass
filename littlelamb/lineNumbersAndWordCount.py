# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 10:20:12 2020

This reads a text file then creates a new file with line numbers added to each
line.  It also counts the number of words, characters and lines

@author: mbrothen
"""

littleLamb = open("littlelamb.txt", "r")
output = open("output.txt", "w")
wordCount = 0
characterCount = 0
lineCount = 0

def main():

    def endProgram():
        # close both files
        littleLamb.close()
        output.close()

    def readFile():
        # process each line of file
        for line in littleLamb:
            global lineCount
            lineCount += 1
            countWords(line)
            countCharacters(line)
            createOutput(line)

        displayOutput()

    def countWords(line):
        # split the line along spaces, count words
        global wordCount
        words = line.split(" ")
        wordCount += len(words)

    def countCharacters(line):
        punctuation = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
        # remove spaces
        global characterCount
        # remove spaces
        characters = line.replace(" ", "")
        # remove punctuation
        for letter in characters:
            if letter in punctuation:
                characters = characters.replace(letter, "")

        characterCount += len(characters)

    def createOutput(line):
        # Add line to output file and append line number to line
        output.write("/* " + str(lineCount) + " */ " + line)

    def displayOutput():
        # display file information and call endProgram()
        print("Character Count: " + str(characterCount))
        print("Word Count: " + str(wordCount))
        print("Line Count: " + str(lineCount))
        endProgram()

    readFile()


main()
