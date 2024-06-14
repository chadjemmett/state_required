import requests
from bs4 import BeautifulSoup as bs

url = "https://www.sdale.org/page/state-required"
data = requests.get(url)
print(data.text)

soup = bs(data.text, 'html.parser')
print(soup)
