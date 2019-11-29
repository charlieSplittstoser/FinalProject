from flask import Flask, request, Response, render_template
from flask_login import LoginManager, UserMixin
from flask_sqlalchemy import SQLAlchemy, inspect, relationship
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/TestDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "blah123"
app.config['TESTING'] = False
db = SQLAlchemy(app)

migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'


from app import routes, models
