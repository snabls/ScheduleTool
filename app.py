from flask import Flask, flash, redirect, render_template, request, session, url_for
import json
import datetime
import os
days = {"Mon": "Lun", "Tue": "Mar", "Wed": "Mer", "Thu": "Gio", "Fri": "Ven", "Sat": "Sab"}
hours = {'08' : 'I', '09' : 'II', '10' : 'III', '11' : 'IV', '12' : 'V', '13' : 'VI'}
daynumber = {'Lun': 0, 'Mar': 1, 'Mer': 2, 'Gio': 3, 'Ven': 4, 'Sab': 5}

def getInfo(day, hour):
    if day not in days or hour not in hours:
        return [7, 7]
    return [days[day], hours[hour]]

def getRoom(data):
    info = getInfo(datetime.datetime.now().strftime("%a"), datetime.datetime.now().strftime("%H"))
    return dat['orario']
    
with open("teachers.txt", "r") as f:
    names = f.read().splitlines()
app = Flask(__name__)
app.secret_key = "chiavesegretasnabl"


@app.route("/")
def home():
    return render_template("index.html", namesArray=names)

@app.route("/schedule")
def schedule():
    name = request.args.get("name")
    if name:
        filename = f"{name}.json"
        filepath = os.path.join("schedules", filename)
        if os.path.exists(filepath):
            with open(filepath, "r") as f:
                data = json.load(f)
            
            
            return render_template("schedule.html", json=data, name=name)
    return "Schedule not found", 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
