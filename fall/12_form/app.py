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
    username = request.args["username"]
    request_method = request.method
    #ImmutableMultiDict([('words', u'woot!'), ('submit', u'Submit')])
    return render_template("response.html",
                            username=username,
                            request_method=request_method
                            )

if __name__ == "__main__":
    app.debug = True
    app.run()
