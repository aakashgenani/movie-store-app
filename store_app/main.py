from app import db
from tables import models


def insert_movie(title, quantity, price, imdb_id):
    movie = models.Movie(title, quantity, price, imdb_id)
    db.session.add(movie)
    db.session.commit()


def main():
    db.create_all()
    # a = 1
    # INSERT MOVIES
    # insert_movie('The Social Network', 10, 6.99, 'tt1285016')
    # insert_movie('Zodiac', 15, 10, 'tt0443706')
    # movie = models.Movie.query.filter_by(id=1).first()
    # print(movie)


if __name__ == '__main__':
    main()
