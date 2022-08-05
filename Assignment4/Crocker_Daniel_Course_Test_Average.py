def toFixed(value, digits):
    return "%.*f" % (digits, value)

# PROGRAMMER:   Daniel Crocker
# PROGRAM NAME:  Course Test Average Program using a While Loop
# DATE WRITTEN:  February 10, 2022
# PURPOSE: DEMONSTRATE BASIC WHILE LOOP CONCEPT
# Declare variables in alpha order
# answer is the lcv
# Initialize variable(s) where calculated results are stored.
averageTestScore = 0.0
count = 0
totalTestScore = 0.0

# Main Column Heading
print('=' * 62)
print("CLASS TEST SCORE INFORMATION")
print('=' * 62)
print("STUDENT NAME                       TEST SCORE")
print('=' * 62)

# Initialize lcv "answer"
print("Do you wish to enter a student's name and test score? [type 'y' or 'Y' otherwise enter 'no'] ")
answer = input()

# Display a blank line
print(" ")

# While Loop
# testing the lcv To enter more than one student name and test score
while answer == "y" or answer == "Y":
    # Input Operations
    print("Enter the student's name ")
    studentName = input()
    print("What is the student's test score? ")
    testScore = float(input())
    
    # keep a running total of the test scores per student
    totalTestScore = totalTestScore + testScore
    
    # count or tally the number of students / tests
    count = count + 1
    
    # Output each student's name and their test score as a column
    print(f'{studentName:30s}{" ":5s}{testScore:6,.2f}{"%"}')
    
    # update lcv answer
    print("Do you wish to enter an additional student's name and test score? [type 'y' or 'Y' otherwise enter 'no'] ")
    answer = input()
    print(" ")
    
    # end while loop
# calculate the average test score
averageTestScore = totalTestScore / count

# Nested IF statements that separate into different ratings depending on the average test score of the class
if averageTestScore >= 90.00 and averageTestScore <= 100.00:
    rating = "EXCELLENT"
else:
    if averageTestScore < 90 and averageTestScore >= 80:
        rating = "GOOD"
    else:
        if averageTestScore < 80 and averageTestScore >= 70:
            rating = "SATISFACTORY"
        else:
            if averageTestScore < 70 and averageTestScore >= 60:
                rating = "MARGINAL"
            else:
                if averageTestScore < 60:
                    rating = "UNSATISFACTORY"

# Output operations
print('=' * 62)

# Displays the total of the student test scores
print(f'{"TOTAL TEST SCORES = ":30s}{" ":5s}{totalTestScore:6,.2f}')
print('=' * 62)

# Displays the average of the test scores of all students
print(f'{"THE CLASS AVERAGE = ":30s}{" ":5s}{averageTestScore:6,.2f}{"%"}')
print('=' * 62)

# Display the class average rating.
print(rating + " CLASS AVERAGE")
print('=' * 62)
print("THIS PROGRAM IS COMPLETE - EDITED BY DANIEL CROCKER")
print('=' * 62)

# END PROGRAM
