# Program Name: Creating Strings and Functions(Assignment #13)
# Programmer: Daniel Crocker
# Date: May 1, 2022
# Purpose: To manipulate a numerical string inputted by the user and produce an output sum of each individual integer

#====================================================================================================================
# Import myCustomFunctions module
from Crocker_Daniel_A15_myCustomFunctions import *

# Declare and initialize variables
fileName = ''
numberList = []
outFile = ''
total = 0

#====================================================================================================================
def main():
    # Call the checkExist function to see if the text file exists
    numFile = checkExist()

    # Call the numList function to read through the list of numbers and create a list within Python
    numberList, total = numList(numFile)
    
    # Call the output file creation function to create an external file
    fileName, outFile = createOutputFile()

    # Call the function that writes an unsorted list with a heading
    unsortedList(outFile, total, numberList)

    # Call the function that calculates the average of all the numbers in the file numbers.txt
    average = calcAvg(total, numberList)

    # Call the function that writes the statistics(max, min, avg)
    writeStats(outFile, average, numberList)
    
    # Call the function that sorts and writes the numbers list
    sortedList(outFile, total, numberList)

    # Again, call the function that writes the statistics(max, min, avg)
    writeStats(outFile, average, numberList)

    # Call the function that writes all values less than or equal to 69.99 and count the number of occurences
    writeRange1(outFile, total, numberList)

    # Call the function that writes all values between 70-94.99 and count the number of occurences
    writeRange2(outFile, total, numberList)

    # Call the function that writes all values between 95-110 and count the number of occurences
    writeRange3(outFile, total, numberList)

    # Call the function that writes all values greater than 110 and count the number of occurences
    writeRange4(outFile, total, numberList)

    #============================================================================================================================================================================
    # Close the output file and the read file
    numFile.close()
    outFile.close()
    
    #============================================================================================================================================================================
    # End of main function
    
#============================================================================================================================================================================
# Call the main function
if __name__ == '__main__':
    main()
# END PROGRAM
