from flask import Flask, render_template
import json
import urllib3

app = Flask(__name__)

req = "https://api.nasa.gov/planetary/earth/imagery/?lon=-74.01&lat=40.72&api_key=59euw1WUxK6UhUpsFpBjTz3OTcZhNiqSKgsBzXAz"




@app.route("/")
def hello_world():
    http = urllib3.PoolManager()
    u = http.request('GET',req)
    response = u.data.decode('utf-8')
    data = json.loads(response)
    return render_template("model_tmplt.html",pic = data['url'])

    


if __name__ == "__main__":
    app.debug = True
    app.run()
