from tables.models import Movie


def get_movies_by_rating(rated):
    movies = Movie.query.filter_by(rated=rated).all()
    return movies


def get_movies_by_genre(genre):
    movies = Movie.query.filter(Movie.genre.like(f'%{genre}%')).all()
    return movies


def get_movies_by_director(director_name):
    movies = Movie.query.filter(Movie.director.like(f'%{director_name}%')).all()
    return movies


def get_movies_within_price_range(max_price, min_price):
    movies = Movie.query.filter(Movie.price < max_price, Movie.price > min_price).all()
    return movies


def get_movies_by_title(title):
    movies = Movie.query.filter(Movie.title.like(f'%{title}%')).all()
    return movies


def get_movie_by_movie_id(movie_id):
    movie = Movie.query.get(movie_id)
    return movie


def get_movies_all():
    movies = Movie.query.all()
    return movies


def get_movies_count():
    count = Movie.query.count()
    return count
