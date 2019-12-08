from app import app, db
from flask import render_template, flash, request, redirect, url_for, Response
import requests
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Course, Enrollment
from app.forms import LoginForm, RegistrationForm, LibraryForm
from flask_wtf import FlaskForm
from werkzeug.urls import url_parse


@app.route('/initdb')
def initdb():
    db.create_all()
    admin = User(first_name='bobby', last_name='clasemann', email='bob@example.com', person_key=1)
    admin2 = User(first_name='charlie', last_name='split', email='split@example.com', person_key=1)
    course1 = Course(course_id='CSCI4131', title='Internet Programming', instructor='Brad Miller', credits=3)
    course2 = Course(course_id='CSCI4041', title='Algorithms & Data Structures', instructor='James Parker', credits=4)
    course3 = Course(course_id='CSCI2041', title='Adv. Programming Principles', instructor='Gopalan Nadathur', credits=3)
    course4 = Course(course_id='ENGL1001W', title='Introduction to Literature', instructor='Chris Kamerbeek', credits=3)
    course5 = Course(course_id='GEOG1403', title='Biogeography', instructor='Kurt Kipfmueller', credits=4)
    course6 = Course(course_id='JOUR3745', title='Journalism', instructor='Ruth Defoster', credits=3)

    enroll1 = Enrollment(user_id=0, course_id=0)
    db.session.add(admin)
    db.session.add(admin2)
    db.session.add(course1)
    db.session.add(course2);
    db.session.add(course3);
    db.session.add(course4);
    db.session.add(course5);
    db.session.add(course6);
    db.session.add(enroll1);
    db.session.commit()
    return "DB initialized"

@app.route('/')
@app.route('/index')
#@login_required
def index():
    print("Hello")

    print(User.query.all())
    print(Course.query.all())
    print(Enrollment.query.all())

    print("Goodbye")

    #return "Hello, World!"
    return render_template("index.html", title='Home')

@app.route('/catalog')
def catalog():
    return render_template("catalog.html", title="Course Catalog", courses=Course.query.all())

@app.route('/enroll/<id>')
def enroll(id):
    return render_template("enroll.html", title="Enroll Course", course=Course.query.get(id))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(first_name=form.first_name.data, last_name=form.last_name.data,
                    email=form.email.data, person_key=0) #Default as student for now CHANGE LATER
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/library', methods=['GET', 'POST'])
def library():
    form = LibraryForm()
    return render_template("library.html", form=form)


@app.route('/proxy/<name>', methods=['GET', 'POST'])
def proxy(name):
    result = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={name}')
    resp = Response(result.text)
    print(resp)
    resp.headers['Content-Type'] = 'application/json'
    return resp


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
