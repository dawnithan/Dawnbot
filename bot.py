#! /usr/bin/python3
import json
import re
import discord
from discord.ext import commands
from twython import Twython

# Load Twitter API keys from a local file
with open("twitter_credentials.json", "r") as file:  
    creds = json.load(file)

# Access Twitter functions
twitter = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])

# Define the prefix used to call commands (e.g. !tweet)
prefix = "!"
bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
	print('Logged in as ' + bot.user.name)


@bot.event
async def on_message(message):
	if message.author == bot.user:
		return

	# This echoes every message in the channel to the console
	# print("The message's content was:", message.content)
	await bot.process_commands(message)


@bot.command()
async def tweet(ctx, arg):
	'''
	Posts all images found within a tweet as Discord doesn't show more than 1 in embed
	arg -> the tweet as argument
	'''
	msg = "Other images in tweet: "
	if len(arg) > 0 and arg.startswith("https://twitter.com/"):
		try:
			# Get the tweet's ID, and then extract its media
			find_id_regex = re.compile('(?:status\\/)(.*)')
			
			tweet_id = find_id_regex.search(arg)

			tweet = twitter.show_status(id=tweet_id.group(1), tweet_mode="extended")
			media = tweet['extended_entities']['media']
			
			# Send each media URL as a message if more than 1 was found
			if(len(media) > 1):
				for element in media[1:]:
					msg += element['media_url_https'] + " "
				await ctx.send(msg)
		except:
			await ctx.send("Something went wrong - did you supply a valid tweet URL?")
	else:
		await ctx.send("Usage: !tweet https://twitter.com/<username>/status/<tweetid>")

@bot.command()
async def quote(ctx, arg):
	'''
	Posts the quoted tweet within a tweet as a chat message
	arg -> the tweet as argument
	'''
	msg = "**Quote tweet:** "
	if len(arg) > 0 and arg.startswith("https://twitter.com/"):
		try:
			find_id_regex = re.compile('(?:status\\/)(.*)')
			
			tweet_id = find_id_regex.search(arg)

			tweet = twitter.show_status(id=tweet_id.group(1), tweet_mode="extended")
			
			# quote_text = tweet['quoted_status']['full_text']
			quote_tweet = tweet['quoted_status_permalink']['expanded']

			if(len(quote_tweet) > 0):
				msg += quote_tweet
				await ctx.send(msg)
			else:
				await ctx.send("No quote content found.")
		except:
			await ctx.send("Something went wrong - did you supply a valid tweet URL or quote tweet?")
	else:
		await ctx.send("Usage: !quote https://twitter.com/<username>/status/<tweetid>")

token = "XXXXX"
bot.run(token)