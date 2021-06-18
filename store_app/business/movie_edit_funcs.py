from app import db
from tables.models import Movie, UserPurchase
from sqlalchemy import and_


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


def set_year(imdb_id, new_year):
    movie = Movie.query.filter_by(imdb_id=imdb_id).first()
    movie.year = new_year
    db.session.commit()


def get_movie_by_date_range(lower_date, upper_date):
    purchases = UserPurchase.query.filter(and_(UserPurchase.date_purchased <= f'{upper_date}',
                                               UserPurchase.date_purchased >= f'{lower_date}'))
    return purchases
