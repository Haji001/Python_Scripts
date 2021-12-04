import pandas as pd
import requests
from bs4 import BeautifulSoup

import csv


# Create a list of the info you want to scrap
movie_name = []
year = []
movie_votes = []
movie_earnings = []

# The movie url
URL = "https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating"
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html5lib')


# Movie data info we want to extract
movie_data_info = soup.findAll('div', class_='lister-item mode-advanced')

def self():

  for info in movie_data_info:

    # scrape the movie name
    name = info.h3.a.text
    movie_name.append(name)

    # Scrape the movie years
    movie_year = info.h3.find('span', class_="lister-item-year text-muted unbold").text.replace('(', '').replace(')', '')
    year.append(movie_year)

    # Both votes and gross have the same class name
    values = info.find_all('span', attrs={'name': 'nv'})


    # Movie votes
    movie_vote = values[0].text
    movie_votes.append(movie_vote)

    # Scrap movie total gross
    gross_earnings = values[1].text if len(values) >1 else 'Movie gross is not reported'
    movie_earnings.append(gross_earnings)
self()


# Create a dataframe for the data your scrapped.
movie_table = pd.DataFrame({'Name of Film': movie_name, 'Movie Year': year, 'Movie Votes': movie_votes, 'Movie Gross': movie_earnings})
print(movie_table.to_string())































