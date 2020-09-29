# importing modules
import os
import csv
import time
import random
import tweepy
import player

# authentication
auth = tweepy.OAuthHandler(os.getenv('c_key'), os.getenv('c_secret'))
auth.set_access_token(os.getenv('a_token'), os.getenv('a_secret'))
api = tweepy.API(auth)

# processing
with open('player_history.csv') as csvfile:
    row = random.choice([a for a in list(csv.DictReader(csvfile)) if int(a['Games']) > 0 ])
    po = player.player(
        row['Player Name'],
        row['Goals'],
        row['Games'],
        row['Starter'],
        row['Sub'],
        row['Active'],
        row['Debut']
        )
    api.update_status(status=po.get_guess_player_string())
    time.sleep(10*60)
    api.update_status(status=f"#GuessThePlayer Well done if you got it, the answer was: {po.name} #CFC #Chelsea")
