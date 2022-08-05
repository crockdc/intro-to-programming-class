#===============================================================
# PROGRAMMER:   Prof. Parham
# PROGRAM NAME: Sample Turtle graphics
# DATE WRITTEN: 2/11/2019
#===============================================================
#PURPOSE:       Illustrate basic turtle graphics commands
#===============================================================
import turtle;

turtle.speed(1);        # change drawing speed
turtle.width(5);        # increase the width of the line
# change the line color
turtle.color("DarkGoldenrod1");
# fill the color of the design
turtle.fillcolor("cadetblue1");
turtle.begin_fill();

# Draw a square design
turtle.showturtle();    # shows turtle cursor
turtle.shape("turtle"); # changes shape of cursor
turtle.forward(200);    # moves cursor forward 100 pixels
turtle.left(90);        # changes direction of turtle 90 degrees
turtle.forward(200);    # moves cursor forward 100 pixels
turtle.left(90);        # changes direction of turtle 90 degrees
turtle.forward(200);    # moves cursor forward 100 pixels
turtle.left(90);        # changes direction of turtle 90 degrees
turtle.forward(200);    # moves cursor forward 100 pixels
turtle.hideturtle();    # hides the cursor 

turtle.end_fill();

#===============================================================
