from flask import make_response, jsonify, request, g
from app import app
from data_access import transaction


@app.route('/movies/transaction', methods=['PUT'])
def movie_bought_update_quantity():
    try:
        imdb_id = request.json['imdb_id']
        quantity_purchased = request.json['quantity']
        if not g.user:
            raise ValueError('User must be logged in to perform this function.')
        if g.user.role != 'customer':
            raise ValueError('User must be a customer to perform this function.')
        msg = transaction.purchase(user_id=g.user.id, imdb_id=imdb_id, quantity_purchased=quantity_purchased)
        return make_response(jsonify(response=msg), 201)
    except Exception as e:
        print(f'error: {str(e)}')
        return make_response(jsonify(error=str(e)), 500)
