from urllib.request import urlopen
import json


def get_poster_link(imdb_id):
    # movie = movie_id
    # add = movie.replace(' ', '+')
    url = "https://www.omdbapi.com/?i=" + imdb_id + '&apikey=aafb7441&'
    data = urlopen(url).read()
    data_p = json.loads(data)
    image_link = data_p['Poster']
    return image_link


def get_info_from_api(imdb_id):
    url = "https://www.omdbapi.com/?i=" + imdb_id + '&apikey=aafb7441&'
    data = urlopen(url).read()
    data_p = json.loads(data)
    title = data_p['Title']
    rated = data_p['Rated']
    director = data_p['Director']
    genre = data_p['Genre']
    year = data_p['Year']
    return title, rated, director, genre, year
