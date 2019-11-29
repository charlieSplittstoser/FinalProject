from flask import Flask, request, Response, render_template
from flask_login import LoginManager, UserMixin
from flask_sqlalchemy import SQLAlchemy, inspect
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
