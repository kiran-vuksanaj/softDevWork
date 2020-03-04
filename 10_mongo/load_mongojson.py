# Team TobyTop40
# Softdev2 pd9
# K10: Import/Export Bank
# 2020-03-04

from json import loads
from pymongo import MongoClient
from sys import argv

FILENAME = "movies.json"

def load_mongo_json(filename,coll):
    with open(filename,"r") as jsonfile:
        stringcontent = jsonfile.read()
        content = loads(stringcontent)
        coll.insert(content)

def prune_data(coll):
    pass
        
if __name__ == "__main__":
    client = MongoClient()
    db_tt4 = client.TobyTop40
    coll_movies = db_tt4.movies
    if len(argv) > 1:
        FILENAME = argv[1]
    print("loading json data from" , FILENAME ) 
    load_mongo_json(FILENAME,coll_movies)
    print("data successfully loaded\nlook in database 'TobyTop40', collection 'movies'")


