#Team TobyTop40 Kiran & Connor
#SoftDev2 pd9
#K10 -- Import/Export Bank
#2020-03-04

import json
from pymongo import MongoClient

client = MongoClient()
db = client.TobyTop40
movies = db.movies

#dislays all movies from a certain time range
def moviesFromTo(start, end):
    """prints all the movies from the years in the interval [start, end]"""
    data = movies.find({"year": {"$gte": start, "$lte": end}})
    for movie in data:
       for key, value in movie.items():
           if key == "title":
               print("{title: %s}" % value)

#displays all the movies a certain actor/actress was in
def moviesThisPerformerIn(name):
    """prints all the movies that includes the performer with [name] in its cast"""
    data = movies.find({"cast": {"$in": name}})
    for movie in data:
       for key, value in movie.items():
           if key == "title":
               print("{title: %s}" % value)

#displays all the movies with in this genre
def moviesInThisGenre(genre):
    """prints all the movies with [genre] in its list of genres"""
    data = movies.find({"genre": {"$in": genre}})
    for movie in data:
       for key, value in movie.items():
           if key == "title":
               print("{title: %s}" % value)

moviesFromTo(2000,2001)
#moviesThisPerformerIn("Tom Cruise")
#moviesInThisGenre("Comedy")
