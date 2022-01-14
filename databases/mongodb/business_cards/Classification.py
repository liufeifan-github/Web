# coding=utf-8
from databases.mongodb.Base import MongoModel


class Classification(MongoModel):
    DB = "business_cards"
    coll = "classification"

    def cla_insert(self, data):
        query = {"cla_id": data['cla_id']}
        if not self.find_one_data(query):
            self.insert_one(data)
        return True

    def cla_delete(self, query):
        if self.delete_one(query):
            return True
        return False

    def cla_query(self, query):
        return self.find(query)
