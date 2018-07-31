# Have a word / phrase
phrase = "girls who code"

# Keep track of user's guesses
guessed_letters = []
game_over = False

#Tell user how many spaces and letters they need to guess
display = " "
for letter in phrase:
    if letter in guessed_letters:
        display += letter
    # Processing the space in our phrase
    elif letter == " ":
        display += "  "
    # The letter in our phrase has not been guessed yet
    else:
        display += "_ "
print (display)

while game_over != True:
    # Allow user to give input to computer
    guess = input("Enter a letter: ")
    # Tell the user if they get the right letter
    if guess in phrase:
        print("You got a letter: {}".format(guess))
    # Tell the user if they get the wrong letter

    else:
        print("{} is not in the phrase.".format(guess))
    # Add the guess letter to our list of guessed letters
    guessed_letters.append(guess)

    #Tell user how many spaces and letters they need to guess
    display = " "
    for letter in phrase:
        if letter in guessed_letters:
            display += letter
        # Processing the space in our phrase
        elif letter == " ":
            display += "  "
        # The letter in our phrase has not been guessed yet
        else:
            display += "_ "
    print (display)

    if "_" in display:
        game_over = False
    else:
        game_over = True

print("END OF GAME")
# End the game if the user gets all the right letters in our word / phrase
