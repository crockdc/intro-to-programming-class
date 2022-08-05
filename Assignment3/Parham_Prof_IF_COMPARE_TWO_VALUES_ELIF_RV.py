# PROGRAMMER:  your first and last name
# PROGRAM NAME: Comparing two values USING Nested IF STATEMENTS
# DATE WRITTEN: 1/3/2020
# PURPOSE: Compare two real / float values using IF statements
# Declare all variables in alphabetical order
# Input operations
print("Enter the first numerical value [positive values only]> ")
number1 = float(input())
print("Enter the second numerical value [positive values only]> ")
number2 = float(input())

# Preliminary Output
print("=" * 75)
print(" The first value = " + format(number1, "12,.2f"))
print("The second value = " + format(number2, "12,.2f"))
print(" ")
print("=" * 75)

# Using Sequential IF statement to compare two values
if (number1 == number2):
    print("Value #1 --> " + format(number1, ",.2f") + " is equal to " \
          "Value #2 --> " + format(number2, ",.2f") + ".")
elif (number1 < number2):
    print("Value #1 --> " + format(number1, ",.2f") + " is less than " \
          "Value #2 --> " + format(number2, ",.2f") + ".")
else:
    print("Value #1 --> " + format(number1, ",.2f") + " is greater than " \
          "Value #2 --> " + format(number2, ",.2f") + ".")
    # end if statement
    
print("=" * 75)

# END PROGRAM
