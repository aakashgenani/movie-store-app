from flask import make_response, jsonify, request, g
from business import ConnectExternalAPI, MovieCRUD
from app import app


@app.route('/movies', methods=['POST', 'DELETE'])
def add_or_remove_movie():
    if request.method == "POST":
        try:
            if g.user.role != 'admin':
                raise ValueError('User must be an admin to perform this function.')
            imdb_id = request.json['imdb_id']
            quantity = request.json['quantity']
            price = request.json['price']
            title, rated, director, genre, year = ConnectExternalAPI.get_info_from_api(imdb_id)
            MovieCRUD.insert_movie(imdb_id, title, quantity, price, rated, director, genre, year)
            msg = "Record successfully added"
            return make_response(jsonify(response=msg), 201)
        except Exception as e:
            print(f'error: {str(e)}')
            return make_response(jsonify(error=str(e)), 500)

    if request.method == 'DELETE':
        try:
            if g.user.role != 'admin':
                raise ValueError('User must be an admin to perform this function.')
            imdb_id = request.json['imdb_id']
            MovieCRUD.delete_movie(imdb_id)
            msg = "Record successfully deleted"
            return make_response(jsonify(response=msg), 201)
        except Exception as e:
            print(f'error: {str(e)}')
            return make_response(jsonify(error=str(e)), 500)


@app.route('/movies/<string:imdb_id>/quantity', methods=['PATCH'])
def set_quantity(imdb_id):
    try:
        if g.user.role != 'admin':
            raise ValueError('User must be an admin to perform this function.')
        new_quantity = request.json['quantity']
        MovieCRUD.set_quantity(imdb_id, new_quantity)
        msg = "Record successfully updated"
        return make_response(jsonify(response=msg), 201)
    except Exception as e:
        print(f'error: {str(e)}')
        return make_response(jsonify(error=str(e)), 500)


@app.route('/movies/<string:imdb_id>/price', methods=['PATCH'])
def set_price(imdb_id):
    try:
        if g.user.role != 'admin':
            raise ValueError('User must be an admin to perform this function.')
        new_price = request.json['price']
        MovieCRUD.set_price(imdb_id, new_price)
        msg = "Record successfully updated"
        return make_response(jsonify(response=msg), 201)
    except Exception as e:
        print(f'error: {str(e)}')
        return make_response(jsonify(error=str(e)), 500)


@app.route('/movies/<string:imdb_id>/year', methods=['PATCH'])
def set_year(imdb_id):
    try:
        if g.user.role != 'admin':
            raise ValueError('User must be an admin to perform this function.')
        new_year = request.json['year']
        MovieCRUD.set_year(imdb_id, new_year)
        msg = "Record successfully updated"
        return make_response(jsonify(response=msg), 201)
    except Exception as e:
        print(f'error: {str(e)}')
        return make_response(jsonify(error=str(e)), 500)
