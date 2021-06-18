from flask import make_response, jsonify, g
from app import app
from business import recommendation


@app.route('/users/<int:user_id>/recommendation', methods=['GET'])
def recommend_movie(user_id):
    try:
        if g.user.role != 'admin' and g.user.id != user_id:
            raise ValueError('User needs to be an admin or the same user who is performing the query')
        recommended_movies = recommendation.recommend_movie(user_id)
        return make_response(jsonify(recommended_movies), 200)
    except Exception as e:
        print(f'error: {str(e)}')
        return make_response(jsonify(error=str(e)), 500)
