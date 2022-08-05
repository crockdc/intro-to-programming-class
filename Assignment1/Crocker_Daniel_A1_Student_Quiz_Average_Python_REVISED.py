def toFixed(value, digits):
    return "%.*f" % (digits, value)

# PROGRAMMER: Daniel Crocker
# PROGRAM NAME: Quiz Average
# DATE WRITTEN: January 24, 2022
# PURPOSE: Use Input, Assignment, Output statements to calculate the average of 5 quizzes for 5 different students.
# Declare variables in alphabetical order
# Initialize variables used to store calculations or results
average = 0.0
total = 0.0

# Input Operations
print("Enter the name of Student #1")
name1 = input()
print("Enter quiz #1 results for " + name1)
quiz1 = float(input())
print("Enter the name of Student #2")
name2 = input()
print("Enter quiz #2 results for " + name2)
quiz2 = float(input())
print("Enter the name of Student #3")
name3 = input()
print("Enter quiz #3 results for " + name3)
quiz3 = float(input())
print("Enter the name of Student #4")
name4 = input()
print("Enter quiz #4 results for " + name4)
quiz4 = float(input())
print("Enter the name of Student #5")
name5 = input()
print("Enter quiz #5 results for " + name5)
quiz5 = float(input())

# Calculate the total of the quizzes
total = quiz1 + quiz2 + quiz3 + quiz4 + quiz5

# Calculate the average of the quizzes
average = total / 5

# Output operations
# Report heading and column headings
print("=" * 60)
print(format("STUDENT QUIZZES", "^60s"))
print("=" * 60)
print("STUDENT NAME                                    QUZZES")
print("=" * 60)

# Student names and quiz grades
print(format(name1, "25s") + "                      " + format(quiz1,"6.2f"))
print(format(name2, "25s") + "                      " + format(quiz2,"6.2f"))
print(format(name3, "25s") + "                      " + format(quiz3,"6.2f"))
print(format(name4, "25s") + "                      " + format(quiz4,"6.2f"))
print(format(name5, "25s") + "                      " + format(quiz5,"6.2f"))
print("=" * 60)

# Total / sum of Quizzes
print(format("Total of the quizzes = ", "25s") + format(total,"6.2f"))
print("=" * 60)

# Quiz Average
print(format("QUIZ AVERAGE = ", "25s") + format(average,"6.2f") + "%")
print("=" * 60)

# END PROGRAM
