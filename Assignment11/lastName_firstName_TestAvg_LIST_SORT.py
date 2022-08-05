#--------------------------------------------------------------------------------------------
# Programmer:  First & Last name
# Program Name: Creating the test Average array / list
# Date Written: March 25, 2020
# Purpose: Demonstrate how to define, create and display an array with test averages
# define the size or the list/array

#--------------------------------------------------------------------------------------------
print("How many test averages will be entered into this list?")
size = int(input())

# count is the lcv/index
testAvg = [0] * (size) # define and initialize testAvg list

# initialize lcv /index to 0
count = 0

# initialize processed variables
average = 0.0
total = 0.0
#--------------------------------------------------------------------------------------------
# Use WHILE LOOP to Create the Array / list "testAvg"
# test lcv / index
while count < size:
    print("Enter Test Average # " + format(count + 1, "2d") + ": ")
    testAvg[count] = float(input())
    
    # update lcv
    count = count + 1
    # end while loop to create list
    
#--------------------------------------------------------------------------------------------
# calculate total or sum of all the test averages in the list
total = sum(testAvg)

# calculate average of all the test averages in the list
average = total / size

#--------------------------------------------------------------------------------------------    
# display heading
print("~" * 50)
print(format("UNSORTED TEST AVERAGE LIST", "^50s"))
print("~" * 50)
print(" ")

#--------------------------------------------------------------------------------------------
# Reset array / list index back to 0
count = 0

# While loop to display the array
# test lcv / index
while count < size:
    print(" " *21 + format(testAvg[count], "6.2f"))
    
    # update lcv/index
    count = count + 1
    # end while loop to display unsorted list

print("~" * 50)
print(" ")

#--------------------------------------------------------------------------------------------
# Functions to find the minimum and maximum item(s) in the list
print("~" * 50)
print("The minimum test average in the list is  " + format(min(testAvg), "6.2f") + "%")
print("~" * 50)
print("The maximum test average in the list is  " + format(max(testAvg), "6.2f") + "%")
print("~" * 50)
print("Average of  test averages in the list is " + format(average, "6.2f") + "%")
print("~" * 50)

#--------------------------------------------------------------------------------------------
# Sort the list
testAvg.sort()
#--------------------------------------------------------------------------------------------
# display heading
print("~" * 50)
print(format("SORTED TEST AVERAGE LIST", "^50s"))
print("~" * 50)
print(" ")

#--------------------------------------------------------------------------------------------
# Reset array / list index back to 0
count = 0

# While loop to display the array
# test lcv / index
while count < size:
    print(" " *21 + format(testAvg[count], "6.2f"))
    
    # update lcv/index
    count = count + 1
    # end while loop to display unsorted list

print("~" * 50)
print(" ")

#--------------------------------------------------------------------------------------------
# Functions to find the minimum and maximum item(s) in the list
print("~" * 50)
print("The minimum test average in the list is  " + format(min(testAvg), "6.2f") + "%")
print("~" * 50)
print("The maximum test average in the list is  " + format(max(testAvg), "6.2f") + "%")
print("~" * 50)
print("Average of  test averages in the list is " + format(average, "6.2f") + "%")
print("~" * 50)
#--------------------------------------------------------------------------------------------
# Calculate average of test scores



# END PROGRAM












