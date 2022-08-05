#-------------------------------------------------------------------------------------------
# PROGRAMMER:       Prof. Parham
# PROGRAM NAME:     Creating double Diamond shapes
# DATE WRITTEN:     enter current date
# PURPOSE:          Design double diamonds and write text inside each diamond
#-------------------------------------------------------------------------------------------
import turtle; # make the turtle graphics system available in Python

turtle.shape("turtle");         # changes the default cursor from shrevron to
                                # circle shape (turtle, square, arrow, circle)

turtle.speed(10);               # changes drawing speed
turtle.bgcolor("powder blue");  # change color
turtle.pensize(5);              # change the width of the pen / line to 5
turtle.pencolor("green");       # change pen / line color

turtle.fillcolor("red");        # fill color of object
turtle.begin_fill();
#-------------------------------------------------------------------------------------------
# Draw 1st simple Diamond
turtle.left(-45);               # -45 degree angle change
turtle.forward(250);            # draw line which is 250 pixels long
turtle.left(90);                # turns cursor 90 degrees left
turtle.forward(250);            # draw line which is 250 pixels long
turtle.left(90);                # turns cursor 90 degrees left
turtle.forward(250);            # draw line which is 250 pixels long
turtle.left(90);                # turns cursor 90 degrees left
turtle.forward(250);            # draw line which is 250 pixels long
#-------------------------------------------------------------------------------------------
# Draw 2nd Diamond              
turtle.forward(250);            # draw line which is 250 pixels long
turtle.right(90);                # turns cursor 90 degrees left
turtle.forward(250);            # draw line which is 250 pixels long
turtle.right(90);                # turns cursor 90 degrees left
turtle.forward(250);            # draw line which is 250 pixels long
turtle.right(90);                # turns cursor 90 degrees left
turtle.forward(250);            # draw line which is 250 pixels long

turtle.hideturtle();            # hides the cursor

turtle.end_fill();              # completes the fill color process

#-------------------------------------------------------------------------------------------
# display text "DIAMOND" in left Diamond shape
turtle.penup();                 # pen moves up
turtle.goto(-235, -20);         # moves the pen to positions -235 for x axis, -20 for y axis
turtle.pencolor("lavender blush");
turtle.write("DIAMOND", font = ("Times New Romans", "25", "bold"))
#-------------------------------------------------------------------------------------------
# display text "DIAMOND" in right Diamond shape 
turtle.penup();                 # pen moves up
turtle.goto(110, -20);          # moves the pen to positions 110 for x axis, -20 for y axis
turtle.pencolor("white");
turtle.write("DIAMOND", font = ("Times New Romans", "25", "bold"))

turtle.done();
#-------------------------------------------------------------------------------------------
# END PROGRAM
