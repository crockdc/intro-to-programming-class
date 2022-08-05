# NAME: Daniel Crocker
# DESCRIPTION: My custom functions(used within the Final Project)

#============================================================================================================
# Import the turtle module
from turtle import *
# Import the os.path module to check if a file exists
from os.path import exists as file_exists

#============================================================================================================
# Define the function that counts the number of values listed and displays each that meets criteria
def writeRange1(oFile, tot, nList):
    # Initialize variables
    count = 0 # lcv
    tally = 0
    # Display heading
    oFile.write("=" * 80 + "\n")
    oFile.write(f'{"Values Less Than or Equal To 69.99" : ^80}')
    oFile.write("=" * 80 + "\n")
    # While loop with nested if statement that keeps a tally and displays criteria matching numbers
    while count < tot:
        if nList[count] <= 69.99:
            oFile.write(f'{f"{nList[count]: 6.2f}" : ^80}\n')
            count += 1
            tally += 1
        else:
            count += 1
    oFile.write("=" * 80 + "\n")
    oFile.write(f'{"There Are " f"{tally}" " Values Less Than or Equal To 69.99" : ^80}')
    oFile.write("=" * 80 + "\n")
# End of writeRange1 function
    
#============================================================================================================
# Define the function that counts the number of values listed and displays each that meets criteria
def writeRange3(oFile, tot, nList):
    # Initialize variables
    count = 0 # lcv
    tally = 0
    # Display heading
    oFile.write("=" * 80 + "\n")
    oFile.write(f'{"Values Between 95-110" : ^80}')
    oFile.write("=" * 80 + "\n")
    # While loop with nested if statement that keeps a tally and displays criteria matching numbers
    while count < tot:
        if nList[count] <= 110 and nList[count] >= 95:
            oFile.write(f'{f"{nList[count]: 6.2f}" : ^80}\n')
            count += 1
            tally += 1
        else:
            count += 1
    oFile.write("=" * 80 + "\n")
    oFile.write(f'{"There Are " f"{tally}" " Values Between 95-110" : ^80}')
    oFile.write("=" * 80 + "\n")
# End of writeRange3 function
    
#============================================================================================================
# Define the function that counts the number of values listed and displays each that meets criteria
def writeRange2(oFile, tot, nList):
    # Initialize variables
    count = 0 # lcv
    tally = 0
    # Display heading
    oFile.write("=" * 80 + "\n")
    oFile.write(f'{"Values Between 70-94.99" : ^80}')
    oFile.write("=" * 80 + "\n")
    # While loop with nested if statement that keeps a tally and displays criteria matching numbers
    while count < tot:
        if nList[count] <= 94.99 and nList[count] >= 70:
            oFile.write(f'{f"{nList[count]: 6.2f}" : ^80}\n')
            count += 1
            tally += 1
        else:
            count += 1
    oFile.write("=" * 80 + "\n")
    oFile.write(f'{"There Are " f"{tally}" " Values Between 70-94.99" : ^80}')
    oFile.write("=" * 80 + "\n")
# End of writeRange2 function
    
#============================================================================================================
# Define the function that counts the number of values listed and displays each that meets criteria
def writeRange4(oFile, tot, nList):
    # Initialize variables
    count = 0 # lcv
    tally = 0
    # Display heading
    oFile.write("=" * 80 + "\n")
    oFile.write(f'{"Values Greater Than 110" : ^80}')
    oFile.write("=" * 80 + "\n")
    # While loop with nested if statement that keeps a tally and displays criteria matching numbers
    while count < tot:
        if nList[count] > 110:
            oFile.write(f'{f"{nList[count]: 6.2f}" : ^80}\n')
            count += 1
            tally += 1
        else:
            count += 1
    oFile.write("=" * 80 + "\n")
    oFile.write(f'{"There Are " f"{tally}" " Values Greater Than 110" : ^80}')
    oFile.write("=" * 80 + "\n")
# End of writeRange4 function
    
