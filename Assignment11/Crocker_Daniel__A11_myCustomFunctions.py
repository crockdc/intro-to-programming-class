# NAME: Daniel Crocker
# DESCRIPTION: My custom functions(used within the Temperature Array Assignment #11)

#============================================================================================================
# Define function to create the external file to store output
def createOutputFile():
    # Create an external data file using functions/methods such as open, write and close
    # to write results to an external output file
    fName = input("Enter the file name where you wish to write the output/results:\n")
    oFile = open(fName + ".txt", "w")
    return fName, oFile
    # End createOutputFile function

#============================================================================================================
# Function to check the data type and for positive input
def checkIntDataType():
    while True: # Loop is used to check the data type, negative values or values greater than 100000000
        try:
            intDataType = int(input())
        except ValueError:
            print("You entered the wrong data type\n" \
                  "Re-enter a positive whole number only:")
            continue
        else:
            if (intDataType < 0) or (intDataType > 100000):
                print("You entered a negative value or a value > 100,000\n" \
                      "Re-enter a positive whole number only:")
                continue
            else:
                break
            # end Try statement
        # end while True statement
    return intDataType
    # End checkIntDataType function

#============================================================================================================
# Function to check the data type and for positive input
def checkFloatDataType():
    while True: # Loop is used to check the data type, negative values or values greater than 100000000
        try:
            floatDataType = float(input())
        except ValueError:
            print("You entered the wrong data type\n" \
                  "Re-enter a positive value [decimals are acceptable]")
            continue
        else:
            if (floatDataType < 0) or (floatDataType > 999):
                print("You entered a negative value or a value > 999\n" \
                      "Re-enter a positive value [decimals are acceptable]")
                continue
            else:
                break
            # end Try statement
        # end while True statement
    return floatDataType
    # End checkFloatDataType function

#============================================================================================================

# End of module
