from flask import Flask,render_template,request, jsonify
from databaseHandler import DBhandler
import json

app = Flask(__name__)

@app.route('/')
def mainPage():
    return render_template("login.html")

@app.route('/game',methods=['POST'])
def redirect():
    name = request.form["username"]
    return render_template("game.html",nm=name)

@app.route('/submit', methods=['POST'])
def AddRecord():
    dbObj = DBhandler("localhost", "root", "", "web")
    abc = json.loads(request.data)
    dbObj = DBhandler("localhost", "root", "", "web")
    dbObj.InsertRecord(abc["username"],abc["score"])
    return ""

@app.route('/fetch',methods=['GET'])
def AllRecords():
    dbObj = DBhandler("localhost", "root", "", "web")
    usersData = dbObj.getAllRecords()
    return jsonify(usersData)

@app.route('/redirectToScores')
def toScorePage():
    return render_template("scores.html",status = "1")

@app.route('/redirectTologin')
def backToLogin():
    return render_template("login.html")

@app.route('/a')
def temp():
    return render_template("scores.html")

@app.route('/checkValid')
def check():
    return render_template("login.html")

if __name__ == '__main__':
    app.run()
