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

# processing
with open('player_history.csv') as csvfile:
 reader = csv.DictReader(csvfile)
 row = random.choice(list(reader))
 name = row['Player Name']
 apps = row['Games']
 goals = row['Goals']
 starts = row['Starter']
 subs = row['Sub']
 debut = row['Debut']
 active = row['Active']

if(active == 1):
    api.update_status(status = f"#GuessThePlayer This player made his debut on {debut} making {apps} appearances so far, scoring {goals} goal(s)")
else:
    api.update_status(status = f"#GuessThePlayer This former blue made his debut on {debut} making a total of {apps} appearances, scoring {goals} goal(s)")

time.sleep(10 * 60)
api.update_status(status = f"#GuessThePlayer Well done if you got it, the answer was: {name}")
