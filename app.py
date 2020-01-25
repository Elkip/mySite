from flask import Flask, render_template, request, redirect, flash, url_for
from flask_mail import Mail, Message
# from flask_sqlalchemy import SQLAlchemy
# import pymysql
from forms import ContactForm
import re
import os

# RECAPTCHA_PUBLIC_KEY = '6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J'
# RECAPTCHA_PRIVATE_KEY = '6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu'

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
# app.config['SQLALCHEMY_DATABASE_URL'] = 'mysql+pymysql://flask_mail:@localhost/flask_app_db'
# app.config['SQLALCHEMY_ECHO'] = True
#
# db = SQLAlchemy(app)

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.getenv('EMAIL_USERNAME'),
    "MAIL_PASSWORD": os.getenv('EMAIL_PASSWORD')
}

app.config.update(mail_settings)
mail = Mail(app)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == "POST":
        if not re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", form.email.data):
            flash('You must enter a valid email')
            return redirect(url_for('contact'))
        elif not form.validate():
            flash("Character limit Exceeded")
        else:
            with app.app_context():
                msg = Message(subject="New message from: " + form.name.data,
                              sender=app.config.get("MAIL_USERNAME"),
                              recipients=[os.getenv('MY_EMAIL')],
                              body="Message From: " + form.name.data + " \nReply Email: " + form.email.data +
                                   "\nMessage: " + form.message.data)
                mail.send(msg)
            return render_template('test.html', title="Message Sent", message="Message Sent!")
        # return redirect(url_for('test'))
    return render_template('contact.html', form=form)


@app.route('/test', methods=['GET', 'POST'])
def test():
    msg = 'Success'
    return render_template('test.html', title="Message Sent", message=msg)


if __name__ == '__main__':
    app.run(debug=False)
