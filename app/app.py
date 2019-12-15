from flask import Flask, request, Response, render_template
from flask_login import LoginManager, UserMixin
from flask_sqlalchemy import SQLAlchemy, inspect
from flask_migrate import Migrate
from sqlalchemy import create_engine, Table
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "thisismysecretkey"
app.config['TESTING'] = False
db = SQLAlchemy(app)

migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'


import routes, models

if __name__ == '__main__':
    app.run()
