import requests
from bs4 import BeautifulSoup
import texttable as tt
import csv

URL = "https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')

lister = soup.find('div', id= 'main')
m = lister.find('div', class_='lister')
info = m.find_all('td', class_='titleColumn')

print("Top 250 Movies")
for lines in info:
  print("Top 250 Movies")
  print(lines.text)
