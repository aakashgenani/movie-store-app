from flask import make_response, jsonify
from business import ConnectExternalAPI
from tables.models import Movie
from app import app
import webbrowser


@app.route('/movies/<int:movie_id>/poster', methods=['GET'])
def get_poster(movie_id):
    try:
        movie = Movie.query.filter_by(id=movie_id).first()
        image_link = ConnectExternalAPI.get_poster_link(movie.imdb_id)
        webbrowser.open_new_tab(image_link)
        return make_response(jsonify(response='ok'), 201)
    except Exception as e:
        print(f'error: {str(e)}')
        return make_response(jsonify(error=str(e)), 500)
