from flask import Flask, render_template, request
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

@app.route("/movies")
def movie_query():
    if 'return_data' in request.args:
        print('request sent: return data')
        request_type = request.args['request_type']
        if request_type == 'performer':
            movies = moviesThisPerformerIn( request.args['query'] )
        elif request_type == 'genre':
            movies = moviesInThisGenre( request.args['query'] )
        elif request_type == 'year':
            print(request.args['start_year'],request.args['end_year'])
            movies = moviesFromTo( int(request.args['start_year']), int(request.args['end_year']) )
    else:
        movies = []
    print(movies)
    return render_template("movie.html",
                           movies=movies,
                           display_data = ('return_data' in request.args)
                           )

@app.route("/meteorites")
def rock_query():
    if 'return-data' in request.args:
        request_type = request.args['return-data']
        if request_type == 'name':
            data = name( request.args['first-letter'][0] )
        elif request_type == 'mass':
            data = mass( int(request.args['close-mass']) )
        elif request_type == 'biggest':
            data = biggest( int(request.args['min-mass']) )
        elif request_type == 'year':
            data = year( int(request.args['year-landed']) )
    else:
        data = []
    return render_template("rock.html",
                           rocks = data,
                           display_data = ('return_data' in request.args)
                           )

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
