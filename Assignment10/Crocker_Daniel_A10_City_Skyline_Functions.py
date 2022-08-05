# PROGRAM NAME: Assignment #10 - CREATING TURTLE DESIGNS AND ORGANIZING AS FUNCTIONS
# PROGRAM DESCRIPTION: TURTLE GRAPHICS PROGRAM THAT DRAWS A CITY SKYLINE
# PROGRAMMER: Daniel Crocker
# DATE: 04/09/2022

# IMPORT THE TURTLE GRAPHICS MODULE
from turtle import *
# IMPORT THE RANDOM MODULE
from random import *

# DEFINE THE MAIN FUNCTION
def main():
    speed(0) # SET THE SPEED OF THE TURTLE DRAWING(0 IS THE FASTEST)

    # CALL THE FOUR FUNCTIONS IN PROPER ORDER
    setup_Screen()
    draw_Stars()
    draw_Building()
    draw_Window()
    hideturtle() # Hides the turtle
    
#=========================================================================================================
# DEFINE THE FUNCTION THAT SETS THE BACKGROUND COLOR
def setup_Screen():
    bgcolor("grey") # SETS THE BACKGROUND COLOR OF THE ENTIRE SCREEN
    penup()
    goto(-2000, -100)
    pendown()
    color("black") # SETS THE COLOR OF THE LINE AND THE FILL COLOR ONCE THE SHAPE IS FINISHED BEING DRAWN
    begin_fill()
    for i in range(2): #FOR LOOP to create a square
        forward(3000)
        left(90)
        forward(800)
        left(90)
        forward(3000)
        end_fill()
        
    return

#=========================================================================================================
# DEFINE THE FUNCTION THAT RANDOMLY DRAWS THE STARS IN THE SKY
def draw_Stars():
    pensize(5)
    color("white")
    penup()
    for i in range(50): # GO TO A RANDOM LOCATION IN THE SKY PORTION AND PRODUCE A DOT FOR 50 TIMES
        goto(randint(-1000, 1000), randint(-95, 700))
        dot()
        
    return

#=========================================================================================================        
# DEFINE THE FUNCTION THAT DRAWS THE BUILDINGS OF THE CITY SKYLINE
def draw_Building():
    goto(-800, -100) # SENDS TURTLE CURSOR TO SPECIFIC LOCATION
    color("grey") # SETS THE COLOR OF THE LINES AND THE FILL COLOR ONCE BUILDINGS ARE DRAWN
    pendown()
    begin_fill()
    for i in range(3): # REPEAT THE BUILDING OUTLINE THREE TIMES THEN FILL THE COLOR
        left(90)
        forward(175)
        right(90)
        forward(100)
        left(90)
        forward(250)
        right(90)
        forward(150)
        right(90)
        forward(300)
        left(90)
        forward(100)
        left(90)
        forward(200)
        right(90)
        forward(100)
        right(90)
        forward(150)
        left(90)
        forward(100)
        right(90)
        forward(200)
        left(90)
    forward(1000)
    right(90)
    forward(300)
    right(90)
    forward(1400)
    end_fill()
    
    return

