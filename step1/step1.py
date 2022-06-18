import requests
from bs4 import BeautifulSoup

yourstring = "the string you found"
url = "epitech"

# Make a GET request to fetch the raw HTML content
response = requests.get(url)

# Parse the html content

# Print the string you found
print("String found : {}".format(response.text))