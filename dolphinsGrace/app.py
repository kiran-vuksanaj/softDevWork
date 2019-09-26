from flask import Flask, render_template, request
import cgi
app = Flask(__name__)

@app.route("/")
def hello_world():
    print(__name__)
    #print(request)
    return render_template("form.html")

@app.route("/auth")
def authPage():
    req = request.args["words"]
    #ImmutableMultiDict([('words', u'woot!'), ('submit', u'Submit')])
    return "it seems to me this has worked! Your word: " + req

if __name__ == "__main__":
    app.debug = True
    app.run()
