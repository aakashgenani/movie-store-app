from flask import make_response, jsonify, request, g
from business import user_edit_funcs
from app import app


@app.route('/users', methods=['POST', 'DELETE'])
def add_or_remove_user():
    if request.method == "POST":
        try:
            if g.user.role != 'admin':
                raise ValueError('User needs to be an admin to perform this function.')
            username = request.json['username']
            password = request.json['password']
            role = request.json['role']
            if role != 'admin' and role != 'customer':
                raise ValueError("Roles can either be 'customer' or 'admin'")
            user_edit_funcs.insert_user(username=username, password=password, role=role)
            msg = "Record successfully added"
            return make_response(jsonify(response=msg), 201)
        except Exception as e:
            print(f'error: {str(e)}')
            return make_response(jsonify(error=str(e)), 500)

    if request.method == 'DELETE':
        try:
            if g.user.role != 'admin':
                raise ValueError("User must be an admin to perform this function")
            user_id = request.json['user_id']
            user_edit_funcs.delete_user(user_id)
            msg = "Record successfully deleted"
            return make_response(jsonify(response=msg), 201)
        except Exception as e:
            print(f'error: {str(e)}')
            return make_response(jsonify(error=str(e)), 500)


@app.route('/users/<int:user_id>/username', methods=['PATCH'])
def change_username(user_id):
    try:
        if g.user.role != 'admin' and g.user.id != user_id:
            raise ValueError("Only admin or the user changing the username can perform this function")
        new_username = request.json['username']
        user_edit_funcs.change_username(user_id, new_username)
        msg = "Record successfully updated"
        return make_response(jsonify(response=msg), 201)
    except Exception as e:
        print(f'error: {str(e)}')
        return make_response(jsonify(error=str(e)), 500)


@app.route('/users/<int:user_id>/password', methods=['PATCH'])
def change_password(user_id):
    try:
        if g.user.role != 'admin' and g.user.id != user_id:
            raise ValueError("Only admin or the user changing the username can perform this function")
        new_password = request.json['password']
        user_edit_funcs.change_password(user_id, new_password)
        msg = "Record successfully updated"
        return make_response(jsonify(response=msg), 201)
    except Exception as e:
        print(f'error: {str(e)}')
        return make_response(jsonify(error=str(e)), 500)
