# Add any model classes for Flask-SQLAlchemy here
from . import db
import datetime
from werkzeug.security import generate_password_hash

class Users(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(255))
    name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    location = db.Column(db.String(80))
    biography = db.Column(db.String(80))
    photo = db.Column(db.String(80))
    date_joined = db.Column(db.DateTime, default = datetime.datetime.now)

    def __init__(self, username, password, name, email, location, biography, photo):
        self.username = username
        self.password = generate_password_hash(password, method='pbkdf2:sha256')
        self.name = name
        self.email = email
        self.location = location
        self.biography = biography
        self.photo = photo

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)

class Cars(db.Model):
    __tablename__ = 'Cars'
    id = db.Column(db.Integer,primary_key = True)
    description = db.Column(db.String(1000))
    make = db.Column(db.String(80))
    model = db.Column(db.String(80))
    colour = db.Column(db.String(80))
    year = db.Column(db.String(80))
    transmission = db.Column(db.String(80))
    car_type = db.Column(db.String(80))
    price = db.Column(db.Float)
    photo = db.Column(db.String(80))
    user_id = db.Column(db.Integer)

    def __init__(self, description, make, model, colour, year, transmission, car_type, price, photo, user_id):
        self.description = description
        self.make = make
        self.model = model
        self.colour = colour
        self.year = year
        self.transmission = transmission
        self.car_type = car_type
        self.price = price
        self.photo = photo
        self.user_id = user_id

    def get_id(self):
            return str(self.id)  # python 3 support

class Favourites(db.Model):
    __tablename__ = 'Favourites'
    id = db.Column(db.Integer,primary_key = True)
    car_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)

    def __init__(self, car_id, user_id):
        self.car_id = car_id
        self.user_id = user_id

    def get_id(self):
        return str(self.id)  # python 3 support"""

