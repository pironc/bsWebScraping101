import requests
from bs4 import BeautifulSoup

url = "http://www.krosmoz.com/fr/almanax"

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text

# Parse the html content
soup = BeautifulSoup(html_content, "lxml")

# Finding the "fleft" class in the "p" tag (Almanax's daily offering)
offering = soup.find("p", attrs={"class": "fleft"})

# The bot will then write the Almanax daily offering and bonus in the Discord chat you typed the command in
print("String found : {}".format(offering.text.strip().partition(".")[0]))