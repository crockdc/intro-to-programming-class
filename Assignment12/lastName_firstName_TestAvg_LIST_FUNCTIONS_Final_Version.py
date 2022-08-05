# Programmer:  First & Last name
# Program Name: Creating the name array / list
# Date Written: March 25, 2020
# Purpose: Demonstrate how to define, create and display an array with test averages
# define the number of items that will be stored inside the list/array;
# Create a variety of functions that can be reused in this program or any programs
#=================================================================================================================

# importing customized functions from the module lastname_firstname_myCustomFunctions
from myCustomFunctions import *

# Define the main program / module function
def main():
    
    #Initialize Variables
    average = 0.0
    fileName = ''
    outFile = ''
    #=============================================================================================================
    # Call function to create an output file to store results
    fileName, outFile = createOutputFile()  

    #=============================================================================================================
    print("How many test averages will be entered into this list? ")
    
    # Call checkIntDataType function
    numItems = checkIntDataType()

    #=============================================================================================================
    # count is the lcv/index
    # Declare the array/list testAvg
    testAvg = [0] * (numItems)   

    #=============================================================================================================
    # Call function to create a list for Test Average
    label = "Test Average # "
    createList(numItems, label, testAvg)
           
    #=============================================================================================================        
    # display heading
    outFile.write("=" *75 + "\n")
    outFile.write(f'{"UNSORTED TEST AVERAGE LIST":^75s}' + "\n" )
    outFile.write("=" *75 + "\n")
    outFile.write(" " + "\n")    

    # Call the function to write the list of Test averages
    writeList(numItems, testAvg, outFile)
    
    #=============================================================================================================
    # sort the list using the predefined method "sort"
    testAvg.sort()

    #=============================================================================================================
    # Call function to Calculate the test average
    average = calcAvg(testAvg)

    #=============================================================================================================

    # Call function to write Statistics for test Average list
    writeStats(average, testAvg, outFile)
    
    #=============================================================================================================
    # display heading
    outFile.write("=" *75 + "\n")
    outFile.write(f'{"SORTED TEST AVERAGE LIST":^75s}' + "\n")
    outFile.write("=" *75 + "\n")
    outFile.write(" " + "\n")

    # Call the function to write the list of Test averages
    writeList(numItems, testAvg, outFile)
    
    #=============================================================================================================
    # Call function to write Statistics for test Average list
    writeStats(average, testAvg, outFile)
     
    #=============================================================================================================

    # Close the external file
    outFile.close()
    # end main function
    #=============================================================================================================

#=================================================================================================================
# Call the main function as a standalone program
if __name__ == '__main__':
    main()
    
# END PROGRAM
