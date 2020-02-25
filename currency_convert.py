
#Thomas Nguyen. February 2, 2018.


import re

#This program takes a CSV input and converts the specified data entries from USD to Euros or Vice Versa
#This function takes 4 input parameters: field, multiplier, inFile, outFile
#field = name of field in CSV that contains data to be converted
#multiplier = conversion rate multiplier (default is 1)
#inFile = CSV file name containing data
#outFile = CSV file to write converted data to; if none given, use stdout
def currency_convert(field=None, multiplier=1, inFile=None, outFile=None):

    #Case where no field specified. No conversion to be done.
    if (field == None):
            print("ERROR: No conversion field specified. Conversion was not successful.\n")
            return

    #determine if USD-->Euro or Euro-->USD
    conversionType = (int)(input("Specify currency conversion (enter the digit)   [0] USD to EUR, [1] EUR to USD: "))
    while (conversionType < 0 or conversionType > 1):
        conversionType = (int)(input("Sorry, please enter a valid choice (enter the digit)   [0] USD to EUR, [1] EUR to USD: "))

    #explicitly define variables to be used throughout program
    index = (int)(-1)
    csvList = []

    #Case where given input .csv file
    #open .csv file, find index number of given field
    if (inFile != "none"):

        with open(inFile, 'r') as _inFile:

            #turn csv file into a list of lists called csvList
            csvList = [i for i in _inFile.readlines()]

            #find index number of given field by iterating through first row of .csv
            index = findIndex(csvList, field, 1)

            # Case where specified field name does not exist
            if (index == -1):
                print("ERROR: Specified field name not found. Conversion was not successful.\n")
                return

            #apply the currency conversion to the data given using multiplier specified
            applyConversion(csvList, index, multiplier, conversionType, 1)

            # write new data to outFile
            writeData(outFile, csvList, 1)

        #end of program
        return

    #case where not given .csv file
    else:

        #get user input from terminal
        inUser = input("\nInput data to be converted in .csv format below (by typing in values separated using commas), one row at a time (no leading/trailing whitespaces):\n[input 'DONE' when entries completed]\n")
        csvList.append((str)(inUser).split(','))
        while (inUser != "DONE"):
            inUser = input()
            if (inUser!= "DONE"):
                csvList.append((str)(inUser).split(','))

        index = findIndex(csvList, field, 0)

        if (index == -1):
            print("ERROR: Specified field name not found. Conversion was not successful.\n")
            return

        applyConversion(csvList, index, multiplier, conversionType, 0)

        writeData(outFile, csvList, 0)

        return




#This function returns the index value of the given field, which will be used to find all values needed to be converted
def findIndex(csvList, field, fromFile):
    if (fromFile == 1):
        headers = csvList[0].split(',')
    else:
        headers = csvList[0]

    for count, i in enumerate(headers):
        if (i == field):
            break

    return count


#this function applies the currency conversion to the data given
def applyConversion(csvList, index, multiplier, conversionType, fromFile):

    # iterate through rest of list and apply multiplier to each entry of 'index' value
    for row, i in enumerate(csvList):

        # split row into a list for easier managing
        if (fromFile == 1):
            csvList[row] = csvList[row].split(',')
        else:
            csvList[row] = csvList[row]

        data = csvList[row]

        # apply multiplier at appropriate cells
        for col, j in enumerate(data):

            if (row > 0 and col == index):

                data[col] = stripSymbols(data[col])
                data[col] = (float)(data[col]) * multiplier
                # convert cell data back to string and add symbol
                if (conversionType == 0):
                    data[col] = (str)("€" + (str)(data[col]))
                else:
                    data[col] = (str)("$" + (str)(data[col]))

    return


#this function writes the updated values to the specified output .csv file (or stdout if not given)
def writeData(outFile, csvList, fromFile):

    # if .csv outFile given
    if (outFile != "none"):

        with open(outFile, 'w') as _outFile:

            # iterate through rows
            for row, i in enumerate(csvList):
                # format string to remove unwanted symbols
                outputString = (str)(csvList[row]).replace('[', '')
                outputString = (str)(csvList[row]).replace(']', '')
                outputString = (str)(csvList[row]).replace('\'', '')
                if (fromFile == 1):
                    outputString = outputString[1:-3]
                else:
                    outputString = outputString[1:-1]
                _outFile.write(outputString + '\n')

    # no .csv outFile given
    else:

        print("\nUPDATED CSV:\n")
        # iterate through rows
        for row, i in enumerate(csvList):
            # format string to remove unwanted symbols
            outputString = (str)(csvList[row]).replace('[', '')
            outputString = (str)(csvList[row]).replace(']', '')
            outputString = (str)(csvList[row]).replace('\'', '')
            if (fromFile == 1):
                outputString = outputString[1:-3]
            else:
                outputString = outputString[1:-1]
            print(outputString)

    return


#this function removes non-numeric symbols from the data in the specified cells
def stripSymbols(data):

    _data = re.sub('[^0-9,.]', '', data)
    return (_data)




#MAIN
_field = input("currency_convert \n\tField Name: ")
_multiplier = input("\tMultiplier: ")
_inputFile = input("\tInput File: ")
_outputFile = input("\tOutput File: ")
currency_convert((str)(_field), (int)(_multiplier), (str)(_inputFile), (str)(_outputFile))