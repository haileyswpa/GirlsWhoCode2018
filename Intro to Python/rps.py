########### Starter code for Rock Paper Scissors ############

# Import the module (aka library) random
import random


def  rps():
    while True:
        # Create a list of possible moves in rock paper scissors
        gestures = ["rock", "paper", "scissors"]
        # Allow the computer to make a random selection on the move
        computer = random.choice(gestures)
        human = ["rock", "paper", "scissors"]
        # Take in user input for rock, paper, or scissors
        # BE SURE TO PROCESS INPUT (valid inputs allowed ONLY)
        answer = input("rock, paper, or scissors? \n")
        if answer not in human:
            print("Sorry that's not a valid response")
        else:
        # Show the human player what the computer decided on
            print("Computer chooses {}".format(computer.upper()))

        # Determine who wins
        # when would there be a tie?
        if computer == answer:
            print("It's a tie!")

        # when does the computer win?
        if (answer == "rock") and (computer == "paper"):
            print("I win!")
        if (answer == "paper") and (computer == "scissors"):
            print("I win!")
        if (answer == "scissors") and (computer == "rock"):
            print("I win!")

        # when does the human win?
        if (answer == "paper") and (computer == "rock"):
            print("You win!")
        if (answer == "scissors") and (computer == "paper"):
            print("You win!")
        if (answer == "rock") and (computer == "scissors"):
            print("You win!")
        ask = input("Do you want to play again? (y/n) \n")
        if ask != "y":
            break

rps()
