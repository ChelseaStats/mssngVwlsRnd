 # importing modules
import tweepy
import os
import csv
import time
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
stripped = str.maketrans(dict.fromkeys('aeiouAEIOU '))

# processing
with open('data_source.csv') as csvfile:
 reader = csv.DictReader(csvfile)
 for row in reader:
    answer = row['text']
    question = (row['text']).translate(stripped)
    api.update_status(status = "Name the player:" + question)     
    time.sleep(10 * 60)
    api.update_status(status = "The answer was:" + answer) 
