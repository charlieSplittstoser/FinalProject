from app import app
from flask import render_template
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from app.forms import LoginForm
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
#@login_required
def index():
    db.create_all()
    admin = User(first_name='bobby', last_name='clasemann', email='bob@example.com', person_key=1)
    admin2 = User(first_name='charlie', last_name='split', email='split@example.com', person_key=1)
    course_one = Course(course_id=4131, title='CSCI4131', credits=3)

    print("Hello")

    db.session.add(admin)
    db.session.add(admin2)
    db.session.add(course_one)
    db.session.commit()

    print(User.query.all())

    print("Goodbye")

    #return "Hello, World!"
    return render_template("index.html", title='Home Page')

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
