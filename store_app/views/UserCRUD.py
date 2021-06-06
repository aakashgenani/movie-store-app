from flask import make_response, jsonify, request
from business import UserCRUD
from app import app


@app.route('/users', methods=['POST', 'DELETE'])
def add_or_remove_user():
    if request.method == "POST":
        try:
            name = request.json['name']
            UserCRUD.insert_user(name)
            msg = "Record successfully added"
            return make_response(jsonify(response=msg), 201)
        except Exception as e:
            print(f'error: {str(e)}')
            return make_response(jsonify(error=str(e)), 500)

    if request.method == 'DELETE':
        try:
            user_id = request.json['user_id']
            UserCRUD.delete_user(user_id)
            msg = "Record successfully deleted"
            return make_response(jsonify(response=msg), 201)
        except Exception as e:
            print(f'error: {str(e)}')
            return make_response(jsonify(error=str(e)), 500)


@app.route('/users/<int:user_id>/username', methods=['PATCH'])
def change_username(user_id):
    try:
        new_username = request.json['username']
        UserCRUD.change_username(user_id, new_username)
        msg = "Record successfully updated"
        return make_response(jsonify(response=msg), 201)
    except Exception as e:
        print(f'error: {str(e)}')
        return make_response(jsonify(error=str(e)), 500)
