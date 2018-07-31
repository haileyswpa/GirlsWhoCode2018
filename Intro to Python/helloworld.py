number = 15

guess = int(input("What number is it? "))
for tries in range(1,3):
    if guess == number:
        break
    elif number > guess:
        guess = int(input("Guess higher: "))
    else:
        guess = int(input("Guess lower: "))
print("The number is {}".format(number))
