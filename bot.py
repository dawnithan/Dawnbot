# Discord.py
import discord
from discord.ext import commands

# BeautifulSoup
import urllib.request as urllib2
from bs4 import BeautifulSoup

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


# @bot.command()
# async def ping(ctx):
# 	'''
# 	This text will be shown in the help command
# 	'''

# 	# Get the latency of the bot
# 	latency = bot.latency  # Included in the Discord.py library
# 	# Send it to the user
# 	await ctx.send("Pong! " + str(latency))


@bot.command()
async def tweet(ctx, arg):
	'''
	Posts all images found within a tweet as Discord doesn't show more than 1 in embeds
	
	TODO: threads break this as the function only retrieves the images of the first
	image div it finds on the web page, rather than the image div of the specific tweet
	'''

	if len(arg) > 0 and arg.startswith("https://twitter.com/"):
		images = []
		try:
			# Access the tweet and get its DOM
			target = urllib2.urlopen(arg)
			soup = BeautifulSoup(target, "lxml")

			# Find the div containing the images and retrieve them
			content = soup.find("div", class_="AdaptiveMedia")
			images = content.findAll("img")

			# Send each image URL source as a message
			# if more than 1 was found
			if(len(images) > 1):
				# Skip the first since it's already in the embed...?
				for image in images[1:]:
					# print(image['src'])
					await ctx.send(image['src'])
		except:
			await ctx.send("Something went wrong - did you supply a valid tweet URL?")
	else:
		await ctx.send("Usage: !tweet https://twitter.com/<username>/status/<tweetid>")


token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
bot.run(token)