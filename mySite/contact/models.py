import json
from datetime import datetime
from socket import inet_ntoa


class Contact():
    # id = db.Column(INTEGER(unsigned=True), autoincrement=True, primary_key=True)
    def __init__(self, name, email, message, ip):
        self.name = name
        self.email = email
        self.message = message
        self.subtime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.ip = ip

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def __repr__(self):
        return self.name + '\n' + self.email + '\n' + self.message + '\n' + \
               inet_ntoa(self.ip.to_bytes(4, byteorder='little', signed=False))
