from flask import request, redirect, render_template, flash, url_for, Blueprint
from flask_mail import Message
from socket import inet_ntoa, inet_aton
from .forms import ContactForm
# from models import Contact
import re
import os

from mySite import mail


bp = Blueprint("contact", __name__)


@bp.route('/contact', methods=['GET', 'POST'])
def contact():
    print(os.getenv("SECRET_KEY"))
    form = ContactForm()
    if request.method == "POST":
        if not re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", form.email.data):
            flash('You must enter a valid email')
            return redirect(url_for('contact.contact'))
        elif not form.validate():
            flash("Character limit Exceeded")
        else:
            msg = Message(subject="New message from: " + form.name.data,
                          sender=os.getenv("EMAIL_USERNAME"),
                          recipients=[os.getenv('MY_EMAIL')],
                          body="Message From: " + form.name.data + " \nReply Email: " + form.email.data +
                               "\nMessage: " + form.message.data)
            mail.send(msg)
            headers_list = request.headers.getlist("X-Forwarded-For")
            user_ip = headers_list[0] if headers_list else request.remote_addr
            coded_ip = inet_aton(user_ip)
            # user = Contact(name=form.name.data, email=form.name.data, message=form.message.data, ip=coded_ip)
            return render_template('contact/test.html', title="Message Sent", message="Success! Thanks for coming.")
    return render_template('contact/contact.html', form=form)


@bp.route('/test', methods=['GET', 'POST'])
def test():
    msg = 'Success'
    return render_template('contact/test.html', title="Message Sent", message=msg)
