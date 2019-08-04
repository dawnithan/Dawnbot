# Dawnbot

Simple Discord bot built mostly for fun, that handles provides a couple of commands:

* !tweet returns the URL(s) of a given tweet's hidden images in the current message channel. This is to circumvent the current design of Discord's embedded tweets, which only display 1 image even if the tweet contains multiple images.

* !quote returns the URL of the tweet within a quoted tweet which is otherwise hidden as a t.co link within Discord embeds.

In order to use the bot, you will need to provide Twitter API keys in the `twitter_creditentials.json` file. To get these keys, you need to sign up to the Twitter API.

Additionally, you need to replace `'XXXXX'` with the token of your Discord bot, which you can get by going to https://discordapp.com/developers/applications/, then clicking on (or creating) your bot, then going Bot -> Copy Token.

Install the modules by running "pip install -r requirements.txt" in the console/terminal.

Run the bot with "python3 bot.py".
