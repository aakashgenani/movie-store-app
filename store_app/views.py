from flask import make_response, jsonify, render_template, request
from models import Movie
from app import app
import webbrowser
import methods


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/movie/total-count', methods=['GET'])
def get_count_entries():
    count = Movie.query.count()
    return make_response(jsonify(count))


@app.route('/movie/<int:movie_id>/poster', methods=['GET'])
def get_poster(movie_id):
    movie = Movie.query.filter_by(id=movie_id).first()
    image_link = methods.get_poster_link(movie.imdb_id)
    webbrowser.open_new_tab(image_link)
    return make_response(jsonify(response='ok'), 201)


@app.route('/movie/add', methods=['POST', 'GET'])
def add_movie():
    if request.method == "POST":
        imdb_id = request.form['imdb_id']
        quantity = request.form['quantity']
        price = request.form['price']
        title, rated, director, genre, year = methods.get_info_from_api(imdb_id)
        methods.insert_movie(imdb_id, title, quantity, price, rated, director, genre, year)
        msg = "Record successfully added"
        return make_response(jsonify(response=msg), 201)
    elif request.method == 'GET':
        return render_template('add-movie.html')


@app.route('/movie/delete', methods=['POST', 'GET'])
def delete_movie():
    if request.method == 'POST':
        imdb_id = request.form['imdb_id']
        methods.delete_movie(imdb_id)
        msg = "Record successfully deleted"
        return make_response(jsonify(response=msg), 201)
    elif request.method == 'GET':
        return render_template('delete-movie.html')


@app.route('/movie/buy', methods=['POST', 'GET'])
def movie_bought_update_quantity():
    if request.method == "POST":
        imdb_id = request.form['imdb_id']
        quantity_bought = request.form['quantity']
        # quantity_bought = request.json['quantity']
        methods.movie_bought(int(quantity_bought), imdb_id)
        msg = "Record successfully updated"
        return make_response(jsonify(response=msg), 201)
    elif request.method == 'GET':
        return render_template('buy-movie.html')
