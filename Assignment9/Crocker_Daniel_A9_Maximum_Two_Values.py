# PROGRAMMER: Daniel Crocker
# PROGRAM NAME: Maximum of Two Values
# DATE WRITTEN: April 2, 2022
# PURPOSE: Write a program that asks the user to enter two values, then returns the largest value of the two
#============================================================================================================

# Import customized functions from the module Crocker_Daniel_myCustomFunctions
from Crocker_Daniel_myCustomFunctions import *

# Define the main function
def main():
    # Declare variables in alphabetical order
    # Initialize variables used to store file names
    fileName = ''
    maximum = 0
    outFile = ''
    value1 = 0
    value2 = 0

    #========================================================================================================
    # Call function to create output file to store results
    fileName, outFile = createOutputFile()

    #========================================================================================================
    # Input Operations utilizing TRY/EXCEPT within WHILE loops
    print("Enter the first positive whole number:")
    value1 = checkIntDataType() # Call function to check data type and for negative values
    print("Enter the second positive whole number:")
    value2 = checkIntDataType() # Call function to check data type and for negative values        

    #========================================================================================================
    # Compare the two values using the findMax function
    maximum = findMax(value1, value2)

    #========================================================================================================
    # OUTPUT OPERATIONS(utilizing the writeResultsMax function)
    writeResultsMax(value1, value2, maximum, outFile)
    
    #========================================================================================================

    # Close the external file
    outFile.close()
    # End of main function
    #========================================================================================================


#============================================================================================================
# Call the main function as a standalone program
if __name__ == '__main__':
    main()
    
# END PROGRAM
