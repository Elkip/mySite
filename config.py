import os

basedir = os.path.abspath(os.path.dirname(__file__))

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.getenv('EMAIL_USERNAME'),
    "MAIL_PASSWORD": os.getenv('EMAIL_PASSWORD')
}


class Config(object):
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    COUCHDB_SERVER = os.getenv('COUCHDB_SERVER')
    COUCHDB_DATABASE = os.getenv('COUCHDB_DATABASE')


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
