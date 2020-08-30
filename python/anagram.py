 # importing modules
import tweepy
import os
import csv
import time
import random

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
def anagram(string):
 l = list(string)
 random.shuffle(l)
 return ''.join(l)

# processing
with open('data_source.csv') as csvfile:
 reader = csv.DictReader(csvfile)
 random_row = random.choice(reader)
 answer = random_row['text']
 question = anagram(random_row['text'])
 api.update_status(status = "#AnagramGame Name the Chelsea player: " + question)     
 time.sleep(10 * 60)
 api.update_status(status = "#AnagramGame Well done if you got it, the answer was: " + answer) 
