# Twitter Logger
## Deprecated - Please see Version 2 for better performance and higher functionality
Have you ever wanted an automatically generated text file of raw data pulled from Twitter that logs every mention of a specific phrase, hashtag, or user? This script does exactly that. Upon execution of the Twitter logger, you will see a raw data file filing up with data that has not been sorted yet, soon after that file is created you will see a now automatically generated cleaned up version of that specific file.

## Python Library

Use the package manager [pip3](https://pypi.org/project/python-twitter/) to install python-twitter.

```bash
pip3 install python-twitter
```

## Usage

```import twitter
import time
import os
import sys
import datetime
from TLC import Cleaner

api = twitter.Api(consumer_key='', # INPUT YOUR API KEYS HERE
  consumer_secret='',
  access_token_key='',
  access_token_secret='', sleep_on_rate_limit=True) # TWITTER POLICE WILL COME IF THIS IS NOT SET TO TRUE
```

## Copyright

<a class="copyrighted-badge" title="Copyrighted.com Registered &amp; Protected" target="_blank" href="https://www.copyrighted.com/work/SDN9EdkW1uqttNJe"><img alt="Copyrighted.com Registered &amp; Protected" border="0" width="125" height="25" srcset="https://static.copyrighted.com/badges/125x25/05_2_2x.png 2x" src="https://static.copyrighted.com/badges/125x25/05_2.png" /></a>

Twitter-Logger is copyrighted by the Twitter user @60MilesPerHour, Twitter-Logger is copyrighted (c) under copyrighted.com

I hereby grant you the downloader of my program to use this software free of charge. I the creator of this software grant you permission to use the mentioned software without restriction, however, you are hereby subject to the following conditions

The software you download is provided as is without any such warranty of any kind. 
You are forbidden to merchandise off of this software unless otherwise granted by me, the author of this software.
By downloading this software, you agree that i the issuer am not liable for any infringement, claims, damages, or any other liabilities, whether contracted or otherwise.

Contact @60MilesPerHour if you have any questions and i will try to answer them to the best of my ability.
