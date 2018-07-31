'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("tweets.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

tweets = [] # empty list/array

# Continue your program below!
for tweet in tweetData:
    tweets.append(tweet["text"]) # string of our twitter text
    giant_string = " ".join(tweets) # add a space between each tweet # use "join" (instead of "tweets.append" like above) so you can get rid of the commas and make it one giant string


# key = words, value = count/ frequency of the words appearance
list_of_words = giant_string.split() # splitting the giant string into individial words

# creating our data
# categorizing our data based on polarity
word_count = {}
for word in list_of_words:
    word = word.lower().rstrip().lstrip()
    if "http" in word:
        continue # if the word is a link, skip it
    if word[0] in {",", "?", ".", ":", "/", "!", '"', "#", "@", "'"}: # if the start of a word is one of these characters, get rid of the character so that it's just a word
        word = word[1:]
    if len(word) < 4: # if word is shorter than 4 letters, skip it
        continue
    if word[-1] in {",", "?", ".", ":", "/", "!", '"', "'"}: # if the last part of a word is one of these characters, get rid of the character so that it's just a word
        word = word[:-1]


#create a word frequency dictionary
    word_count[word] = word_count.get(word, 0) + 1 # if it does exist in the dictionary, +1  # if its the first time seeing it, default 0 and then +1

word_count_2 = {}
for word, count in word_count.items(): # new dictionary holding only the words with frequency 2 or greater
    if count < 2:
        continue
    else:
        word_count_2[word] = count
print(word_count_2)

wordcloud = WordCloud().generate_from_frequencies(word_count_2)
plt.imshow(wordcloud, interpolation = 'bilinear')
plt.show()
