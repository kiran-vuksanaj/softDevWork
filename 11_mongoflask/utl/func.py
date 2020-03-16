import json
from pymongo import MongoClient

client = MongoClient()
db = client.ExitWest
movies = db.movies
col = db.meteorites

# given a letter, return meteorites with names starting with that letter
def name(a):
    for r in col.find({}):
        if r['name'][0] == a:
            pprint.pprint(r)

# given a mass, return meteorites with mass within 50 kg of that mass
def mass(n):
	for r in col.find({ 'mass': {"$exists": True} }):
		if abs(n - float(r['mass'])) <= 50:
			pprint.pprint(r)

# given a mass, return meteorites with mass larger than that mass
def biggest(n):
	for r in col.find({ 'mass': {"$exists": True} }):
		if float(r['mass']) > n:
			pprint.pprint(r)

# given a year, return meteorites that landed in that year
def year(n):
	for r in col.find({ 'year': {"$exists": True} }):
		if float(r['year'][:4]) == n:
			pprint.pprint(r)

# the equator is at latitude 0 degrees
# each degree of latitude is 68.703 miles

# given a number of miles, return meteorites that landed within that
# number of miles from the equator in terms of latitude (given by reclat)

def lat(n):
	degrees = n / 68.703
	for r in col.find({ 'reclat': {"$exists": True} }):
		if abs(float(r['reclat'])) <= degrees:
			pprint.pprint(r)

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
