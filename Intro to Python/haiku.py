#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Create the list of words you want to choose from.
aList = ["go outside", "she ate it", "this is good", "plant a seed", "really hot", "where is it?", "it is hot", "baseball bat", "hum a tune", "not a thing", "some big dogs"]
bList = ["come back right away", "right across the street", "it is all my fault", "give me some of it", "I have lost my keys", "She has a good job", "I will go with you", "I think you are right"]
#Generates a random integer.

response = input("Would you like a Haiku? (Y/N?)")
while response != "N":
    if response == "Y":
        aRandomIndex = randint(0, len(aList)-1)
        bRandomIndex = randint(0, len(bList)-1)
        cRandomIndex = randint(0, len(aList)-1)
        print(aList[aRandomIndex])
        print(bList[bRandomIndex])
        print(aList[cRandomIndex])
    else:
        print("{} is an invalid input.".format(response))
    response = input("Would you like a Haiku? (Y/N?)")
