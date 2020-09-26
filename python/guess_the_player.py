 # importing modules
"""
Build and Tweet
"""
import os
import csv
import time
import random
import tweepy
import datefinder
from datetime import datetime

# secrets
consumer_key = os.getenv('c_key')
consumer_secret = os.getenv('c_secret')
access_token = os.getenv('a_token')
access_token_secret = os.getenv('a_secret')

# authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
#methods
def get_goals_string(goals):
    if(goals > 1):
        output_goals = f"{goals} goals"
    elif(goals == 0):
        output_goals = "no goals"
    else:
        output_goals = "1 goal"
    return output_goals

def get_date_from_string(date):
    try:
        published_matches = list(datefinder.find_dates(date))
        if len(published_matches) > 0:
            date_string = published_matches[0].strftime("%-d %B %Y ")
        else:
            date_string = ""
    except KeyError:
        print(f"error with publishing {name}")
        date_string = ""
    return date_string

# processing
with open('player_history.csv') as csvfile:
 reader = csv.DictReader(csvfile)
 row = random.choice(list(reader))
 name = row['Player Name']
 apps = row['Games']
 goals = get_goals_string(int(row['Goals'] or 0))
 starts = row['Starter'] or 0
 subs = row['Sub'] or 0
 active = row['Active']
 debut = get_date_from_string(row['Debut'])

if(active == 1):
    api.update_status(status = f"#GuessThePlayer This player made his debut on {debut} making {apps} appearances so far, scoring {goals}.")
else:
    api.update_status(status = f"#GuessThePlayer This former blue made his debut on {debut} making a total of {apps} appearances, scoring {goals}.")

time.sleep(10 * 60)
api.update_status(status = f"#GuessThePlayer Well done if you got it, the answer was: {name}")
