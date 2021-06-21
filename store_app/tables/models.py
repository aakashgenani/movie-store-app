from app import db
from datetime import datetime
from business import connect_external_API


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    imdb_id = db.Column(db.String(20), unique=True, nullable=False)
    title = db.Column(db.String(80), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float(5), nullable=False)
    rated = db.Column(db.String(20), nullable=True)
    director = db.Column(db.String(50), nullable=True)
    genre = db.Column(db.String(50), nullable=True)
    year = db.Column(db.Integer, nullable=True)
    purchases = db.relationship('UserPurchase', backref='movie_purchases', lazy=True)

    def __init__(self, imdb_id, title, quantity, price, rated, director, genre, year):
        self.imdb_id = imdb_id
        self.title = title
        self.quantity = quantity
        self.price = price
        self.rated = rated
        self.director = director
        self.genre = genre
        self.year = year
        self.poster = connect_external_API.get_poster_link(self.imdb_id)

    def __repr__(self):
        return f"Movie Title: {self.title}, Quantity Available: {self.quantity}, Price: ${self.price}"

    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'movie_id': self.id,
            'imdb_id': self.imdb_id,
            'title': self.title,
            'quantity': self.quantity,
            'price': self.price,
            'rated': self.rated,
            'director': self.director,
            'genre': self.genre,
            'year': self.year,
            }

    def additional_info(self):
        return{
            'poster': connect_external_API.get_poster_link(imdb_id=self.imdb_id),
            'description': connect_external_API.get_movie_description(imdb_id=self.imdb_id)
        }


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(20))
    role = db.Column(db.String(20))
    purchases = db.relationship('UserPurchase', backref='user_purchases', lazy=True)

    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def __repr__(self):
        return f"UserID: {self.id}, User Name: {self.username}"

    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'username': self.username,
            }


class UserPurchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user_rel = db.relationship('User', foreign_keys='UserPurchase.user_id')
    imdb_id = db.Column(db.String(20), db.ForeignKey('movie.imdb_id'), nullable=False)
    movie_rel = db.relationship('Movie', foreign_keys='UserPurchase.imdb_id')
    quantity_purchased = db.Column(db.Integer, nullable=False)
    date_purchased = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, user_id, imdb_id, quantity_purchased):
        self.user_id = user_id
        self.imdb_id = imdb_id
        self.quantity_purchased = quantity_purchased

    def __repr__(self):
        return f"Transaction ID: {self.id}, User ID: {self.user_id}, " \
               f"Username: {User.query.get(self.user_id).username}, " \
               f"Quantity Purchased: {self.quantity_purchased}, " \
               f"Date of Transaction: {self.date_purchased}"

    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'transaction_id': self.id,
            'user_id': self.user_id,
            'username': User.query.get(self.user_id).username,
            'imdb_id': self.imdb_id,
            'Movie title': self.movie_rel.title,
            'quantity_purchased': self.quantity_purchased,
            'date_purchased': self.date_purchased
            }
