# NAME: Daniel Crocker
# DESCRIPTION: My custom functions(used within Maximum of Two Values and Feet To Inches programs

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
# MAXIMUM TWO VALUES FUNCTIONS:
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
            if (intDataType < 0) or (intDataType > 100000000):
                print("You entered a negative value or a value > 100,000,000\n" \
                      "Re-enter a positive whole number only:")
                continue
            else:
                break
            # end Try statement
        # end while True statement
    return intDataType
    # End checkIntDataType function

#============================================================================================================
# Define a function to compare two values
def findMax(v1, v2):
    if v1 <= v2:
        return v2
    else:
        return v1
    # End findMax function

#============================================================================================================
# Define a function to write the results and create a report
def writeResultsMax(val1, val2, max1, oFile):
    # REPORT HEADING AND COLUMN HEADINGS
    oFile.write("~" * 60 + "\n")
    oFile.write(f"{'MAXIMUM OF TWO VALUES':^60}\n")
    oFile.write("~" * 60 + "\n")
    # Display the conversion from feet to inches
    oFile.write(f"           The maximum of {val1:,} and {val2:,} is {max1:,}\n")
    oFile.write("~" * 60)
    # End of writeResultsMax function

#============================================================================================================
# FEET TO INCHES FUNCTIONS:
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
            if (floatDataType < 0) or (floatDataType > 100000000):
                print("You entered a negative value or a value > 100,000,000\n" \
                      "Re-enter a positive value [decimals are acceptable]")
                continue
            else:
                break
            # end Try statement
        # end while True statement
    return floatDataType
    # End checkFloatDataType function

#============================================================================================================
# Define a function to convert feet to inches
def calcFeetToInches(f1):
    in1 = f1 * 12
    return in1
    # End calcFeetToInches function

#============================================================================================================
# Define a function to write the results and create a report
def writeResultsFeet(f2, in2, oFile):
    # REPORT HEADING AND COLUMN HEADINGS
    oFile.write("~" * 60 + "\n")
    oFile.write(f"{'CONVERTING FEET TO INCHES':^60}\n")
    oFile.write("~" * 60 + "\n")

    # Display the conversion from feet to inches
    oFile.write(f"               {f2:,.2f} feet = {in2:,.2f} inches\n")
    oFile.write("~" * 60)
    # End of writeResultsFeet function

#============================================================================================================

# End of module
