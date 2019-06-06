from bs4 import BeautifulSoup
import urllib.request as urllib2

# Tweet to extract images from
# Below tweet is an example
tweet = "https://twitter.com/peachhugs/status/1132346135375433729"

# Array to store images
images = []

# Access the tweet and get its DOM
target = urllib2.urlopen(tweet)
soup = BeautifulSoup(target, "lxml")

# Find the div containing the images and get all "img"
content = soup.find("div", class_="AdaptiveMedia")
images = content.findAll("img")

# Print each img source
for image in images:
	print(image['src'])
