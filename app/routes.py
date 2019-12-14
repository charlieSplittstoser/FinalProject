from app import app, db
from flask import render_template, flash, request, redirect, url_for, Response
import requests
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Course, Enrollment
from app.forms import LoginForm, RegistrationForm, LibraryForm
from flask_wtf import FlaskForm
from werkzeug.urls import url_parse
import random


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
    course7 = Course(course_id='WRIT1401', title='Freshmen Writing', instructor='Sadie Johnson', credits=3)
    course8 = Course(course_id='MATH1371', title='Calculus I', instructor='Jennie Morgan', credits=4)
    course9 = Course(course_id='MATH1372', title='Calculus II', instructor='Denis Bashkirov', credits=4)
    course10 = Course(course_id='CSCI1101', title='Introduction to Computer Science', instructor='Tim Wrenn', credits=3)
    course11 = Course(course_id='CSCI4707', title='Principles of Database Systems', instructor='Jaideep Srivistava', credits=3)
    course12 = Course(course_id='BUS101', title='Introduction to Business', instructor='Mark Widdell', credits=3)

    db.session.add(admin)
    db.session.add(admin2)
    db.session.add(course1)
    db.session.add(course2)
    db.session.add(course3)
    db.session.add(course4)
    db.session.add(course5)
    db.session.add(course6)
    db.session.add(course7)
    db.session.add(course8)
    db.session.add(course9)
    db.session.add(course10)
    db.session.add(course11)
    db.session.add(course12)
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

@app.route('/schedule', defaults={'term': 'Spring 2020'})
@app.route('/schedule/<term>')
@login_required
def schedule(term):
    try:
        enrollment = db.session.query(Enrollment, Course).filter(Enrollment.course_id == Course.id, Enrollment.user_id == current_user.id)
    except Exception as e:
        enrollment = []
    return render_template("schedule.html", title="Course Schedule", enrollment=enrollment, term=term)


@app.route('/catalog', methods=['GET', 'POST'])
def catalog():
    enrolled = request.form.get('enrolled') #if key doesn't exist, returns None
    return render_template("catalog.html", title="Course Catalog", courses=Course.query.all(), enrolled=enrolled)

@app.route('/enrollUser/<user_id>/<course_id>')
def enrollUser(user_id, course_id):
    enroll1 = Enrollment(user_id=user_id, course_id=course_id, term="Spring 2020", grade="IP")
    db.session.add(enroll1)
    try:
        db.session.commit()
        return "Success"
    except Exception as e:
        print(e)
        return "Failed"

@app.route('/enroll/<id>')
@login_required
def enroll(id):
    return render_template("enroll.html", title="Enroll Course", course=Course.query.get(id), user_id=current_user.id)

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
        populatePreviousSemesters(user.email)
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
            flash('Invalid username or password!')
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

def populatePreviousSemesters(email):
    user = User.query.filter_by(email=email).first()
    courses = db.session.query(Course.id).all()
    print(courses)
    random.shuffle(courses)
    print(courses)
    grades = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-"]
    term = "Spring 2019"
    x = 0
    for course in courses:
        enroll = Enrollment(user_id=user.id, course_id=course[0], term=term, grade=random.choice(grades))
        db.session.add(enroll)
        x += 1
        if x is 4:
            term = "Fall 2019"
        elif x is 8:
            break
    db.session.commit()
