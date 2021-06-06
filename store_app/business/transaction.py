from tables.models import Movie, UserPurchase, User
from app import db
from business import MovieCRUD


def purchase(user_id, imdb_id, quantity_purchased):
    try:
        movie = Movie.query.filter_by(imdb_id=imdb_id).first()
        movie.quantity = movie.quantity - quantity_purchased
        if movie.quantity < 0:
            raise ValueError('Movie quantity cannot be negative.')
        user = User.query.filter_by(id=user_id).first()
        transaction = UserPurchase(user_id=user.id, imdb_id=imdb_id, quantity_purchased=quantity_purchased)
        # if movie.quantity == 0:
        #     MovieCRUD.delete_movie(imdb_id)
        db.session.add(transaction)
        db.session.commit()
        msg = 'Transaction Successful.'
        return msg
    except ValueError:
        db.session.rollback()
        msg = "Value Error: Movie quantity cannot be negative."
        return msg
