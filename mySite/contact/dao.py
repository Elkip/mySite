from couchdb import Server
import json
import logging


class MessageStore(object):
    def __init__(self, db_server, db_name):
        self.db_server = db_server
        self.db_name = db_name

    def add_msg(self, contact):
        db_uri = self.db_server
        db_table = self.db_name
        logging.debug("Creating connection from " + db_uri + "...")
        server = Server(db_uri)
        logging.debug("Connecting to db " + db_table + "...")
        db = server[db_table]

        j = json.dumps(contact.__dict__)
        logging.debug(str(type(j)))
        logging.info("Storing message: " + j)
        db.save(json.loads(j))
