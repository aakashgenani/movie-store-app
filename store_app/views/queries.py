from flask import make_response, jsonify
from tables.models import Movie
from app import app


@app.route('/movies/total-count', methods=['GET'])
def get_count_entries():
    count = Movie.query.count()
    return make_response(jsonify(count))


@app.route('/movies/directors/<string:director_name>', methods=['GET'])
def get_movies_by_director(director_name):
    try:
        movies = Movie.query.filter(Movie.director.like(f'%{director_name}%')).all()
        return make_response(jsonify([m.serialize() for m in movies]), 200)
    except Exception as e:
        print(f'error: {str(e)}')
        return make_response(jsonify(error=str(e)), 500)
