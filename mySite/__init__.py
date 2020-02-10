from flask import Flask, render_template, request, redirect, flash, url_for
# from flask_mail import Mail
from config import Config
# from flask_sqlalchemy import SQLAlchemy


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object(Config)
    # db = SQLAlchemy(app)
    # app.config.update(mail_settings)
    # mail = Mail(app)

    from mySite import contact
    from mySite import blog
    from mySite import site

    app.register_blueprint(contact.bp)
    app.register_blueprint(blog.bp)
    app.register_blueprint(site.bp)

    # make "index" point at "/", which is handled by "site.home"
    app.add_url_rule("/", endpoint="site.home")

    return app
