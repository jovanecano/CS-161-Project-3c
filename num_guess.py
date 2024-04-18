# Author: Jovane Cano
# GitHub Username: jovanecano
# Date: 04/17/2024
""" Description: This program prompts the user for an integer that the player will try to guess
If the player's guess is higher than the target integer, the program should dsiplay "too high." If the user's guess is lower
than the target integer, the program should display "too low." When the player guesses the number it will print the number of tries it took
If the player guesses it on the first try it will print "You guessed it in 1 try."
"""
target_num = int(input("Enter the integer for the player to guess.")) # asking the user to input the target integer

guess = None # initializing the guess var
number_of_tries = 0 # initializing the number of tries var


while guess != target_num: # a while loop that will continue until guess equals target_num
    guess = int(input("Enter your guess."))
    number_of_tries += 1 # augments 1 to number of tires
    if guess > target_num:
        print("Too high - try again:")
    elif guess < target_num:
        print("Too low - try again:")
    elif number_of_tries == 1 and guess == target_num:
        print("You guessed it in 1 try.")
    else:
        print(f"You guessed it in {number_of_tries} tries.")