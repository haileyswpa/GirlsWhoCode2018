#TODO: import the random module since you  will need it in your game functions
import random

#TODO: define function guess_the_num
def number_game():
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


#TODO: define function rock_paper_scissors
def  rps():
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


#TODO: define function madlibs
def madlibs():
    # define function madlibs
    word = ["adjective",
            "adjective",
            "noun",
            "noun",
            "plural noun",
            "game",
            "plural noun",
            "'ing' verb",
            "'ing' verb",
            "plural noun",
            "'ing' verb",
            "noun",
            "plant",
            "part of body",
            "place",
            "'ing' verb",
            "adjective",
            "number",
            "plural noun"
            ]
    print("Let's play madlibs!")
    answer = []
# gather the input
    for element in word:
        a = input("type a(n) {} ".format(element))
        answer.append(a)
        print(a)

# output the finished madlib with the inputs you received
    print("""
    A vacation is when you take a trip to some """ + answer[0] + """ place
    with your """ + answer[1] + """ family. Usually you go to some place
    that is near a/an """ + answer[2] + """ or up on a/an """ + answer[3] + """.
    A good vacation place is one where you can ride """ + answer[4] + """
    or play """ + answer[5] + """ or go hunting for """ + answer[6] + """ . I like
    to spend my time """ + answer[7] + """ or """ + answer[8] + """.
    When parents go on a vacation, they spend their time eating
    three """ + answer[9] + """ a day, and fathers play golf, and mothers
    sit around """ + answer[10] + """. Last summer, my little brother
    fell in a/an """ + answer[11] + """ and got poison """ + answer[12] + """ all
    over his """ + answer[13] + """. My family is going to go to (the)
    """ + answer[14] + """, and I will practice """ + answer[15] + """. Parents
    need vacations more than kids because parents are always very
    """ + answer[16] + """ and because they have to work """ + answer[17] + """
    hours every day all year making enough """ + answer[18] + """ to pay
    for the vacation.
    """)

#TODO: define function riddle
# Didn't do this game

#TODO: define even or odd game
def evenorodd():
    computer_value = random.randint(1,10)
    print("{}".format(computer_value))
    user_input = input("Is this number even or odd? \n")
    if (computer_value % 2 == 0) and (user_input == "even"):
        print("You did it!")
    elif (computer_value % 2 == 0) and (user_input == "odd"):
        print("You're wrong!")
    elif (computer_value % 2 != 0) and (user_input == "odd"):
        print("You did it!")
    elif (computer_value % 2 != 0) and (user_input == "even"):
        print("You're wrong!")
