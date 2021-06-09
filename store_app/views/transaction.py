from flask import make_response, jsonify, request
from app import app
from business import transaction


@app.route('/movies/transaction', methods=['PUT'])
def movie_bought_update_quantity():
    # if request.method == "PUT":
    try:
        user_id = request.json['user_id']
        imdb_id = request.json['imdb_id']
        quantity_purchased = request.json['quantity']
        msg = transaction.purchase(user_id=user_id, imdb_id=imdb_id, quantity_purchased=quantity_purchased)
        return make_response(jsonify(response=msg), 201)
    except Exception as e:
        print(f'error: {str(e)}')
        return make_response(jsonify(error=str(e)), 500)
