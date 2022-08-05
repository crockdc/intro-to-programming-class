# Programmer:  Daniel Crocker
# Program Name: Temperature array / list(Assignment 11)
# Date Written: April 15, 2022
# Purpose: Demonstrate how to define, create and display an array with outdoor temperature readings

#============================================================================================================================================================================
# Import the custom functions module
from Crocker_Daniel__A11_myCustomFunctions import *

# define the size of the list/array, define the state
print("Please enter which state you will be entering temperature data for:")
state = input()
print("Please input how many days of weather temperature will be entered into this list:")
size = checkIntDataType()
# Check the integer data type via the checkIntDataType function

#============================================================================================================================================================================
# initialize variables
count = 0
fileName = ''
maxTemp = 0
minTemp = 0
outFile = ''
totalTemp = 0

#============================================================================================================================================================================
# Call function to create output file to store results
fileName, outFile = createOutputFile()


#============================================================================================================================================================================
# count is the lcv/index
wTemp = [0] * (size)

# for loop that iterates the number of days entered, adding each days temperature to the wTemp list while also accumulating the total temperature via the totalTemp variable
while count < size:
    print(f"Enter the temperature Fahrenheit in {state} for day #{count + 1}:")
    wTemp[count] = checkFloatDataType()
    
    # update lcv
    totalTemp = totalTemp + wTemp[count]
    count = count + 1

# calculate the average temp by dividing the total temp by the number of days
avgTemp = totalTemp / size

# obtain the max and min daily temperatures
maxTemp = max(wTemp)
minTemp = min(wTemp)

#============================================================================================================================================================================
# Unsorted list display heading
outFile.write("=" * 80 + "\n")
outFile.write(f'{"Unsorted Daily Temperature List for the State of " f"{state}" : ^80}')
outFile.write("=" * 80 + "\n")

# Reset array / list index back to 0
count = 0

# test lcv / index
# for loop that iterates through the wTemp list the number of days entered by the user and repeats the data in an organized output
while count < size:
    outFile.write(f'{"Day #" f"{count + 1}" ":" f"{wTemp[count]:6.2f}" "°F" : ^80}\n')
    
    # update lcv/index
    count = count + 1
outFile.write("=" * 80 + "\n")

# output statement displaying the min, max, and average temperature over the period of days in the state entered
outFile.write(f'{"The minimum temperature in " f"{state}" " over the " f"{size}" " day period was " f"{minTemp:6.2f}" "°F": ^80}\n')
outFile.write(f'{"The maximum temperature in " f"{state}" " over the " f"{size}" " day period was " f"{maxTemp:6.2f}" "°F": ^80}\n')
outFile.write(f'{"The average temperature in " f"{state}" " over the " f"{size}" " day period was " f"{avgTemp:6.2f}" "°F": ^80}\n')
outFile.write("=" * 80 + "\n")

#============================================================================================================================================================================
# Sort the list to prepare it for output display
wTemp.sort()

#============================================================================================================================================================================
# Sorted list display heading
outFile.write("=" * 80 + "\n")
outFile.write(f'{"Sorted Daily Temperature List for the State of " f"{state}" : ^80}')
outFile.write("=" * 80 + "\n")

# Reset array / list index back to 0
count = 0

# test lcv / index
# for loop that iterates through the wTemp list the number of days entered by the user and repeats the data in an organized output
while count < size:
    outFile.write(f'{"Day #" f"{count + 1}" ":" f"{wTemp[count]:6.2f}" "°F" : ^80}\n')
    
    # update lcv/index
    count = count + 1
outFile.write("=" * 80 + "\n")

# output statement displaying the min, max, and average temperature over the period of days in the state entered
outFile.write(f'{"The minimum temperature in " f"{state}" " over the " f"{size}" " day period was " f"{minTemp:6.2f}" "°F": ^80}\n')
outFile.write(f'{"The maximum temperature in " f"{state}" " over the " f"{size}" " day period was " f"{maxTemp:6.2f}" "°F": ^80}\n')
outFile.write(f'{"The average temperature in " f"{state}" " over the " f"{size}" " day period was " f"{avgTemp:6.2f}" "°F": ^80}\n')
outFile.write("=" * 80 + "\n")

#============================================================================================================================================================================
# Close the external file
outFile.close()

#============================================================================================================================================================================
# END PROGRAM
