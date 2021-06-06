from app import db
from tables.models import User


def insert_user(name):
    user = User(name)
    db.session.add(user)
    db.session.commit()


def delete_user(user_id):
    db.session.query(User).filter(User.id == user_id).delete()
    db.session.commit()


def change_username(user_id, new_username):
    user = User.query.get(user_id)
    user.username = new_username
    db.session.commit()
