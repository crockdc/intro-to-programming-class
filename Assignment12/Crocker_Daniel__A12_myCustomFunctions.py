# NAME: Daniel Crocker
# DESCRIPTION: My custom functions(used within the Temperature Array Assignment #12)

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
# Function to read and store data inside of list
def tempList(sz, st, tot):
    count = 0
    temps = [0] * (sz)

    # for loop that iterates the number of days entered, adding each days temperature to the wTemp list while also accumulating the total temperature via the totalTemp variable
    while count < sz:
        print(f"Enter the temperature Fahrenheit in {st} for day #{count + 1}:")
        temps[count] = checkFloatDataType()
        
        # update lcv
        tot = tot + temps[count]
        count = count + 1
    return temps, tot
    
#============================================================================================================
# Function to write an unsorted list of temperatures to the output file
def writeUnsorted(oFile, sz, st, mx, mn, av, tmp):
    # Unsorted list display heading
    oFile.write("=" * 80 + "\n")
    oFile.write(f'{"Unsorted Daily Temperature List for the State of " f"{st}" : ^80}')
    oFile.write("=" * 80 + "\n")

    # Reset array / list index back to 0
    count = 0

    # test lcv / index
    # while loop that iterates through the wTemp list the number of days entered by the user and repeats the data in an organized output
    while count < sz:
        oFile.write(f'{"Day #" f"{count + 1}" ":" f"{tmp[count]:6.2f}" "°F" : ^80}\n')
        
        # update lcv/index
        count = count + 1
    oFile.write("=" * 80 + "\n")

    # output statement displaying the min, max, and average temperature over the period of days in the state entered
    oFile.write(f'{"The minimum temperature in " f"{st}" " over the " f"{sz}" " day period was " f"{mn:6.2f}" "°F": ^80}\n')
    oFile.write(f'{"The maximum temperature in " f"{st}" " over the " f"{sz}" " day period was " f"{mx:6.2f}" "°F": ^80}\n')
    oFile.write(f'{"The average temperature in " f"{st}" " over the " f"{sz}" " day period was " f"{av:6.2f}" "°F": ^80}\n')
    oFile.write("=" * 80 + "\n")
    
#============================================================================================================
# Function to write a sorted list of temperatures to the output file
def writeSorted(oFile, sz, st, mx, mn, av, tmp):
    # Sort the list to prepare it for sorted list 
    tmp.sort()

    # Sorted list display heading
    oFile.write("=" * 80 + "\n")
    oFile.write(f'{"Sorted Daily Temperature List for the State of " f"{st}" : ^80}')
    oFile.write("=" * 80 + "\n")

    # Reset array / list index back to 0
    count = 0

    # test lcv / index
    # while loop that iterates through the wTemp list the number of days entered by the user and repeats the data in an organized output
    while count < sz:
        oFile.write(f'{"Day #" f"{count + 1}" ":" f"{tmp[count]:6.2f}" "°F" : ^80}\n')
        
        # update lcv/index
        count = count + 1
    oFile.write("=" * 80 + "\n")

    # output statement displaying the min, max, and average temperature over the period of days in the state entered
    oFile.write(f'{"The minimum temperature in " f"{st}" " over the " f"{sz}" " day period was " f"{mn:6.2f}" "°F": ^80}\n')
    oFile.write(f'{"The maximum temperature in " f"{st}" " over the " f"{sz}" " day period was " f"{mx:6.2f}" "°F": ^80}\n')
    oFile.write(f'{"The average temperature in " f"{st}" " over the " f"{sz}" " day period was " f"{av:6.2f}" "°F": ^80}\n')
    oFile.write("=" * 80 + "\n")

#============================================================================================================
# Function to calculate the average temperature
def calculateAvg(tot, sz):
    avg = tot / sz
    return avg

#============================================================================================================
# Function to calculate the max and min temperature
def tempExtremes(temp):
    maximum = max(temp)
    minimum = min(temp)
    return maximum, minimum

#============================================================================================================
# Function to write a list of all temperatures >= 75°F and display the total number of days >= 75°F
def writeHighTemps(oFile, sz, tmp):
    # High temp list display heading
    oFile.write("=" * 80 + "\n")
    oFile.write(f'{"Temperatures Greater Than or Equal To 75°F" : ^80}')
    oFile.write("=" * 80 + "\n")

    # Reset array / list index back to 0
    count = 0

    # Create accumulator variable to count the days >= 75°F
    hotDays = 0

    # test lcv / index
    # while loop that iterates through the wTemp list the temperatures of the days that were >= 75°F
    while count < sz:
        # If statement that checks to if the temp of a day is >= 75°F then writes it and adds 1 to the accumulator variable
        if tmp[count] >= 75:
            oFile.write(f'{"Day #" f"{count + 1}" ":" f"{tmp[count]:6.2f}" "°F" : ^80}\n')
            hotDays += 1
            count = count + 1
        else:
            count = count + 1

    # Output write statement displaying how many days the temperature was >= 75°F
    oFile.write("=" * 80 + "\n")
    oFile.write(f'{"Temperature(s) >= 75°F Occured " f"{hotDays}" " Time(s).": ^80}\n')
    oFile.write("=" * 80 + "\n")

#============================================================================================================

# End of module
