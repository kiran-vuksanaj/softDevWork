from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    print(__name__)
    return """
woah! <br />
it's looking as though this might be working! <br />
<a href="/submarine">where do we live?</a><br />
<a href="/muji">a cool store</a>
"""

@app.route("/submarine")
def submareen():
    print("we all live in a")
    return """
we all live in a yellow submarine! <br />
<a href="/">Go Home</a>
"""

@app.route("/muji")
def mooj():
    return """
Apparently their staplers are greaT! <br />
<a href="/">Go Home</a>
    """

if __name__ == "__main__":
    app.debug = True
    app.run()
