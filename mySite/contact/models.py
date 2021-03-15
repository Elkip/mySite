from datetime import datetime
from socket import inet_ntoa


class Contact:

    def __init__(self, name, email, message, ip):
        self._id = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
        self.name = name
        self.email = email
        self.message = message
        self.ip = ip

    def __repr__(self):
        return self._id + '\n' + self.name + '\n' + self.email + '\n' + self.message + '\n' + \
               inet_ntoa(self.ip.to_bytes(4, byteorder='little', signed=False))
