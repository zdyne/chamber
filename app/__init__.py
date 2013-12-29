"""
Copyright 2013, Patrick J. Franz
"""

from flask import Flask
from flask.ext import sqlalchemy
from flask.ext import login
from flask.ext import bcrypt


app = Flask(__name__, static_folder='static', static_url_path='')
app.config.from_object('config')

db = sqlalchemy.SQLAlchemy(app)

loginManager = login.LoginManager()
loginManager.init_app(app)
loginManager.login_view = 'loginRoute'

bcrypt = bcrypt.Bcrypt(app)

from app import views, models
