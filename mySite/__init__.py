from flask import Flask
from flask_mail import Mail
from config import Config, mail_settings
from flask_sqlalchemy import SQLAlchemy


mail = Mail()
db = CouchDBManager()


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config.update(mail_settings)

    mail.init_app(app)
    db.setup(app)

    from mySite import contact
    from mySite import blog
    from mySite import site

    #app.register_blueprint(contact.bp)
    app.register_blueprint(blog.bp)
    app.register_blueprint(site.bp)

    # make "index" point at "/", which is handled by "site.home"
    app.add_url_rule("/", endpoint="site.home")

    return app
