import requests
from bs4 import BeautifulSoup

yourstring = "the string you found"
url = "https://intra.epitech.eu/yourauth"

# Make a GET request to fetch the raw HTML content
response = requests.get(url)

# Parse the html content
soup = BeautifulSoup(response.text, "lxml")

# Extract the element we need
offering = soup.find("span", attrs={"class": "note"}).find("span", attrs={"class": "value"})

# Print the string you found
print("Your credits : {}".format(offering.text))
