from flask import Flask
from flask_mail import Mail

from config import mail_settings, ProductionConfig

mail = Mail()


def create_app():
    app = Flask(__name__)
    app.config.from_object(ProductionConfig)
    app.config.update(mail_settings)

    mail.init_app(app)

    from mySite import contact
    from mySite import blog
    from mySite import site

    app.register_blueprint(contact.bp)
    app.register_blueprint(blog.bp)
    app.register_blueprint(site.bp)

    # make "index" point at "/", which is handled by "site.home"
    app.add_url_rule("/", endpoint="site.home")

    return app
