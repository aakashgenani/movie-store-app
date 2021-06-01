from app import db


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

    def __init__(self, imdb_id, title, quantity, price, rated, director, genre, year):
        self.imdb_id = imdb_id
        self.title = title
        self.quantity = quantity
        self.price = price
        self.rated = rated
        self.director = director
        self.genre = genre
        self.year = year

    def __repr__(self):
        return f"{self.title}, {self.quantity}, ${self.price}, {self.imdb_id}"

    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'imdb_id': self.imdb_id,
            'title': self.title,
            'quantity': self.quantity,
            'price': self.price,
            'rated': self.rated,
            'director': self.director,
            'genre': self.genre,
            'year': self.year
            }
