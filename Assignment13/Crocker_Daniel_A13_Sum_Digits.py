# Program Name: Creating Strings and Functions(Assignment #13)
# Programmer: Daniel Crocker
# Date: May 1, 2022
# Purpose: To manipulate a numerical string inputted by the user and produce an output sum of each individual integer
#====================================================================================================================
# Import myCustomFunctions module
from Crocker_Daniel__A13_myCustomFunctions import * 

# Declare and initialize variables
fileName = ''
intCount = 0
intString = ''
intTotal = 0
outFile = ''

def main():
    # Call the output file creation function to create an external file
    fileName, outFile = createOutputFile()
    
    #============================================================================================================================================================================
    # Call the string total function which takes a users numerical input and turns it into a string and performs calculations adding each integer at each index position
    intString, intCount, intTotal = stringTotal()
    
    #============================================================================================================================================================================
    # Call the sum function that adds each individual integer and writes their sum to the open file in an organized display
    writeSum(outFile, intString, intCount, intTotal)

    #============================================================================================================================================================================
    # Close the output file
    outFile.close()
    
    #============================================================================================================================================================================

#============================================================================================================================================================================
if __name__ == '__main__':
    main()
# END PROGRAM
