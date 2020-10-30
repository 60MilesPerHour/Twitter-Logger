#!/usr/bin/env python3

# I AM NOT RESPONSIBLE FOR YOUR ACTIONS! WHAT YOU DO WITH THIS CODE IS YOUR RESPONSIBILITY! YOU ASSUME ALL DAMAGES SHOULD THEY BE BROUGHT UPON YOU BY USING THIS CODE!
#
# you can either attach this to your personal account or you can make a new account but you'll have to grab my retweet bot or another twitterbot so twitter doesn't
# ban your account!
#
# Twitter will not like this code if its runing solo, so make sure your doing something on that account besides this!
#
# 1 GB = roughly 2 months of harvesting data

import twitter # pip3 install python-twitter
import time
import os
import sys
import datetime
import hashlib

def Cleaner():
  output_file_path = "ENTER PATH TO OUTPUT FILE AND NAME, FILE WILL BE CREATED ON FIRST RUN"
  input_file_path = "ENTER PATH TO INPUT FILE AND NAME, FILE WILL BE CREATED ON FIRST RUN" # YOU DEFINED THIS IN LINE 51

  completed_lines_hash = set()

  output_file = open(output_file_path, "w")

  for line in open(input_file_path, "r"):

    hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()

    if hashValue not in completed_lines_hash:
      output_file.write(line)
      completed_lines_hash.add(hashValue)

  output_file.close()

api = twitter.Api(consumer_key='', # INPUT YOUR API KEYS HERE 37-40
  consumer_secret='',
  access_token_key='',
  access_token_secret='', sleep_on_rate_limit=True) # HAS TO BE SET TO TRUE OR THE TWITTER POLICE WILL COME

print(twitter.User) # NOT NEEDED BUT YOU'LL PROBABLY FIND IT TO BE PREFERABLE

i = True

while i == True: # WHERE THE MAGIC HAPPENS (DOES NOT END)
    search = api.GetSearch("") # LIKE MY RETWEET BOT, USE @ OR # (EXAMPLE: #60MilesPerHour/#60MilesPerHour)
    for tweet in search:

        T = tweet.id
        appendFile = open('FILENAME_NOT_CLEAN.txt','a') # NAME CAN BE CHANGED, BUT DO NOT CHANGE EXTENSION
        appendFile.write('\n')
        appendFile.write(str(T))
        appendFile.write(" | Wrote on --> ")
        appendFile.write(str(datetime.datetime.now()))
        appendFile.write('\n')

        D = tweet.text

        appendFile.write(str(D))
        appendFile.write(" | Written on --> ")
        appendFile.write(str(datetime.datetime.now()))
        appendFile.write('\n')
        appendFile.close()
        time.sleep(15)
        Cleaner()
        continue  
    continue

# LOG'S ENTIRE TWEET... RETWEET... LIKE... USERNAME... WHEN THEY WROTE IT... LINK TO TWEET... MEDIA IF ANY...