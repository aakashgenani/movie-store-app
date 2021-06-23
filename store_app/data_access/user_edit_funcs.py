from app import db
from tables.models import User
from werkzeug.security import generate_password_hash


def insert_user(username, password, role):
    user = User(username, password, role)
    db.session.add(user)
    db.session.commit()


def delete_user(user_id):
    db.session.query(User).filter(User.id == user_id).delete()
    db.session.commit()


def change_username(user_id, new_username):
    user = User.query.get(user_id)
    user.username = new_username
    db.session.commit()


def change_password(user_id, new_password):
    user = User.query.get(user_id)
    user.password = generate_password_hash(new_password)
    db.session.commit()
