#==============================================================================
# PROGRAMMER:      Daniel Crocker
# PROGRAM NAME:    Assignment #2 Turtle Graphics-Olympic Rings
# DATE WRITTEN:    January 31, 2022
#
# PURPOSE: This program will utilize Python turtle to draw the Olympic rings
#==============================================================================

import turtle;

# Set the background color.
turtle.bgcolor('light blue');

# Change the speed of the turtle.
turtle.speed(2);

# Turtle cursor shape and size.
turtle.shape("turtle");
turtle.pensize(20);

# Show turtle cursor.
turtle.showturtle();

# Lift the pen, move to the top center of the screen and write the title.
turtle.penup();
turtle.goto(0, 150)
turtle.write("Olympic Rings", align='center', font=("comic sans ms", 70, "bold"));

# Draw the first circle.
turtle.color("blue");
turtle.penup();
turtle.goto(-180, -40);
turtle.pendown();
turtle.circle(70);
turtle.penup();

# Draw the following circles by adjusting the location of the turtle.
turtle.color("red");
turtle.penup();
turtle.goto(180, -40);
turtle.pendown();
turtle.circle(70);
turtle.penup();

turtle.color("yellow");
turtle.penup();
turtle.goto(-90, -130);
turtle.pendown();
turtle.circle(70);
turtle.penup();

turtle.color("green");
turtle.penup();
turtle.goto(90, -130);
turtle.pendown();
turtle.circle(70);
turtle.penup();

turtle.color("black");
turtle.penup();
turtle.goto(0, -40);
turtle.pendown();
turtle.circle(70);
turtle.penup();

# Hide the turtle.
turtle.hideturtle();

# Keep program open if not using Python IDLE.
turtle.done();

# End Program.
