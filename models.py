import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

database_path = os.environ['DATABASE_URL']
db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    print("database_path - ", database_path)
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''
Person
Have title and release year
'''
class Person(db.Model):
  __tablename__ = 'People'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  email = Column(String)
  catchphrase = Column(String)

  def __init__(self, name, email, catchphrase=""):
    self.name = name
    self.email = email
    self.catchphrase = catchphrase

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'email': self.email,
      'catchphrase': self.catchphrase}
