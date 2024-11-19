from bs4 import BeautifulSoup
import requests

url = 'http://quotes.toscrape.com/'
response = requests.get(url)
print(response.content)
