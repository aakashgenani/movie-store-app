from flask import make_response, jsonify
from tables.models import Movie
from app import app


@app.route('/movies/<int:movie_id>/description', methods=['GET'])
def get_movie_description(movie_id):
    try:
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
        description = Movie.query.get(movie_id).additional_info()['poster']
        return make_response(jsonify(description), 200)
    except Exception as e:
        print(f'error: {str(e)}')
        return make_response(jsonify(error=str(e)), 500)
