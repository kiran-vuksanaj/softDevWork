# Team TobyTop40
# Softdev2 pd9
# K10: Import/Export Bank
# 2020-03-04

from json import loads
from pymongo import MongoClient
from urllib.request import Request, urlopen

DEFAULT_URL = "https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies.json"

def load_mongo_json(url,db):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = loads(urlopen(req).read().decode('utf-8'))
    db.insert(response)

if __name__ == "__main__":
    client = MongoClient()
    db = client.test
    TobyTop40 = db.TobyTop40
    load_mongo_json(DEFAULT_URL,TobyTop40)
    print("complete!")


