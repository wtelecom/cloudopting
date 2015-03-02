
from engines import *


class ORM(object):

    def __init__(self, type, host, port, database):
        super(ORM, self).__init__()
        self.type = type
        self.host = host
        self.port = port
        self.database = database
        self.db = None
        self.select_type()

    def select_type(self):
        self.db = eval(self.type)(self.host, self.port, self.database)

    def get(self, **kwargs):
        self.db.get(kwargs)

    def get_all(self, **kwargs):
        self.db.get_all(kwargs)

    def create(self, **kwargs):
        return self.db.create(kwargs)

    def update(self, **kwargs):
        self.db.update(kwargs)

    def delete(self, **kwargs):
        self.db.delete(kwargs)