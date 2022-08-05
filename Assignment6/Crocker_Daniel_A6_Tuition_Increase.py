def toFixed(value, digits):
    return "%.*f" % (digits, value)

# PROGRAMMER:  Daniel Crocker
# PROGRAM:     Tuition Increase
# DATE WRITTEN: 3/5/2022
# PURPOSE: Use a FOR loop to calculate the projected semester tuition amount for a specified number of years.
# Declare variables
# Ask user how much the initial tuition is, what the annual percentage rate increase is, and for how many years.
print("What is the amount of the starting tuition?[Decimals may be entered]")
tuition = float(input())
print("What is the percentage of increase?[Enter in decimal format(i.e. for 3% type 0.03)]")
percentIncrease = float(input())
print("How many years are you projecting the tuition increase?[Enter whole numbers only]")
years = int(input())

# Display a header that organizes the data that follows into columns.
print("=" * 80)
print("PROJECTED TUITIONS(PER SEMESTER FOR FULL-TIME STUDENTS)")
print("=" * 80)
print("   YEAR                  PROJECTED TUITION")
print("=" * 80)

# Create a FOR loop utilizing the yearCount variable to keep track as the loop iterates from zero in steps of one, and reaching the value of the year variable.
for yearsCount in range(1, years + 1, 1):
    
    # As the FOR loop iterates, the tuition variable is recalculated utilizing the percentage variable. Each iteration
    tuition = tuition * percentIncrease + tuition
    print(f"    {yearsCount:2}                     ${tuition:11,.2f}")

# Maintaining the format of the header, create a closing statement that displays the annual percentage increase that the annual tuition rates were based off of.
print("=" * 80)
print(f"THESE PROJECTIONS REFLECT A {percentIncrease * 100:5.3f}% ANNUAL INCREASE")
print("=" * 80)
print("This program is complete - Edited by Daniel Crocker")

# End Program