#============================================================================================================
# Function to sort and write the sorted number list
def sortedList(oFile, tot, nList):
    count = 0 # lcv
    nList.sort() # sorts the list from least to greatest
    # Display heading
    oFile.write("=" * 80 + "\n")
    oFile.write(f'{"Sorted List of Numbers" : ^80}')
    oFile.write("=" * 80 + "\n")
    # While loop that iterates through the list and displays each number
    while count < tot:
        oFile.write(f'{f"{nList[count]: 6.2f}" : ^80}\n')
        count += 1
# End of sortedList function

#============================================================================================================
# Function to write the minimum, maximum, and average of the number list
def writeStats(oFile, avg, nList):
    oFile.write("=" * 80 + "\n")
    oFile.write(f'{"The minimum number is " f"{min(nList): 6.2f}": ^80}\n')
    oFile.write(f'{"The maximum number is " f"{max(nList): 6.2f}": ^80}\n')
    oFile.write(f'{"The average number is " f"{avg: 6.2f}": ^80}\n')
    oFile.write("=" * 80 + "\n")
# End of writeStats function

#============================================================================================================
# Function to calculate the average of all the numbers in the list
def calcAvg(tot, nList):
    count = 0 # lcv
    added = 0
    avg = 0
    # While loop that iterates through the list while adding each number to the added variable
    while count < tot:
        added += nList[count]
        count += 1
    # Formula for the average is the total divided by the number of elements in the list
    avg = added / tot
    return avg # Returns the average
# End of calcAvg function

#============================================================================================================
# Function to write an unsorted list of the numbers from numbers.txt
def unsortedList(oFile, tot, nList):
    count = 0
    # Unsorted list display heading
    oFile.write("=" * 80 + "\n")
    oFile.write(f'{"Unsorted List of Numbers" : ^80}')
    oFile.write("=" * 80 + "\n")

    while count < tot:
        oFile.write(f'{f"{nList[count]: 6.2f}" : ^80}\n')
        count += 1
# End of unsortedList function

#============================================================================================================
# Function to check if the numbers.txt file exists and if so, opens the file, otherwise displays that it cannot be found
def checkExist():
    if file_exists('numbers.txt'):
        num = open('numbers.txt', 'r')
        return num
    else:
        print("The file numbers.txt does not exist within the same directory as this .py file")
# End of checkExist function

#============================================================================================================
# Function that creates a Python float list using numbers within a current read file
def numList(numFile):
    # Initialize local variables
    floatList = []
    nList = numFile.readlines()
    stripList = []
    tot = 0
    # Remove the newline characters by replacing with a blank
    for i in nList:
        stripList.append(i.replace("\n", ""))
        tot += 1

    # Convert the stripList from strings to floats
    for i in stripList:
        floatList.append(float(i))

    return floatList, tot
# End of numList function
    
#============================================================================================================
def drawSky():
    drawBackground() # Call on the drawBackground function
    drawSun() # Call on the drawSun function
    drawClouds() # Call on the drawClouds function

#============================================================================================================
def drawHouse():
    drawOutline() # Call on the drawOutline function
    drawChimney() # Call on the drawChimney function
    drawWindows() # Call on the drawWindows function
    drawDoor() # Call on the drawDoor function
    drawSidewalk() # Call on the drawSidewalk function
    drawPerson() # Call on the drawPerson function

#============================================================================================================
def drawScenery():
    drawGrass() # Call on the drawGrass function
    drawTrees() # Call on the drawTrees function
    drawFlowers() # Call on the drawFlowers function

#============================================================================================================
def drawGrass():
    # Grass
    bgcolor("darkolivegreen")

