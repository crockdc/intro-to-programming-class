# PROGRAM NAME: Assignment #15 Graphic House Design FUNCTIONS
# PROGRAM DESCRIPTION: Design a house and call on functions by importing a module
# PROGRAMMER: Daniel Crocker
# DATE: 5/7/2022

#============================================================================================================
# Import myCustomFunctions and Turtle modules
from Crocker_Daniel_A15_myCustomFunctions import *
from turtle import *

#============================================================================================================
def main():
    # Set the turtle cursor speed
    speed(0)

    # Call the drawSky function which draws the sky color, the sun, and the clouds
    drawSky()

    # Call the drawScenery function which draws the trees, the shrubs, flowers, and person
    drawScenery()

    # Call the drawHouse function which draws the house, windows, chimney, door, sidewalk
    drawHouse()

    hideturtle() # Hides the turtle
#============================================================================================================
# Call on main function
if __name__ == "__main__":
    main()

#============================================================================================================  
# PROGRAM COMPLETE
# End Program



