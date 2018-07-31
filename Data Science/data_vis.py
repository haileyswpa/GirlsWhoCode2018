'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("tweets.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

polarity_values = []

for tweet in tweetData:
    tweet_text = tweet["text"]
    tb = TextBlob(tweet_text)
    print("{}: {}".format(tweet_text, tb.polarity))
    # break makes it stop after the first tweet instead of looping through all of them. right now it's commented bc we want it to loop completely through
    #break
    polarity_values.append(tb.polarity)

bins = [-1, - 0.5, 0, 0.5, 1] # 4 bins  # bins can be used to specify the values wanted in graph, you would have to put "polarity_values, bins" inside the () on line 29

# create a histogram
plt.hist(polarity_values)
plt.title("Tweet Polarity") # add a title to the histogram
plt.ylabel("Count of Tweets") # label for y-axis
plt.xlabel("Polarity") # label for x-axis
plt.grid() # shows a grid
plt.show() # show the histogram



# Continue your program below!

# Textblob sample:
# while True:
#     phrase = input("Enter a phrase: ")
#     tb = TextBlob(phrase)
#     print(tb.polarity)
