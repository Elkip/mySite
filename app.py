from flask import Flask, render_template, request, redirect, flash, url_for
from flask_mail import Mail, Message
from config import Config, mail_settings
from flask_sqlalchemy import SQLAlchemy
from socket import inet_ntoa, inet_aton
from forms import ContactForm
import re

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
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
                headers_list = request.headers.getlist("X-Forwarded-For")
                user_ip = headers_list[0] if headers_list else request.remote_addr
            return render_template('test.html', title="Message Sent", message=user_ip)
    return render_template('contact.html', form=form)


@app.route('/test', methods=['GET', 'POST'])
def test():
    msg = 'Success'
    return render_template('test.html', title="Message Sent", message=msg)


if __name__ == '__main__':
    app.run(debug=False)
