from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators


class ContactForm(FlaskForm):
    name = StringField('Name', [validators.required(), validators.length(max=100)])
    email = StringField('Email', [validators.required(), validators.length(max=100)])
    message = TextAreaField('Message (500 Character Limit)', [validators.required(), validators.length(max=500)])
