#Single Player Guessing Game
#This app allows a user to play against an AI to guess a number

#IMPORTS
import random

#VARIABLES
player_guess = -1
random_number = -1
player_lives = 2

print("Welcome to the Single Player Guessing Game!")
print("Guess a number between 1 and 1,000")
random_number = random.randint(1,1000)
print (random_number)
try:
    while True:
        if player_lives > 0:
            player_guess=int(input("Guess a number 1-1000"))
            print("lives left",player_lives)
            player_lives -= 1
            if player_guess == random_number:
                player_guess = int(input("->"))
                print("lives remaining", player_lives)
                print("YOU WIN!")
            elif player_guess > random_number:
                print("Guess Lower")
            elif player_guess < random_number:
                print("Guess Higher")
            else:
                print ("an error has occured")
        else:
            break
except:
    print("An error has occured")
print("Thanks for playing!")
print("The secret number was", random_number)