from app import db
from tables.models import Movie


def delete_movie(imdb_id):
    db.session.query(Movie).filter(Movie.imdb_id == imdb_id).delete()
    db.session.commit()


def insert_movie(imdb_id, title, quantity, price, rated, director, genre, year):
    movie = Movie(imdb_id, title, quantity, price, rated, director, genre, year)
    db.session.add(movie)
    db.session.commit()


def set_quantity(imdb_id, new_quantity):
    movie = Movie.query.filter_by(imdb_id=imdb_id).first()
    movie.quantity = new_quantity
    db.session.commit()


def set_price(imdb_id, new_price):
    movie = Movie.query.filter_by(imdb_id=imdb_id).first()
    movie.price = new_price
    db.session.commit()
