# import libraries
import json

file = open("tweets.json", "r")
data = json.load(file) # load from file into a json object

for d in data: # data is a list, d is a dictionary
    # loop through the dictionary (which corresponds to a single tweet)
    # for info_category, info in d.items():
    #     print(info_category, info)

    # d is our dictionary about our tweet
    print(d["retweet_count"])
        # each unser_mention is a dictionary
        # it corresponds

    break
