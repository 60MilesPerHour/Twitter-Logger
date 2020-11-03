#!/usr/bin/env python3

# I AM NOT RESPONSIBLE FOR YOUR ACTIONS! WHAT YOU DO WITH THIS CODE IS YOUR RESPONSIBILITY! YOU ASSUME ALL DAMAGES SHOULD THEY BE BROUGHT UPON YOU BY USING THIS CODE!
#
# you can either attach this to your personal account or you can make a new account but you'll have to grab my retweet bot or another twitterbot so twitter doesn't
# ban your account!
#
# Twitter will not like this code if its runing solo, so make sure your doing something on that account besides this!
#
# 1 GB = roughly 2 months of harvesting data

import twitter
import time
import os
import sys
import datetime
from TLC import Cleaner

api = twitter.Api(consumer_key='', # INPUT YOUR API KEYS HERE 19-22
  consumer_secret='',
  access_token_key='',
  access_token_secret='', sleep_on_rate_limit=True) # HAS TO BE SET TO TRUE OR THE TWITTER POLICE WILL COME

print(twitter.User) # NOT NEEDED BUT YOU'LL PROBABLY FIND IT TO BE PREFERABLE

i = True

while i == True: # WHERE THE MAGIC HAPPENS (DOES NOT END)
    search = api.GetSearch("") # LIKE MY RETWEET BOT, USE @ OR # (EXAMPLE: #60MilesPerHour/#60MilesPerHour)
    for tweet in search:

        T = tweet.id
        appendFile = open('Unfiltered.txt','a') # NAME CAN BE CHANGED, BUT DO NOT CHANGE EXTENSION
        appendFile.write('\n')
        appendFile.write(str(T))
        appendFile.write(" | Wrote on --> ")
        appendFile.write(str(datetime.datetime.now()))
        appendFile.write('\n')

        D = tweet.text

        appendFile.write(str(D))
        appendFile.write('\n')
        appendFile.close()
        time.sleep(15)
        Cleaner()
        continue
    continue

# LOG'S ENTIRE TWEET... RETWEET... LIKE... USERNAME... WHEN THEY WROTE IT... LINK TO TWEET... MEDIA IF ANY...
