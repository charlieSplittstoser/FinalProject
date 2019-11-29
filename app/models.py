from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import create_engine, Table
from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

### MODELS ###

#db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

#Base.query = db_session.query_property()

class User(UserMixin, db.Model):
  __tablename__ = 'User'
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  first_name = db.Column(db.String(80), unique=False, nullable=False)
  last_name = db.Column(db.String(80), unique=False, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  person_key = db.Column(db.Boolean, unique=False, nullable=False)

  def __repr__(self):
      return '<first_name %r, last_name %r, email %r>' % (self.first_name, self.last_name, self.email)


  def set_password(self, password):
        self.password_hash = generate_password_hash(password)
  def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Course(db.Model):
  __tablename__ = 'Course'
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  course_id = db.Column(db.Integer, unique=True, nullable=False)
  title = db.Column(db.String(50), unique=False, nullable=False)
  credits = db.Column(db.Integer, unique=False, nullable=False)

  def __repr__(self):
    return '<Course %r, Credits %r>' % (self.title, self.credits)


class Enrollment(db.Model):
  __tablename__ = 'Enrollment'
  __table_args__ = (db.UniqueConstraint('user_id', 'course_id', name='enrolled'),)
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  user_id = Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
  user = db.relationship("User")
  course_id = Column(db.Integer, db.ForeignKey('Course.id'), nullable=False)
  course = db.relationship("Course")

  
  def __repr__(self):
    return '<Course %r, User %r>' % (self.course_id, self.user_id)
  #enroll = relationship(
    #"User",
    #secondary=Table'enrolled', Base.metadata,
    #  Column('user_id', Integer, ForeignKey('User.id'), primary_key=True),
    #  Column('course_id', Integer, ForeignKey('Course.id'), primary_key=True))


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
