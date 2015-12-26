# Streamable To Reddit

A simple python program that allows you to upload videos to streamable and have them posted to reddit.

## Use

Make sure PRAW is installed. 

There are 5 global variables that must be assigned before we can proceed:

  1. Your streamable username and password
  2. Your reddit username and password
  3. The subreddit (without the /r/) or thread you plan on submitting/commenting your video to

The program requires 3 command line arguments in terminal:

  1. The script name itself - i.e. "post.py"
  2. Video filename with the extension included - i.e. "myvideo.mov"
  3. Name of the reddit post/comment - i.e. "This is a video of mine"

In the end, we get something like: "python post.py myvideo.mov "This is a video of mine"

NOTE: The video you choose to upload must be in the same directory as your script. 