#============================================================================================================
def drawTrees():
    # Tree 1
    penup()
    goto(300, -300)
    pendown()
    color("tan", "saddlebrown")
    setheading(90)
    begin_fill()
    forward(30)
    right(90)
    forward(30)
    right(90)
    forward(30)
    right(90)
    forward(30)
    end_fill()
    color("mediumspringgreen", "darkgreen")
    begin_fill()
    setheading(0)
    forward(60)
    left(115)
    forward(100)
    left(110)
    goto(270, -300)
    goto(300, -300)
    end_fill()

    # Tree 2
    penup()
    goto(240, -230)
    pendown()
    color("tan", "saddlebrown")
    setheading(0)
    begin_fill()
    forward(30)
    right(90)
    forward(30)
    right(90)
    forward(30)
    right(90)
    forward(30)
    end_fill()
    color("mediumspringgreen", "darkgreen")
    begin_fill()
    setheading(0)
    forward(60)
    left(115)
    forward(100)
    left(110)
    goto(210, -230)
    goto(240, -230)
    end_fill()

    # Tree 3
    penup()
    goto(-280, -300)
    pendown()
    color("tan", "saddlebrown")
    setheading(0)
    begin_fill()
    forward(30)
    right(90)
    forward(30)
    right(90)
    forward(30)
    right(90)
    forward(30)
    end_fill()
    color("mediumspringgreen", "darkgreen")
    begin_fill()
    setheading(0)
    forward(60)
    left(115)
    forward(100)
    left(110)
    goto(-310, -300)
    goto(-280, -300)
    end_fill()

    # Tree 4
    penup()
    goto(-220, -230)
    pendown()
    color("tan", "saddlebrown")
    setheading(0)
    begin_fill()
    forward(30)
    right(90)
    forward(30)
    right(90)
    forward(30)
    right(90)
    forward(30)
    end_fill()
    color("mediumspringgreen", "darkgreen")
    begin_fill()
    setheading(0)
    forward(60)
    left(115)
    forward(100)
    left(110)
    goto(-250, -230)
    goto(-220, -230)
    end_fill()
    setheading(0)

#============================================================================================================
def drawFlowers():
    # Flower 1
    penup()
    goto(-150, -100)
    color("chartreuse")
    pendown()
    left(90)
    pensize(5)
    forward(20)
    left(45)
    forward(20)
    penup()
    goto(-150, -100)
    pendown()
    setheading(90)
    forward(40)
    right(45)
    forward(25)
    penup()
    goto(-150, -100)
    pendown()
    setheading(90)
    forward(60)
    left(45)
    forward(30)
    penup()
    goto(-150, -40)
    pendown()
    setheading(90)
    forward(20)
    setheading(0)
    penup()
    forward(10)
    pendown()
    color("pink", "yellow")

    for i in range(8):  #FOR LOOP to create flower petals
        begin_fill()
        circle(10)
        end_fill()
        left(45)
        forward(15)

    # Flower 2
    penup()
    goto(140, -100)
    color("lime")
    pendown()
    left(90)
    pensize(5)
    forward(20)
    left(45)
    forward(20)
    penup()
    goto(140, -100)
    pendown()
    setheading(90)
    forward(40)
    right(45)
    forward(25)
    penup()
    goto(140, -100)
    pendown()
    setheading(90)
    forward(60)
    left(45)
    forward(30)
    penup()
    goto(140, -40)
    pendown()
    setheading(90)
    forward(20)
    setheading(0)
    penup()
    forward(10)
    pendown()
    color("magenta", "gold")

    for i in range(8): #FOR LOOP to create flower petals
        begin_fill()
        circle(10)
        end_fill()
        left(45)
        forward(15)

#============================================================================================================
def drawPerson():
    # Person
    penup()
    goto(0, -200)
    pendown()
    setheading(0)
    color("tan")
    begin_fill()
    circle(40)
    end_fill()
    penup()
    goto(-7, -150)
    dot(10, "skyblue")
    goto(7, -150)
    dot(10, "skyblue")
    goto(-10, -180)
    setheading(-60)
    color("crimson")
    pendown()

    for i in range(20): #FOR LOOP to create the smile
        forward(1)
        left(6)
        
    penup()
    goto(0, -200)
    setheading(-90)
    color("tan")
    pendown()
    pensize(5)
    forward(10)
    left(40)
    forward(20)
    right(20)
    forward(30)
    penup()
    goto(0, -210)
    setheading(-130)
    pendown()
    forward(10)
    left(20)
    forward(30)
    penup()
    goto(0, -210)
    setheading(-90)
    pendown()
    forward(30)
    left(10)
    forward(40)
    penup()
    goto(0, -250)
    pendown()
    right(10)
    forward(40)

