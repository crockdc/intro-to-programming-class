# PROGRAMMER: Daniel Crocker
# PROGRAM NAME: Feet To Inches
# DATE WRITTEN: April 2, 2022)
# PURPOSE: Write a program that asks the user to enter the number of feet, then converts feet to inches
#============================================================================================================

# Import customized functions from the module Crocker_Daniel_myCustomFunctions
from Crocker_Daniel_myCustomFunctions import *

# Define the main function
def main():
    # Declare variables in alphabetical order
    # Initialize variables used to store file names
    feet = 0.0
    fileName = ''
    outFile = ''

    #========================================================================================================
    # Call function to create output file to store results
    fileName, outFile = createOutputFile()

    #========================================================================================================
    # Input Operations utilizing TRY/EXCEPT within WHILE loops
    print("Enter the number of feet to be converted to inches [decimal is acceptable]:")
    feet = checkFloatDataType() # Call function to check data type and for negative values

    #========================================================================================================
    # Calculate the conversion of feet to inches using the calcFeetToInches function
    inches = calcFeetToInches(feet)

    #========================================================================================================
    # OUTPUT OPERATIONS(utilizing the writeResultsFeet function)
    writeResultsFeet(feet, inches, outFile)
    
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

