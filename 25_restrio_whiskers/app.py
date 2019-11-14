#Clement Chan & Kiran Vuksanaj
#SoftDev1 pd1
#K25 -- Getting more REST
#2019-11-13

from flask import Flask, render_template
import json
import urllib3

app = Flask(__name__)

key1 = "d5c33a6d038213d31fdfcc8aa681f15b6e8ee5971b2f223305aa65f3e841c01f"
key2 = ""
key3 = ""
req1 = "https://api.unsplash.com/photos/random?client_id=" + key1
req2 = "http://api.citybik.es/v2/networks/citi-bike-nyc"
req3 = ""

@app.route("/")
def hello_world():
    return render_template("home.html")

@app.route("/first")
#unsplash API random photo 
def displayFirst():
    http = urllib3.PoolManager()
    u = http.request('GET',req1)
    response = u.data.decode('utf-8')
    data = json.loads(response)
    return render_template("first.html",pic = data['urls']['small'])

@app.route("/second")
#
def displaySecond():
    http = urllib3.PoolManager()
    u = http.request('GET',req2)
    response = u.data.decode('utf-8')
    data = json.loads(response)
    station = data['network']['stations'][12]
    return render_template("second.html",freeBikes = station['free_bikes'],openSlots = station['empty_slots'],timestamp = station['timestamp'])

@app.route("/third")
#
def displayThird():
    http = urllib3.PoolManager()
    u = http.request('GET',"https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
    response = u.data.decode('utf-8')
    data = json.loads(response)
    deck_id = data['deck_id']
    u2 = http.request('GET','https://deckofcardsapi.com/api/deck/{}/draw/?count=5'.format(deck_id))
    response2 = u2.data.decode('utf-8')
    data2 = json.loads(response2)
    print(data2)
    return render_template("third.html",deck = data2['cards'])





    


if __name__ == "__main__":
    app.debug = True
    app.run()
