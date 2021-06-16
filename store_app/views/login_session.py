from flask import make_response, jsonify, request, session, url_for, redirect, g
from tables.models import Movie, User, UserPurchase
from app import app


@app.before_request
def before_request():
    g.user = None
    # try:
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        g.user = user
    #     else:
    #         raise ValueError('User not logged in')
    # except Exception as e:
    #     print(f'error: {str(e)}')
    #     return make_response(jsonify(error=str(e)), 500)


@app.route('/login', methods=['POST'])
def login():
    try:
        session.pop('user_id', None)
        username = request.json['username']
        password = request.json['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('profile'))
        else:
            return make_response(jsonify(response='Incorrect details entered. Try again'))
            # return make_response(jsonify(response='User logged in'), 200)
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