"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app.models import *
from flask import make_response, render_template, request, jsonify, send_file, g
from fileinput import filename
import psycopg2
import os
from app import app, db, ma
from flask import render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename

# Using JWT
import jwt
from flask import _request_ctx_stack
from functools import wraps
import datetime

#Schemas
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'password', 'name', 'email', 'location', 'biography', 'photo', 'date_joined')

user_schema = UserSchema()
users_schema = UserSchema(many=True)


class CarSchema(ma.Schema):
    class Meta:
        fields = ('id', 'description', 'make', 'model', 'colour', 'year', 'transmission', 'car_type', 'price', 'photo', 'user_id')

car_schema = CarSchema()
cars_schema = CarSchema(many=True)

class FavSchema(ma.Schema):
    class Meta:
        fields = ('id', 'car_id', 'user_id')

fav_schema = FavSchema()
favs_schema = FavSchema(many=True)



# Create a JWT @requires_auth decorator
# This decorator can be used to denote that a specific route should check
# for a valid JWT token before displaying the contents of that route.
def requires_auth(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    auth = request.headers.get('Authorization', None) # or request.cookies.get('token', None) 

    if not auth:
      return jsonify({'code': 'authorization_header_missing', 'description': 'Authorization header is expected'}), 401

    parts = auth.split()

    if parts[0].lower() != 'bearer':
      return jsonify({'code': 'invalid_header', 'description': 'Authorization header must start with Bearer'}), 401
    elif len(parts) == 1:
      return jsonify({'code': 'invalid_header', 'description': 'Token not found'}), 401
    elif len(parts) > 2:
      return jsonify({'code': 'invalid_header', 'description': 'Authorization header must be Bearer + \s + token'}), 401

    token = parts[1]
    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])

    except jwt.ExpiredSignatureError:
        return jsonify({'code': 'token_expired', 'description': 'token is expired'}), 401
    except jwt.DecodeError:
        return jsonify({'code': 'token_invalid_signature', 'description': 'Token signature is invalid'}), 401

    g.current_user = user = payload
    return f(*args, **kwargs)

  return decorated

###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")

@app.route('/api/register', methods=['POST'])
def register():
    username = request.json['username']
    password = request.json['password']
    name = request.json['name']
    email = request.json['email']
    location = request.json['location']
    biography = request.json['biography']
    photo = request.json['photo']
    
    users = Users(username, password, name, email, location, biography, photo)
    db.session.add(users)
    db.session.commit()
    return user_schema.jsonify(users)

@app.route('/api/auth/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']

    payload = {
        'username': username,
        'password': password
    }
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')

    resp= make_response(jsonify(message="Login Successful", token = token, ))
    resp.set_cookie('token', "Bearer " + token, httponly=True, secure=True)
    return resp



@app.route('/api/auth/logout', methods=['POST'])
@requires_auth
def logout():
    message = "Log out successful"
    return jsonify(message = message)

@app.route('/api/cars', methods=['POST'])
@requires_auth
def create_car():
    description = request.json['description']
    make = request.json['make']
    model = request.json['model']
    colour = request.json['colour']
    year = request.json['year']
    transmission = request.json['transmission']
    car_type = request.json['car_type']
    price = request.json['price']
    photo = request.json['photo']
    user_id = request.json['user_id']

    cars = Cars(description, make, model, colour, year, transmission, car_type, price, photo, user_id)
    db.session.add(cars)
    db.session.commit()
    return car_schema.jsonify(cars)

@app.route('/api/cars', methods=['GET'])
@requires_auth
def view_cars():
    all_cars = Cars.query.all()
    results = cars_schema.dump(all_cars)
    return jsonify(results)


@app.route('/api/cars/<car_id>', methods=['GET'])
@requires_auth
def view_car(car_id):
    car = Cars.query.get(car_id)
    return car_schema.jsonify(car)

@app.route('/api/cars/<car_id>/favourite', methods=['POST'])
@requires_auth
def add_fav(car_id):
    message = "Car Successfully Favourited"
    car_id = request.json['car_id']
    user_id = request.json['user_id']

    fav = Favourites(car_id, user_id)
    db.session.add(fav)
    db.session.commit()
    return jsonify(message = message, car_id = car_id)


@app.route('/api/search', methods=['GET'])
@requires_auth
def search():
    make = request.args.get('make')
    model = request.args.get('model')
    car = Cars.query.filter_by(make = make, model = model)
    return cars_schema.jsonify(car)


@app.route('/api/users/<user_id>', methods=['GET'])
@requires_auth
def get_user(user_id):
    user = Users.query.get(user_id)
    return user_schema.jsonify(user)

@app.route('/api/users/<user_id>/favourites', methods=['GET'])
@requires_auth
def get_fav(user_id):
    fav = Favourites.query.filter_by(user_id = user_id)
    return favs_schema.jsonify(fav)


###
# The functions below should be applicable to all Flask apps.
###

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return jsonify(error="Page Not Found"), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")