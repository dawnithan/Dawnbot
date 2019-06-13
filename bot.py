import json
import re
import discord
from discord.ext import commands
from twython import Twython

bot_token = str(os.environ.get('BOT_TOKEN'))
consumer_key = str(os.environ.get('CONSUMER_KEY'))
consumer_secret = str(os.environ.get('CONSUMER_SECRET'))

# Access Twitter functions
twitter = Twython(consumer_key, consumer_secret)

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

token = BOT_TOKEN
bot.run(token)