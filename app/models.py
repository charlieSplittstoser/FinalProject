from app import db

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


### MODELS ###
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))


    def __repr__(self):
        return '<User %r>' % self.username

    #def set_password(self, password):
        #self.password_hash = generate_password_hash(password)

    #def check_password(self, password):
        #return check_password_hash(self.password_hash, password)
