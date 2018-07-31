list_of_responses = []
import json
import os

cont = True
while cont:

    survey = {
    "name" : "What is your name? \n",
    "birthday" : "What is your date of birth? (MM/DD/YYYY) \n",
    "age" : "What is your age? \n",
    "hours" : "How many hours per week do you spend on the phone? \n",
    "app" : "Name the app, program, or website that you use most frequently. \n",
    "movie" : "What's your favorite movie? \n",
    "restaurant" : "What's your favorite restaurant? \n",
    "store" : "What's your favorite online store? \n",
    "song" : "What's a song you really like? \n",
    "object" : "What's the most worth-it thing you have ever bought? \n"
    }

    response = {}

    for key, value in survey.items():
        response[key] = input(value)
    list_of_responses.append(response)
    print(list_of_responses)

    to_cont = input("Continue? Y/N (Don't press N unless you're the last person)\n")
    if to_cont == "N":
        print("Generating report...")
        cont = False
    else:
        cont = True

print(list_of_responses)

#turn data (list of responses) into a json object
with open("data.json", "w") as f:
    #write the json obect to our file
    f.write(json.dumps(list_of_responses))

# (this is all so that we can save the responses to a separate file, so that they stay saved even after ending this python program)

# this file can now be accessed by typing "more data.json" in the Command Prompt
