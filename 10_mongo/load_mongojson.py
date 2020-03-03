# Team TobyTop40
# Softdev2 pd9
# K10: Import/Export Bank
# 2020-03-04

from json import loads
from pymongo import MongoClient

def load_mongoclient():
    client = MongoClient()
    db = client.test
    JDB = db.JDB

def load_mongo_json(filename):
    pass

if __name__ == "__main__":
    load_mongoclient()
    load_mongo_json("testfile.json")
    print("complete!")


