#Bayle SMith-Salzberg
#SoftDev1 pd8
#HW02 -- Fill Your Flask
#2016-09-21

from flask import Flask

app=Flask(__name__)

@app.route("/")
def hello_world():
    return "goodbye world"

@app.route("/catssss")
def kitty():
    return '''
<img src = http://www.siberiancat.com/uploads/1/2/7/0/12700455/8887087_orig.jpg>
'''
    
@app.route("/random")
def asdf():
    return "did it work?"


def foo():
    print "bayle"
if __name__=="__main__":
    app.run()
