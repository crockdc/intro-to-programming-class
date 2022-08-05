import random

random.seed()   #Prepare random number generator

# PROGRAMMER:  Daniel Crocker
# PROGRAM:     Guess the number
# DATE WRITTEN: 2/24/2022
# PURPOSE: USE WHILE LOOP TO GUESS A NUMBER with a built in RANDOM NUMBER GENERATOR function

# Variable to keep track if user wants to play game again
# Variable initially set to "y" to continue through the first while loop which is used later in program
again = "y"

# Initially the again variable is set to "y" which makes the loop true. Later the user will choose whether to keep playing and will utilize this loop.
while again == "y" or again == "Y":
    
    # count is initally set to 0
    count = 0
    
    # Call the Random function that will select a random number between 0 and 100 inclusive
    number = int(random.random() * 101)
    
    # Output statement to provide directions to user
    print("Guess a magic number between 0 and 100 ")
    
    # guess will be initially set to -1
    guess = -1
    
    # While Loop to prompt the user to enter numbers continuously until it matches the randomly generated number.
    while guess != number:
        
        # prompt user to guess the number
        print("Enter your guess[positive whole values only]: ")
        guess = int(input())
        
        # count variable increases by 1 after each guess
        count = count + 1
        
        # nested if to analyze guessed value entered by user
        if guess == number:
            
            # Tells the user when they guess correctly and in how many attempts
            print("You guessed the correct number ==> " + str(guess) + ", in " + str(count) + " attempts.")
            
            # Tells the user whether they are a winner with 4 or less attempts, or better luck next time with greater than 4
            if count <= 4:
                print("Congratulations, you are a winner!")
            else:
                print("Unfortunately it took you more than 4 attempts to guess the correct number, better luck next time!")
            
            # Asks user if they would like to play again. Assigns string to the again variable
            print("Guess The Number Game again? [Type 'y' or 'Y' for yes, otherwise type 'no' to exit the program]")
            again = input()
        else:
            if guess > number:
                print("Your guess of " + str(guess) + " is too high")
            else:
                print("Your guess of " + str(guess) + " is too low")
        
        # end while loop
# Tells the user thank you for playing after the user chooses to exit
print("Thanks for playing the Guess The Number Game - Have a nice day!")
print("THIS PROGRAM IS COMPLETE - EDITED BY DANIEL CROCKER")

# END PROGRAM