#============================================================================================================
def drawOutline():
    # House
    setheading(0)
    penup()
    goto(-100, -100)
    pendown()
    pensize(3)
    color("turquoise", "steelblue") # (stroke, fill)
    begin_fill()

    for i in range(4): #FOR LOOP to create square
        forward(170)
        left(90)
    end_fill()

    # Roof
    penup()
    goto(-127, 70)
    pendown()
    begin_fill()

    for i in range(3): #FOR LOOP to create triangle
        forward(225)
        left(120)
    end_fill()

#============================================================================================================
def drawChimney():
    # Chimney
    penup()
    goto(20, 130)
    pendown()
    color("paleturquoise", "steelblue")
    begin_fill()

    for i in range(2): #FOR LOOP to create square
        forward(40)
        left(90)
        forward(100)
        left(90)
    end_fill()

    # Smoke
    penup()
    goto(35, 230)
    pendown()
    color("dimgray")

    for i in range(5): #FOR LOOP to create smoke circles
        begin_fill()
        circle(10)
        end_fill()
        penup()
        left(45)
        forward(20)
        right(45)
        pendown()
        begin_fill()
        circle(10)
        end_fill()
        penup()
        left(135)
        forward(20)
        right(135)
        pendown()


#============================================================================================================
def drawWindows():
    # Window 1
    penup()
    goto(0,0)
    pendown()
    color("peru", "white")
    begin_fill()

    for i in range(4): #FOR LOOP to create square
        forward(50)
        left(90)
    end_fill()

    # Window 1 Cross - Horizontal Line
    penup()
    goto(0, 25)
    pendown()
    color("peru")
    forward(50)

    # Window 1 Cross - Vertical Line
    penup()
    goto(25, 0)
    pendown()
    left(90)
    forward(50)

    # Window 2
    penup()
    goto(-80,0)
    pendown()
    right(90)
    color("peru", "white")
    begin_fill()

    for i in range(4): #FOR LOOP to create square
        forward(50)
        left(90)
    end_fill()

    # Window 2 Cross - Horizontal Line
    penup()
    goto(-80, 25)
    pendown()
    color("peru")
    forward(50)

    # Window 2 Cross - Vertical Line
    penup()
    goto(-55, 0)
    pendown()
    left(90)
    forward(50)

#============================================================================================================
def drawDoor():
    # Door
    penup()
    goto(-40, -97)
    pendown()
    right(90)
    color("wheat")
    begin_fill()

    for i in range(2): #FOR LOOP to create rectangle
        forward(50)
        left(90)
        forward(80)
        left(90)
    end_fill()

    # Door Handle
    penup()
    goto(-30, -60)
    pendown()
    color("peru")
    begin_fill()
    circle(5)
    end_fill()

#============================================================================================================
def drawSidewalk():
    # Sidewalk
    penup()
    goto(-40, -97)
    pendown()
    color("tan", "grey")
    begin_fill()
    right(95)
    forward(1000)
    left(95)
    forward(225)
    left(95)
    forward(1000)
    goto(-40, -97)
    end_fill()

#============================================================================================================
def drawBackground():
    # Draw the sky background
    penup()
    goto(-2000, -100)
    pendown()
    color("lavender")
    begin_fill()

    for i in range(2): #FOR LOOP to create a square
        forward(3000)
        left(90)
        forward(600)
        left(90)
    end_fill()

#============================================================================================================
def drawSun():
    # Sun
    penup()
    goto(-320, 225)
    pendown()
    color("sandybrown")
    begin_fill()
    circle(50)
    end_fill()

#============================================================================================================
def drawClouds():
    # Cloud 1
    setheading(0)
    penup()
    goto(200, 200)
    pendown()
    color("whitesmoke")

    for i in range(5): #FOR LOOP to create cloud circles
        begin_fill()
        circle(25)
        end_fill()
        penup()
        forward(30)
        pendown()

    # Cloud 2
    penup()
    goto(-100, 300)
    pendown()
    color("snow")

    for i in range(4):  #FOR LOOP to create cloud circles
        begin_fill()
        circle(30)
        end_fill()
        penup()
        forward(35)
        pendown()

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
