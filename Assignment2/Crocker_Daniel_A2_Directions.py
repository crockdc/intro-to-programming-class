#==============================================================================
# PROGRAMMER:      Daniel Crocker
# PROGRAM NAME:    Assignment #2 Turtle Graphics-Directions
# DATE WRITTEN:    January 31, 2022
#
# PURPOSE: This program will utilize Python turtle to draw cardinal directions.
#==============================================================================

import turtle;

# Set the background color.
turtle.bgcolor('light pink');

# Change the speed of the turtle.
turtle.speed(2);

# Turtle cursor shape and size.
turtle.shape("turtle");
turtle.pensize(5);

# Show turtle cursor.
turtle.showturtle();

# Draw the first circle, choose a color, then fill in the shape with a color.
turtle.color("white");
turtle.penup();
turtle.goto(0, -70);
turtle.pendown();
turtle.fillcolor("light blue");
turtle.begin_fill();
turtle.circle(70);
turtle.end_fill();
turtle.penup();
turtle.home();

# Rotate the turtle 90 degrees, then draw a line and title it "north" at the end.

turtle.color("red");
turtle.pendown();
turtle.left(90);
turtle.forward(250);
turtle.write("NORTH", align='center', font=("comic sans ms", 20, "underline"));
turtle.penup();
turtle.home();

# Repeat the process of returning the turtle to the center and drawing the lines.

turtle.color("black");
turtle.pendown();
turtle.left(180);
turtle.forward(250);
turtle.penup();
turtle.goto(-295, -15);
turtle.write("WEST", align='center', font=("comic sans ms", 20, "underline"));
turtle.home();

turtle.color("purple");
turtle.pendown();
turtle.left(270);
turtle.forward(250);
turtle.penup();
turtle.goto(0, -280);
turtle.write("SOUTH", align='center', font=("comic sans ms", 20, "underline"));
turtle.home();

turtle.color("yellow");
turtle.pendown();
turtle.forward(250);
turtle.penup();
turtle.goto(295, -15);
turtle.write("EAST", align='center', font=("comic sans ms", 20, "underline"));
turtle.home();

# Hide the turtle.
turtle.hideturtle();

# Keep program open if not using Python IDLE.
turtle.done();

# End Program.
