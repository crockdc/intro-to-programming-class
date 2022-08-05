# Programmer:  Daniel Crocker
# Program Name: Temperature array / list(Assignment 12)
# Date Written: April 27, 2022
# Purpose: Demonstrate how to define, create and display an array with outdoor temperature readings
# and create functions for all procedures.

#============================================================================================================================================================================
# Import the custom functions module
from Crocker_Daniel__A12_myCustomFunctions import *

# Define the main function
def main():
    # initialize variables
    fileName = ''
    maxTemp = 0
    minTemp = 0
    outFile = ''
    totalTemp = 0
    highTempDays = 0

    #============================================================================================================================================================================
    # Call function to create output file to store results
    fileName, outFile = createOutputFile()

    #============================================================================================================================================================================
    # define the size of the list/array, define the state
    print("Please enter which state you will be entering temperature data for:")
    state = input()
    print("Please input how many days of weather temperature will be entered into this list:")
    size = checkIntDataType()
    # Check the integer data type via the checkIntDataType function

    #============================================================================================================================================================================
    # Count is the lcv/index
    wTemp, totalTemp = tempList(size, state, totalTemp)

    #============================================================================================================================================================================
    # Calculate the average temp via the calculateAvg function
    avgTemp = calculateAvg(totalTemp, size)

    #============================================================================================================================================================================
    # Obtain the max and min daily temperatures via function tempExtremes
    maxTemp, minTemp = tempExtremes(wTemp)

    #============================================================================================================================================================================
    # Call on function to write the unsorted list display
    writeUnsorted(outFile, size, state, maxTemp, minTemp, avgTemp, wTemp)

    #============================================================================================================================================================================
    # Call on function to write the sorted list display
    writeSorted(outFile, size, state, maxTemp, minTemp, avgTemp, wTemp)

    #============================================================================================================================================================================
    # Call on function to write the temps >= 75°F and write the number of days this occurs
    writeHighTemps(outFile, size, wTemp)
    
    #============================================================================================================================================================================
    # Close the external file
    outFile.close()
    # End of main function
    #============================================================================================================================================================================

#============================================================================================================================================================================
if __name__ == '__main__':
    main()
# END PROGRAM
