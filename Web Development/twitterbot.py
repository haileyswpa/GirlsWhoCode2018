# Imports
import tweepy
import random
import time

# Keys and Access Tokens
CONSUMER_KEY    = 'ugqLcMb0HPpz2Vkt3VEHJQRNZ'
CONSUMER_SECRET = 'M2Mqglr3NCjaA4uSNz2udugpJLgshOzlzcEOIU3le7dtaOMozh'

ACCESS_TOKEN    = '1017154984813588480-rMdIbDii3BBeITts3FoTLVQL71fZNh'
ACCESS_SECRET   = 'Te8jCAPjDunGWpsZXO33lPeZaGHbOeKQJRBojV3ZRZHkR'

tweets = ["hello", "hi", ":)", ":("]

# Authentication
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api  = tweepy.API(auth)

# Update Status
count = 0
while True:
    count += 1
    index = random.randint(0, len(tweets) - 1)
    api.update_status(tweets[index] + str(count)) #tweets a random tweet from the tweets list
    time.sleep(7)
