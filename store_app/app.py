from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key ='123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/movie_store.db'
db = SQLAlchemy(app)

import tables.models
from views import MovieCRUD, UserCRUD, ExternalAPI, homepage, queries, transaction, login_session
