from tables.models import User
from flask import session


def get_user_by_username(username):
    user = User.query.filter_by(username=username).first()
    return user


def get_user_session():
    user = User.query.get(session['user_id'])
    return user
