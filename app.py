from flask import Flask, jsonify, render_template, request
import json

app = Flask(__name__)
jsondata = json.loads(open('./NBATeams.json').read())
data = jsondata["Teams"]

@app.route('/')
@app.route('/allteams/')
def teams_all():
    teamList=[]
    for element in data:
        teamList.append(element)
    result = jsonify(teamList)
    return render_template("index.html",teams=teamList)

@app.route('/allteams/<int:id>/')
def teams_id(id=''):
    teamList=[]
    for element in data:
        if element['id'] == id:
            teamList.append(element)
    result = jsonify(teamList)
    return render_template("index.html",teams=teamList)

@app.route('/allteams/<string:division>/')
def teams_division(division=''):
    teamList=[]
    for element in data:
        if element['division'] == division:
            teamList.append(element)
    result = jsonify(teamList)
    return render_template("index.html",teams=teamList)

@app.route('/allteams/<string:division>/<int:id>/')
def teams_div_id(division='', id=''):
    teamList=[]
    for element in data:
        if element['division'] == division and element['id'] == id:
            teamList.append(element)
    result = jsonify(teamList)
    return render_template("index.html",teams=teamList)

if __name__ == "___main__":
    app.run(debug=True,host='0.0.0.0')