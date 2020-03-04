#Team TobyTop40 Kiran & Connor
#SoftDev2 pd9
#K10 -- Import/Export Bank
#2020-03-04

import json
from pymongo import MongoClient

"""
Wikipedia Movie Data, by Peter Rust
This dataset contains information about a great number of American-made movies, including their title,genre,year,cast, and more
raw data can be found at: https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies.json

As can be found in a separate file, load_mongojson.py, our import mechanism can take any json file as its second argument, and employs json.loads to convert the data into a python dictionary and in turn load the data into the locally running MongoDB server, in the database TobyTop40 and the collection 'movies'
"""

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
    data = movies.find({"cast": {"$in": [ name ] } } )
    for movie in data:
       for key, value in movie.items():
           if key == "title":
               print("{title: %s}" % value)

#displays all the movies with in this genre
def moviesInThisGenre(genre):
    """prints all the movies with [genre] in its list of genres"""
    data = movies.find({"genres": {"$in": [genre] } })
    for movie in data:
       for key, value in movie.items():
           if key == "title":
               print("{title: %s}" % value)

#moviesFromTo(2000,2001)
#moviesThisPerformerIn("Tom Cruise")
#moviesInThisGenre("Horror")

requested_command = input("what would you like to search for? [year,performer,genre]: ")
if requested_command == "year":
    print("you requested: movies in a time interval")
    startyear = int(input("start year: "))
    endyear = int(input("end year: "))
    moviesFromTo(startyear,endyear)
elif requested_command == "performer":
    print("you requested: movies including a specified performer")
    name = input("performer name: ")
    moviesThisPerformerIn(name)
elif requested_command == "genre":
    print("you requested: movies in a specific genre")
    genre = input("genre: ")
    moviesInThisGenre(genre)
