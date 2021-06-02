from flask import make_response, jsonify, request
from app import app
from business import transaction


@app.route('/movie/transaction', methods=['PUT'])
def movie_bought_update_quantity():
    if request.method == "PUT":
        try:
            imdb_id = request.json['imdb_id']
            quantity_bought = request.json['quantity']
            transaction.purchase(imdb_id, quantity_bought)
            msg = "Record successfully updated"
            return make_response(jsonify(response=msg), 201)
        except Exception as e:
            print(f'error: {str(e)}')
            return make_response(jsonify(error=str(e)), 500)
