import random

def number_game():
    while True:
        number = random.randint(0,20)

        guess = int(input("I have chosen a number from 0 to 20. What number is it? "))
        for tries in range(1,3):
            if guess == number:
                break
            elif number > guess:
                guess = int(input("Guess higher: "))
            else:
                guess = int(input("Guess lower: "))
        print("The number is {}".format(number))

        ask = input("Do you want to play again? (y/n) \n")
        if ask != "y":
            break

number_game()
