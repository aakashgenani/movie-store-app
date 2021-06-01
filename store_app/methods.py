from urllib.request import urlopen
from models import Movie
from app import db
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


def insert_movie(imdb_id, title, quantity, price, rated, director, genre, year):
    movie = Movie(imdb_id, title, quantity, price, rated, director, genre, year)
    db.session.add(movie)
    db.session.commit()


def delete_movie(imdb_id):
    db.session.query(Movie).filter(Movie.imdb_id == imdb_id).delete()
    db.session.commit()


def movie_bought(quantity_bought, imdb_id):
    movie = Movie.query.filter_by(imdb_id=imdb_id).first()
    movie.quantity = movie.quantity - quantity_bought
    db.session.commit()
