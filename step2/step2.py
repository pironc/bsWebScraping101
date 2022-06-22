import requests
from bs4 import BeautifulSoup

url = "https://newyork.craigslist.org/search/apa"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

print("Here are the listings from your research :\n")