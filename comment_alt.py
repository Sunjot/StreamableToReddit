#!/usr/bin/env python

from subprocess import check_output
import praw
import sys
import time

# Supply your streamable/reddit account details, as well as the GDT link and home/away team subs
STRM_USERNAME = 
STRM_PASSWORD = 
REDD_USERNAME = 
REDD_PASSWORD = 
GAMETHREAD = 
AWAYTEAMSUB = 
HOMETEAMSUB = 
TEXTFILE = 

# Assign the command line arguments to the following variables
VIDEO_NAME = sys.argv[1]
LINK_CAPTION = sys.argv[2]

# Uploads the video to streamable and produces a link to the video
output = check_output(['curl', '-F', 'file=@' + VIDEO_NAME, '-u', 
	STRM_USERNAME + ':' + STRM_PASSWORD, 'https://api.streamable.com/upload'])

strm_link = 'https://streamable.com/' + output[28:-2]

# Logs into your reddit account and posts the streamable link to the given GDT as a comment
r = praw.Reddit(user_agent='Post video (via streamable) to Reddit, by yourusername')
r.login(REDD_USERNAME, REDD_PASSWORD)

time.sleep(3)
submission = r.get_submission(url=GAMETHREAD)
submission.add_comment('[STRM: ' + LINK_CAPTION + '](' + strm_link + ')')

f = open(TEXTFILE, "a")

if sys.argv[3] == "away":
	f.write("[](/r/" + AWAYTEAMSUB + ") | " + sys.argv[2] + " | [STRM](" + strm_link + ")\n")
else:
	f.write("[](/r/" + HOMETEAMSUB + ") | " + sys.argv[2] + " | [STRM](" + strm_link + ")\n")

f.close()
