# Import modules
import os
import csv
import time
import random
import tweepy
import player

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
    row = random.choice(list(csv.DictReader(csvfile)))
    po = player.player(
        row['Player Name'],
        row['Goals'],
        row['Games'],
        row['Starter'],
        row['Sub'],
        row['Active'],
        row['Debut']
        )
    api.update_status(status = f"#MssngVwlsRnd Name the #Chelsea player: {po.name.translate(stripped)} #CFC")
    time.sleep(10 * 60)
    api.update_status(status = f"#MssngVwlsRnd Well done if you got it, the answer was: {po.name} #CFC #Chelsea")
