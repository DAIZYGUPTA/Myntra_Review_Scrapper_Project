from pymongo import MongoClient
import pandas as pd


class mongo_operation:
    def __init__(self, client_url: str, database_name: str):
        self.client = MongoClient(client_url)
        self.database = self.client[database_name]

    @property
    def _mongo_operation__connect_database(self):
        return self.database

    def bulk_insert(self, data: pd.DataFrame, collection_name: str):
        collection = self.database[collection_name]
        collection.insert_many(data.to_dict("records"))

    def find(self, collection_name: str):
        collection = self.database[collection_name]
        return list(collection.find())




"""
from pymongo import MongoClient
import pandas as pd


class mongo_operation:
    def __init__(self, client_url: str, database_name: str):
        self.client = MongoClient(client_url)
        self.database = self.client[database_name]

    @property
    def _mongo_operation__connect_database(self):
        # this is needed because your code uses this exact name
        return self.database

    def bulk_insert(self, data: pd.DataFrame, collection_name: str):
        collection = self.database[collection_name]
        collection.insert_many(data.to_dict("records"))

    def find(self, collection_name: str):
        collection = self.database[collection_name]
        return list(collection.find())

        """