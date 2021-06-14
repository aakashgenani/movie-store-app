from urllib.request import urlopen
import json

api_key_path = 'keys/API_Key.txt'


def read_api_key():
    with open(api_key_path, 'r') as out:
        api_key = str(out.read())
    return api_key


def get_data_from_ex_api(imdb_id):
    api_key = read_api_key()
    url = "https://www.omdbapi.com/?i=" + imdb_id + f'&apikey={api_key}'
    data = urlopen(url).read()
    data_p = json.loads(data)
    return data_p


def get_poster_link(imdb_id):
    data_p = get_data_from_ex_api(imdb_id)
    image_link = data_p['Poster']
    return image_link


def get_movie_description(imdb_id):
    data_p = get_data_from_ex_api(imdb_id)
    movie_plot = data_p['Plot']
    return movie_plot


def get_info_from_api(imdb_id):
    data_p = get_data_from_ex_api(imdb_id)
    title = data_p['Title']
    rated = data_p['Rated']
    director = data_p['Director']
    genre = data_p['Genre']
    year = data_p['Year']
    return title, rated, director, genre, year
