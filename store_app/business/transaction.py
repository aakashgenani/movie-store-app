from tables.models import Movie
from app import db


def purchase(imdb_id, quantity_bought):
    movie = Movie.query.filter_by(imdb_id=imdb_id).first()
    movie.quantity = movie.quantity - quantity_bought
    db.session.commit()
