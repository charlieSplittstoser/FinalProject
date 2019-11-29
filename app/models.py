from app import db

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


### MODELS ###
class User(db.Model):
  __tablename__ = 'User'
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  first_name = db.Column(db.String(80), unique=False, nullable=False)
  last_name = db.Column(db.String(80), unique=False, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  person_key = db.Column(db.Boolean, unique=False, nullable=False)

  def __repr__(self):
      return '<User %r>' % self.username

  #def set_password(self, password):
      #self.password_hash = generate_password_hash(password)

  #def check_password(self, password):
      #return check_password_hash(self.password_hash, password)

class Course(db.Model, Base):
  __tablename__ = 'Course'
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  course_id = db.Column(db.Integer, unique=True, nullable=False)
  title = db.Column(db.String(50), unique=False, nullable=False)
  credits = db.Column(db.Integer, unique=False, nullable=False)

  enroll = relationship(
    "User",
    secondary=Table'enrolled', Base.metadata,
      Column('user_id', Integer, ForeignKey('User.id'), primary_key=True),
      Column('course_id', Integer, ForeignKey('Course.id'), primary_key=True))


@app.route('/')
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

  return render_template("base.html")
        
