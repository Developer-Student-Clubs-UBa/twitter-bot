#!/usr/bin/python
# -*-coding:utf-8-*-
"""
This is a simple script for the GDSC-UBa twitter bot

TODO: Add credentials
"""

# External Libs
from tkinter import *

# Owned
from bot_actions import *

__author__ = "Elroy Kanye"
__credits__ = ["Elroy Kanye"]
__license__ = "Set license here"
__version__ = "0.1.0"
__maintainer__ = "Elroy Kanye"
__email__ = "elroykanye@gmail.com"
__status__ = "Dev"

# Code
root = Tk()

search_label = Label(root, text='Search')
search_entry = Entry(root, bd=5)

num_tweets_label = Label(root, text='Number of tweets')
num_tweets_entry = Entry(root, bd=5)

response_label = Label(root, text='Response')
response_entry = Entry(root, bd=5)

reply_label = Label(root, text='Reply?')
reply_entry = Entry(root, bd=5)

retweet_label = Label(root, text='Retweet?')
retweet_entry = Entry(root, bd=5)

favorite_label = Label(root, text='Favorite')
favorite_entry = Entry(root, bd=5)

follow_label = Label(root, text='Follow')
follow_entry = Entry(root, bd=5)


def main():
    search = search_entry.get()
    num_tweets = int(num_tweets_entry.get())
    response = response_entry.get()

    reply = reply_entry.get()
    retweet = retweet_entry.get()
    favorite = favorite_entry.get()
    follow = follow_entry.get()

    if reply == 'yes':
        reply_tweet(search, num_tweets, response)

    if retweet == 'yes':
        retweet_tweet(search, num_tweets)

    if favorite == 'yes':
        fav_tweet(search, num_tweets)

    if follow == 'yes':
        follow_user(search, num_tweets)


submit_button = Button(root, text="Submit", command=main)

search_label.pack()
search_entry.pack()

num_tweets_label.pack()
num_tweets_entry.pack()

response_label.pack()
response_entry.pack()

reply_label.pack()
reply_entry.pack()

retweet_label.pack()
retweet_entry.pack()

favorite_label.pack()
favorite_entry.pack()

follow_label.pack()
follow_entry.pack()

submit_button.pack(side=BOTTOM)

root.mainloop()
