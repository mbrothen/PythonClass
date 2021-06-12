# -*- coding: utf-8 -*-
'''
Retreive a text file from the internet, break it down into a dictionary
Allow user to search infromation in it
@author: mbrothen
'''

import urllib.request


def main():
    def getFile():
        try:
            list = []
            # Retreive text file from CIA Site
            fileLocation = "https://www.cia.gov/library/publications/the-world-factbook/rankorder/rawdata_2004.txt"
            data = urllib.request.urlopen(fileLocation)
            # Covert text to list
            for line in data:
                list.append(line)  # Create list of the text file
            return(list)
        except urllib.error.HTTPError as e:
            print("Url Error, unable to retreive list \n" +
                  str(e.reason))

    def processList(list):
        # Covert list to dictionary after trimming rank
        dataDict = {}
        for line in list:
            line = line.decode()
            data = line.split(' ', 1)  # Split line after first space
            data = data[1].split("$", 1)  # Split the rest at the $
            data[0] = data[0].strip()   # remove white space after country
            data[1] = data[1].strip()   # remove white space after dollar value
            # add country and capita to dict
            dataDict.update({data[0]: data[1]})
        return dataDict

    def getCountries(searchString):
        # Search finalist for substring in key and display results
        formatString = "{:50} {:} {:>7}"  # d after num
        print("-------------------------------------------------------------")
        print(formatString.format("Countries", "Per Capita", ""))
        print("-------------------------------------------------------------")
        # find all countries containing substring, output list
        for countries in finalList:
            if searchString.lower() in countries.lower():
                print(formatString.format(countries, "$",
                                          finalList[countries]))

    def getInput():
        # Receive user input.  End program if 'q'.  Ask again if not
        userInput = ""
        print("Retreive the per capita GDP of a country from the CIA World Fact Book")
        while userInput != 'q':
            userInput = input("Enter a country name (q=quite): ")
            if userInput != 'q':
                getCountries(userInput)

    rawList = getFile()
    finalList = processList(rawList)
    getInput()


main()
