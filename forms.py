from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, TextAreaField, validators
from wtforms.validators import DataRequired


# RECAPTCHA_PUBLIC_KEY = ''
# RECAPTCHA_PRIVATE_KEY = ''


class ContactForm(FlaskForm):
    name = StringField('Name', [validators.required(), validators.length(max=100)])
    email = StringField('Email', [validators.required(), validators.length(max=100)])
    message = TextAreaField('Message (500 character limit)', [validators.required(), validators.length(max=500)])
    # captcha = RecaptchaField()
