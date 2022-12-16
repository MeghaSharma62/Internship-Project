import requests

from bs4 import BeautifulSoup



url = "https://en.wikipedia.org/wiki/Can_Yaman"



response = requests.get(url)

soup = BeautifulSoup(response.text,"lxml")

# print(soup.title.string)

# print (soup.Life.string)
