import logging
import os

basedir = os.path.abspath(os.path.dirname(__file__))

mail_settings = {
    'MAIL_SERVER': 'smtp.gmail.com',
    'MAIL_PORT': 465,
    'MAIL_USE_TLS': False,
    'MAIL_USE_SSL': True,
    'MAIL_USERNAME': os.getenv('EMAIL_USERNAME'),
    'MAIL_PASSWORD': os.getenv('EMAIL_PASSWORD')
}


class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv('SECRET_KEY')
    COUCHDB_SERVER = os.getenv('COUCHDB_SERVER')
    COUCHDB_DATABASE = os.getenv('COUCHDB_DATABASE')


class ProductionConfig(Config):
    DEBUG = False

    LOGGING_CONFIG = dict(
        version=1,
        formatters={
            'f': {'format': '%(asctime)s %(name)-13s %(levelname)-8s %(message)s'}
        },
        handlers={
            'h': {'class': 'logging.StreamHandler',
                  'formatter': 'f',
                  'level': logging.INFO}
        },
        root={
            'handlers': ['h'],
            'level': logging.INFO,
        },
    )


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

    DEV_LOGGING_CONFIG = dict(
        version=1,
        formatters={
            'f': {'format': '%(asctime)s %(name)-13s %(levelname)-8s %(message)s'}
        },
        handlers={
            'h': {'class': 'logging.StreamHandler',
                  'formatter': 'f',
                  'level': logging.DEBUG}
        },
        root={
            'handlers': ['h'],
            'level': logging.DEBUG,
        },
    )
