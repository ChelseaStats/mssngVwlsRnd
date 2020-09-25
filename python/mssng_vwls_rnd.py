 # importing modules
"""
Build and Tweet
"""
import os
import csv
import time
import random
import tweepy

# secrets
consumer_key = os.getenv('c_key')
consumer_secret = os.getenv('c_secret')
access_token = os.getenv('a_token')
access_token_secret = os.getenv('a_secret')

# authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# functions
stripped = str.maketrans(dict.fromkeys('aeiouAEIOU -'))

# processing
with open('player_history.csv') as csvfile:
 reader = csv.DictReader(csvfile)
 row = random.choice(list(reader))
 answer = row['Player Name']
 question = (row['Player Name']).translate(stripped)
 api.update_status(status = "#MssngVwlsRnd Name the Chelsea player: " + question)
 time.sleep(10 * 60)
 api.update_status(status = "#MssngVwlsRnd Well done if you got it, the answer was: " + answer)
