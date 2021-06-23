from flask import make_response, jsonify, request, session, url_for, redirect, g
from data_access import get_users_funcs
from werkzeug.security import check_password_hash
from app import app


@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        user = get_users_funcs.get_user_session()
        g.user = user


@app.route('/login', methods=['POST'])
def login():
    try:
        session.pop('user_id', None)
        username = request.json['username']
        password = request.json['password']
        user = get_users_funcs.get_user_by_username(username=username)
        if user and user.verify_password(password=password):
            session['user_id'] = user.id
            return redirect(url_for('profile'))
        else:
            return make_response(jsonify(response='Incorrect details entered. Try again'))
    except Exception as e:
        print(f'error: {str(e)}')
        return make_response(jsonify(error=str(e)), 500)


@app.route('/profile', methods=['GET'])
def profile():
    if not g.user:
        return make_response(jsonify(response="No user logged in."), 500)
    else:
        return make_response(jsonify(response=f"User logged in. User ID: {g.user.id}, and username: "
                                              f"{g.user.username}, Role: {g.user.role}"), 200)


@app.route('/logout', methods=['POST'])
def logout():
    try:
        if g.user:
            session.pop('user_id', None)
            return make_response(jsonify(response='User logged out'), 200)
        else:
            return make_response(jsonify(response='No user was logged in'), 200)
    except Exception as e:
        print(f'error: {str(e)}')
        return make_response(jsonify(error=str(e)), 500)