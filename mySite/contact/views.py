import os
import re
from socket import inet_aton

from flask import request, redirect, render_template, flash, url_for, Blueprint, current_app
from flask_mail import Message
import logging

from .dao import MessageStore
from .forms import ContactForm
from .models import Contact

from mySite import mail


bp = Blueprint("contact", __name__)


@bp.route('/contact', methods=['GET', 'POST'])
def contact():
    db_server = current_app.config["COUCHDB_SERVER"]
    db_name = current_app.config["COUCHDB_DATABASE"]

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

            headers_list = request.headers.getlist("X-Forwarded-For")
            user_ip = headers_list[0] if headers_list else request.remote_addr
            coded_ip = int.from_bytes(inet_aton(user_ip), byteorder='little', signed=False)

            try:
                document = Contact(name=form.name.data, email=form.email.data, message=form.message.data, ip=coded_ip)
                logging.info(document)
                couch = MessageStore(db_server, db_name)
                couch.add_msg(document)
                mail.send(msg)
            except Exception as e:
                logging.error(e)
                return render_template('contact/test.html', title="Try again later.", message="Something went wrong."
                                                                                              " Failure logged.")
            return render_template('contact/test.html', title="Message Sent", message="Success! Thanks for coming.")
    return render_template('contact/contact.html', form=form)


@bp.route('/test', methods=['GET'])
def test():
    return render_template('contact/test.html', title="Congrats", message="You found the test page.")
