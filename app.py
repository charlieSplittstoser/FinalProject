from flask import Flask, request, Response, render_template
import requests
from flask_sqlalchemy import SQLAlchemy, inspect
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    #def set_password(self, password):
        #self.password_hash = generate_password_hash(password)

    #def check_password(self, password):
        #return check_password_hash(self.password_hash, password)

@app.route('/')
def index():
    db.create_all()
   # admin = User(username='admin', email='admin@example.com')
   # guest = User(username='guest', email='guest@example.com')

    print("Hello")

  #  db.session.add(admin)
  #  db.session.add(guest)
  #  db.session.commit()

    print(User.query.all())

    print("Goodbye")

    return render_template("base.html")
