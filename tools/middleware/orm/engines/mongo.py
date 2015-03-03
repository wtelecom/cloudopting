from pymongo import MongoClient
from bson.objectid import ObjectId


class Engine(object):
    
    def __init__(self, host, port, database):
        super(Engine, self).__init__()
        self.client = MongoClient(host, port)
        self.db = self.client[database]

    def get(self, kwargs):
        if kwargs is not None:
            collection = self.db[kwargs['collection']]
            dc = dict((k, v) for k,v in kwargs.items() if k != 'collection')
            dc_t = dict(('_id', ObjectId(v)) for k,v in dc.items() if k == 'id')
            return collection.find_one(dc_t)

    def get_all(self, kwargs):
        dc = []
        if kwargs is not None:
            collection = self.db[kwargs['collection']]
            for doc in collection.find():
                doc['_id'] = str(doc['_id'])
                dc.append(doc)
            return dc

    def create(self, kwargs):
        if kwargs is not None:
            collection = self.db[kwargs['collection']]
            dc = dict((k, v) for k,v in kwargs.items() if k != 'collection')
            return collection.insert(dc)

    def update(self, kwargs):
        if kwargs is not None:
            collection = self.db[kwargs['collection']]
            dc = dict((k, v) for k,v in kwargs.items() if k != 'collection')
            collection.update(dc['search'], {'$set':{"fields.$":dc['change']}}, upsert=False, multi=True)
            return True

