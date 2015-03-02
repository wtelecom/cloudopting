from pymongo import MongoClient


class Engine(object):
    
    def __init__(self, host, port, database):
        super(Engine, self).__init__()
        self.client = MongoClient(host, port)
        self.db = self.client[database]
        self.collection = None

    def get(self, **kwargs):
        if kwargs is not None:
            self.collection = self.db[kwargs['collection']]

    def create(self, kwargs):
        collection = self.db[kwargs['collection']]
        d = dict((k, v) for k,v in kwargs.items() if k != 'collection')
        return collection.insert(d)

