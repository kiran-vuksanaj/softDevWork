# Kiran Vuksanaj
# SoftDev1 pd1
# K12 -- ECHO Echo echo
# 2019-09-26

from flask import Flask, render_template, request

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
    #print(request)
    #print(request.args)
    #ImmutableMultiDict([('words', u'woot!'), ('submit', u'Submit')])
    #print(request.method)
    #GET
    #print("hello_world")
    #print(request.headers)
    return render_template("response.html",
                            username=username,
                            request_method=request_method
                            )

if __name__ == "__main__":
    app.debug = True
    app.run()
