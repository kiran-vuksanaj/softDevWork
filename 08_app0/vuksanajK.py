# Kiran Vuksanaj
# SoftDev1 pd1
# K08 -- Lemme Flask You Sump'n
# 2019-09-19
from flask import Flask
app = Flask(__name__) # constructor of the flask app

@app.route("/") #route for the function directly below, this is the root route
def hello_world():
    print(__name__) #prints to the debug console! not the webpage!
    return """
woah! <br />
it's looking as though this might be working! <br />
<a href="/submarine">where do we live?</a><br />
<a href="/muji">a cool store</a>
""" #this is the content of the page, a valid HTML snippet
    #it seems as though it works fine without a body though its not advisable

@app.route("/submarine") #another example of a route, what would be put in the url box
def submareen():
    print("we all live in a")
    return """
we all live in a yellow submarine! <br />
<a href="/">Go Home</a>
"""

@app.route("/muji") #see the two above, functions the same way
def mooj():
    return """
Apparently their staplers are greaT! <br />
<a href="/">Go Home</a>
    """

if __name__ == "__main__": # equivalent to C: `int main(){}` or Java: `main(String[] args){}`
    app.debug = True # show stuff on my console!
    app.run() # makes it all GO!
