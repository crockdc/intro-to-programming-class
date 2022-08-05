# Programmer:  First & Last name
# Program Name: Creating the test Average array / list
# Date Written: March 25, 2020
# Purpose: Demonstrate how to define, create and display an array with test averages
# define the size or the list/array
print("How many test averages will be entered into this list?")
size = int(input())

# count is the lcv/index
testAvg = [0] * (size) # define and initialize testAvg list

# initialize lcv /index to 0
count = 0

# Use WHILE LOOP to Create the Array / list "testAvg"
# test lcv / index
while count < size:
    print("Enter Test Average # " + format(count + 1, "2d") + ": ")
    testAvg[count] = float(input())
    
    # update lcv
    count = count + 1
# display heading
print("~" * 45)
print(format("UNSORTED TEST AVERAGE LIST", "^45s"))
print("~" * 45)
print(" ")

# Reset array / list index back to 0
count = 0

# While loop to display the array
# test lcv / index
while count < size:
    print(" " *19 + format(testAvg[count], "6.2f"))
    
    # update lcv/index
    count = count + 1
print("~" * 45)
print(" ")

# END PROGRAM