#=========================================================================================================
# DEFINE THE FUNCTION THAT DRAWS THE WINDOWS ON THE CITY BUILDINGS
def draw_Window():
    penup()
    color("white")
    goto(-780, 20)
    pendown()
    begin_fill()
    for i in range(4): # DRAW A SQUARE USING A FOR LOOP, REPEAT THIS FOR EVERY WINDOW AT DIFFERENT LOCATIONS
        forward(10)
        right(90)
    end_fill()
    penup()

    goto(-780, 50)
    pendown()
    begin_fill()
    for i in range(4):
        forward(10)
        right(90)
    end_fill()
    penup()

    goto(-720, 50)
    pendown()
    begin_fill()
    for i in range(4):
        forward(10)
        right(90)
    end_fill()
    penup()

    goto(-720, 20)
    pendown()
    begin_fill()
    for i in range(4):
        forward(10)
        right(90)
    end_fill()
    penup()

    goto(-680, 270)
    pendown()
    begin_fill()
    for i in range(4):
        forward(10)
        right(90)
    end_fill()
    penup()

    goto(-680, 300)
    pendown()
    begin_fill()
    for i in range(4):
        forward(10)
        right(90)
    end_fill()
    penup()

    goto(-650, 180)
    pendown()
    begin_fill()
    for i in range(4):
        forward(10)
        right(90)
    end_fill()
    penup()

    goto(-400, 180)
    pendown()
    begin_fill()
    for i in range(4):
        forward(10)
        right(90)
    end_fill()
    penup()

    goto(-400, 150)
    pendown()
    begin_fill()
    for i in range(4):
        forward(10)
        right(90)
    end_fill()
    penup()

    goto(-310, 50)
    pendown()
    begin_fill()
    for i in range(4):
        forward(10)
        right(90)
    end_fill()
    penup()

    goto(-340, 50)
    pendown()
    begin_fill()
    for i in range(4):
        forward(10)
        right(90)
    end_fill()
    penup()

    goto(-100, 150)
    pendown()
    begin_fill()
    for i in range(4):
        forward(10)
        right(90)
    end_fill()
    penup()

    goto(-70, 180)
    pendown()
    begin_fill()
    for i in range(4):
        forward(10)
        right(90)
    end_fill()
    penup()

    goto(-100, 210)
    pendown()
    begin_fill()
    for i in range(4):
        forward(10)
        right(90)
    end_fill()
    penup()

    goto(-70, 270)
    pendown()
    begin_fill()
    for i in range(4):
        forward(10)
        right(90)
    end_fill()
    penup()

    goto(-40, 270)
    pendown()
    begin_fill()
    for i in range(4):
        forward(10)
        right(90)
    end_fill()
    penup()

    goto(160, 50)
    pendown()
    begin_fill()
    for i in range(4):
        forward(10)
        right(90)
    end_fill()
    penup()

    goto(190, 80)
    pendown()
    begin_fill()
    for i in range(4):
        forward(10)
        right(90)
    end_fill()
    penup()

    goto(190, 170)
    pendown()
    begin_fill()
    for i in range(4):
        forward(10)
        right(90)
    end_fill()
    penup()

    goto(250, 20)
    pendown()
    begin_fill()
    for i in range(4):
        forward(10)
        right(90)
    end_fill()
    penup()

    goto(430, 50)
    pendown()
    begin_fill()
    for i in range(4):
        forward(10)
        right(90)
    end_fill()
    penup()

    goto(430, 110)
    pendown()
    begin_fill()
    for i in range(4):
        forward(10)
        right(90)
    end_fill()
    penup()

    goto(460, 140)
    pendown()
    begin_fill()
    for i in range(4):
        forward(10)
        right(90)
    end_fill()
    penup()

    goto(460, 200)
    pendown()
    begin_fill()
    for i in range(4):
        forward(10)
        right(90)
    end_fill()
    penup()

    goto(490, 260)
    pendown()
    begin_fill()
    for i in range(4):
        forward(10)
        right(90)
    end_fill()
    penup()

    goto(520, 260)
    pendown()
    begin_fill()
    for i in range(4):
        forward(10)
        right(90)
    end_fill()
    penup()

    goto(720, 80)
    pendown()
    begin_fill()
    for i in range(4):
        forward(10)
        right(90)
    end_fill()
    penup()

    goto(690, 50)
    pendown()
    begin_fill()
    for i in range(4):
        forward(10)
        right(90)
    end_fill()
    penup()

    goto(780, -10)
    pendown()
    begin_fill()
    for i in range(4):
        forward(10)
        right(90)
    end_fill()
    penup()

    goto(810, -10)
    pendown()
    begin_fill()
    for i in range(4):
        forward(10)
        right(90)
    end_fill()
    penup()
    
    return

#=========================================================================================================
# CALL THE MAIN FUNCTION
if __name__ == "__main__":
    main()

# PROGRAM COMPLETE
# End Program



