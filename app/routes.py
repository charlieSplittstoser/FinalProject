from app import app
from flask import render_template

@app.route('/')
def index():
    #db.create_all()
   # admin = User(username='admin', email='admin@example.com')
   # guest = User(username='guest', email='guest@example.com')

    print("Hello")

  #  db.session.add(admin)
  #  db.session.add(guest)
  #  db.session.commit()

    #print(User.query.all())

    print("Goodbye")

    #return "Hello, World!"
    return render_template("base.html")
