# NAME: Daniel Crocker
# DESCRIPTION: My custom functions(used within the Sum Digits Assignment #13)

#============================================================================================================
# Define function to create the external file to store output
def createOutputFile():
    # Create an external data file using functions/methods such as open, write and close
    # to write results to an external output file
    fName = input("Enter the file name where you wish to write the output/results(Press ENTER):\n")
    oFile = open(fName + ".txt", "w")
    return fName, oFile
    # End createOutputFile function

#============================================================================================================
# Function that takes a users numerical input and turns it into a string and performs calculations adding each integer at each index position
def stringTotal():
    # Declare and initialize variables
    num = 0
    count = 0
    tot = 0
    ind = 0 # Index variable set to zero to iterate through the index position of the string
    num = int(input("Enter a sequence of numbers(i.e. 54372762) then press ENTER:\n"))
    strNum = str(num)
    
    # Iterate through the numbers as a string to return the total number of index positions
    for i in strNum:
        count += 1

    # Iterate through the string while adding each integer to the previous total to get a total sum  
    while ind < count:
        tot += int(strNum[ind])
        ind += 1

    # Return the string and two integers
    return strNum, count, tot
    # End stringTotal function
    
#============================================================================================================
# Function to write an organized display of data to the output file
def writeSum(oFile, strNum, count, tot):
    ind = 0 # Index variable set to zero to iterate through the index position of the string
    # Write the output in an organized manner using format function
    oFile.write("-" * 80 + "\n")
    oFile.write(f'{"There are " f"{count}" " different numbers in the string" : ^80}\n')
    oFile.write("-" * 80 + "\n")
    oFile.write(f'{"They are:" : ^80}\n')
    oFile.write("-" * 80 + "\n")

    # While loop which iterates through each index position and displays the corresponding number
    while ind < count:
        oFile.write(f'{strNum[ind]: ^80}\n')
        ind += 1

    oFile.write("-" * 80 + "\n")
    oFile.write(f'{"Sum of all digits entered = " f"{tot}": ^80}\n')
    oFile.write("-" * 80 + "\n")
    # End the writeSum function

#============================================================================================================

# End of module
