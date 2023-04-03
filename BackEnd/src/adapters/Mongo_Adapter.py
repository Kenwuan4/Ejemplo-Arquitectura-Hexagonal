from pymongo import MongoClient
from ports.Persistance_Port import Persistance_port


class MongoAdapter(Persistance_port):
    def __init__(self, mongo_uri, database_name, collection_name):
        self.client = MongoClient(mongo_uri)
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]

    def find_email(self, email):
        persona = self.collection.find_one(
            {'email': email})
        return persona

    def autenticate_user(self, email, password):
        try:
            persona = self.collection.find_one(
                {'email': email, 'password': password})

            return persona
        except:
            return False

    def save(self, email, password):
        email_val = self.find_email(email=email)

        if email_val is not None:
            return False
        else:
            data = {'email': email, 'password': password}
            self.collection.insert_one(data)

            return self.find_email(email=email)
