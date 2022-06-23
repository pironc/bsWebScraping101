import requests
from bs4 import BeautifulSoup

yourstring = "the string you found"
url = "https://intra.epitech.eu/auth-7ed7544501d6a96dc54f0ba85297ba97b1f7c7b9/user/#!/netsoul"

# Make a GET request to fetch the raw HTML content
response = requests.get(url)

# Parse the html content
soup = BeautifulSoup(response.text, "lxml")

# Extract the element we need
offering = soup.find("span", attrs={"class": "note"}).find("span", attrs={"class": "value"})

# Print the string you found
print("Your credits : {}".format(offering.text))