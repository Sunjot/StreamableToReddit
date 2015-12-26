#!/usr/bin/env python

# IMPORTS
from subprocess import check_output
import praw
import sys

# Supply your streamable/reddit account details, as well as the subreddit to post to
STRM_USERNAME = 
STRM_PASSWORD = 
REDD_USERNAME = 
REDD_PASSWORD = 
SUBREDDIT = 

# Assign the command line arguments to the following variables
VIDEO_NAME = sys.argv[1]
LINK_TITLE = sys.argv[2]

# Uploads the video to streamable and produces a link to the video
output = check_output(['curl', '-F', 'file=@' + VIDEO_NAME, '-u', 
	STRM_USERNAME + ':' + STRM_PASSWORD, 'https://api.streamable.com/upload'])

strm_link = 'https://streamable.com/' + output[28:-2]

# Logs into your reddit account and posts the streamable link to the given subreddit
r = praw.Reddit(user_agent='Post video (via streamable) to Reddit, by yourusername')
r.login(REDD_USERNAME, REDD_PASSWORD)

r.submit(SUBREDDIT, LINK_TITLE, url=strm_link)
