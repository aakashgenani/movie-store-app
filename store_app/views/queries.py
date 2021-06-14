from flask import make_response, jsonify, request
from tables.models import Movie, User, UserPurchase
from app import app
from business import MovieCRUD


@app.route('/movies/total-count', methods=['GET'])
def get_count_entries():
    try:
        count = Movie.query.count()
        return make_response(jsonify(count))
    except Exception as e:
        print(f'error: {str(e)}')
        return make_response(jsonify(error=str(e)), 500)


@app.route('/movies/title/<string:title>', methods=['GET'])
def get_movies_by_title(title):
    try:
        movies = Movie.query.filter(Movie.title.like(f'%{title}%')).all()
        return make_response(jsonify([m.serialize() for m in movies]), 200)
    except Exception as e:
        print(f'error: {str(e)}')
        return make_response(jsonify(error=str(e)), 500)


@app.route('/movies/price-range', methods=['GET'])
def get_movies_in_price_range():
    try:
        if not request.args.get('max_price'):
            raise RuntimeError("Missing max_price parameter which is mandatory")
        elif not request.args.get('min_price'):
            raise RuntimeError('Missing min_price parameter which is mandatory')
        else:
            max_price = request.args.get('max_price')
            min_price = request.args.get('min_price')

        movies = Movie.query.filter(Movie.price < max_price, Movie.price > min_price).all()
        return make_response(jsonify([m.serialize() for m in movies]), 200)
    except Exception as e:
        print(f'error: {str(e)}')
        return make_response(jsonify(error=str(e)), 500)


@app.route('/movies/directors/<string:director_name>', methods=['GET'])
def get_movies_by_director(director_name):
    try:
        movies = Movie.query.filter(Movie.director.like(f'%{director_name}%')).all()
        return make_response(jsonify([m.serialize() for m in movies]), 200)
    except Exception as e:
        print(f'error: {str(e)}')
        return make_response(jsonify(error=str(e)), 500)


@app.route('/movies/rated/<string:rated>', methods=['GET'])
def get_movies_by_rated(rated):
    try:
        movies = Movie.query.filter_by(rated=rated).all()
        return make_response(jsonify([m.serialize() for m in movies]), 200)
    except Exception as e:
        print(f'error: {str(e)}')
        return make_response(jsonify(error=str(e)), 500)


@app.route('/movies/purchase-date', methods=['GET'])
def get_movies_within_date_range():
    try:
        if not request.args.get('low_date'):
            raise ValueError("Missing low_date parameter")
        elif not request.args.get('up_date'):
            raise ValueError('Missing up_date parameter')
        else:
            lower_date = request.args.get('low_date')
            upper_date = request.args.get('up_date')
        purchases = MovieCRUD.get_movie_by_date_range(lower_date=lower_date, upper_date=upper_date)
        return make_response(jsonify([m.serialize() for m in purchases]), 200)
    except Exception as e:
        print(f'error: {str(e)}')
        return make_response(jsonify(error=str(e)), 500)


@app.route('/users/<int:user_id>/movies', methods=['GET'])
def get_movies_bought_by_user_id(user_id):
    try:
        purchases = UserPurchase.query.filter_by(user_id=user_id).all()
        return make_response(jsonify([m.serialize() for m in purchases]), 200)
    except Exception as e:
        print(f'error: {str(e)}')
        return make_response(jsonify(error=str(e)), 500)


@app.route('/users/<string:username>/movies', methods=['GET'])
def get_movies_bought_by_username(username):
    try:
        user = User.query.filter_by(username=username).first()
        return make_response(jsonify([m.serialize() for m in user.purchases]), 200)
    except Exception as e:
        print(f'error: {str(e)}')
        return make_response(jsonify(error=str(e)), 500)
