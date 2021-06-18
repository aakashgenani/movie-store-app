from flask import make_response, jsonify, g
from app import app
from tables.models import Movie


@app.route('/movies/<int:movie_id>/description', methods=['GET'])
def get_movie_description(movie_id):
    try:
        if g.user.role != 'admin' and g.user.role != 'customer':
            raise ValueError("User must be either admin or customer.")
        if not Movie.query.get(movie_id):
            raise ValueError(f"Movie with movie_id: {movie_id} is not in the database")
        else:
            description = Movie.query.get(movie_id).additional_info()['description']
            return make_response(jsonify(description), 200)
    except Exception as e:
        print(f'error: {str(e)}')
        return make_response(jsonify(error=str(e)), 500)


@app.route('/movies/<int:movie_id>/poster', methods=['GET'])
def get_movie_poster(movie_id):
    try:
        if g.user.role != 'admin' and g.user.role != 'customer':
            raise ValueError("User must be either admin or customer.")
        poster = Movie.query.get(movie_id).additional_info()['poster']
        return make_response(jsonify(poster), 200)
    except Exception as e:
        print(f'error: {str(e)}')
        return make_response(jsonify(error=str(e)), 500)
