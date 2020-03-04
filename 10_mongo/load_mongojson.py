# Team TobyTop40
# Softdev2 pd9
# K10: Import/Export Bank
# 2020-03-04

from json import loads
from pymongo import MongoClient
from urllib.request import Request, urlopen

DEFAULT_FILENAME = "movies.json"

def load_mongo_json(filename,db):
    with open(filename,"r") as jsonfile:
        stringcontent = jsonfile.read()
        content = loads(stringcontent)
        db.insert(content)

if __name__ == "__main__":
    client = MongoClient()
    db = client.test
    TobyTop40 = db.TobyTop40
    load_mongo_json(DEFAULT_FILENAME,TobyTop40)
    print("complete!")


