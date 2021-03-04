from couchdb import Server
from flask import current_app


class MessageStore(object):
    def add_msg(self, contact):
        db_uri = str(current_app.config["COUCHDB_SERVER"])
        db_name = str(current_app.config["COUCHDB_DATABASE"])
        print("Creating connection from " + db_uri + "...")
        server = Server(db_uri)
        print("Connecting to db " + db_name + "...")
        db = server[db_name]
        print("Storing message...")
        db.save(contact.toJson())
        server.logout()
