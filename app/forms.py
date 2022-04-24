# Add any form classes for Flask-WTF here
import email
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextAreaField, SubmitField, validators, SelectField, IntegerField, FileField, PasswordField
from wtforms.validators import DataRequired, InputRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired


class UserForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    name = StringField('Name', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])
    location = StringField('Location',validators=[InputRequired()])
    biography = StringField('Biography',validators=[InputRequired()])
    photo = FileField('Image', validators=[FileRequired(),FileAllowed(['jpg','png'], 'Images only!')])
    submit = SubmitField("Add User")