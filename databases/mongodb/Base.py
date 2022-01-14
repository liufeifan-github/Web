# coding=utf-8
from pymongo import MongoClient


class MongoModel:
    DB = ''
    COLL = ''

    def __init__(self):
        mongo_str = "mongodb://127.0.0.1:27017"
        client = MongoClient(mongo_str, connect=False)
        self.db = client[self.DB]
        self.coll = self.db[self.COLL]

    def find(self, query):
        return self.coll.find(query)

    def find_one_data(self, query):
        return self.coll.find_one(query)

    def insert_one(self, data):
        return self.coll.insert_one(data)

    def update_one_data(self, query, update_data):
        if '$set' not in update_data:
            update_data = {'$set': update_data}
        return self.coll.update_one(query, update_data)

    def update_many_data(self, query, update_data):
        if '$set' not in update_data:
            update_data = {'$set': update_data}
        return self.coll.update_many(query, update_data)

    def find_and_insert_one(self, data, check_field):
        if not self.find_one_data({check_field: data[check_field]}):
            return self.insert_one(data)
        return True

    def delete_one(self, query):
        return self.coll.delete_one(query)
