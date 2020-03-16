from flask import Flask, render_template
import pymongo, json, pprint
from bson.json_util import loads
from utl.func import name, mass, biggest, year, lat, moviesFromTo, moviesThisPerformerIn, moviesInThisGenre

client = pymongo.MongoClient('localhost', 27017) # port 27017
db = client['ExitWest'] # team name as database name
rocks = db['meteorites'] # creating collection for NASA data
films = db['movies']

if films.count() == 0:
    with open('movies.json','r') as jsonfile:
        stringcontent = jsonfile.read()
        content = loads(stringcontent)
        films.insert(content)

if rocks.count() == 0:
    file = open("meteorites.json", "r")
    data = file.readlines()
    for line in range(len(data)):
        if line == 0:
            rocks.insert_one(loads(data[line]))
        else:
            rocks.insert_one(loads(data[line][1:]))

app = Flask(__name__)

@app.route("/")
def hello_world():
    print("RISE AND SHINE, TIME TO GRIND")
    return render_template("base.html")

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
