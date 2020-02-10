from app import db
from sqlalchemy.dialects.mysql import INTEGER
from datetime import datetime


class Contact(db.Model):
    id = db.Column(INTEGER(unsigned=True), autoincrement=True, primary_key=True)
    name = db.Column(db.VARCHAR(100), nullable=False)
    email = db.Column(db.VARCHAR(100), nullable=False)
    message = db.Column(db.VARCHAR(250), nullable=False)
    subtime = db.Column(db.DATETIME, nullable=False, default=datetime.utcnow())
    ip = db.Column(INTEGER(unsigned=True))

    def __repr__(self):
        return (self.id + '\n' + self.name + '\n' + self.email + '\n' + self.message + '\n' +
                self.subtime + '\n' + self.ip)
