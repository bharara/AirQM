from flask import render_template, request
from myapp import app
from myapp.fun import *
from myapp.loc import DataBase, Location
from datetime import datetime, timedelta
import webbrowser

db = DataBase()


@app.route('/')
def Index():
    return render_template("home.html")


@app.route('/map', methods = ['GET', 'POST'])
def Map():
	if request.method == 'GET':
		st = datetime.today().date()
		end = (datetime.today() - timedelta(days = 7)).date()

	else:
		st = request.form['fromdate']
		end = request.form['todate']

	return render_template("map.html", title = "Map", lst = db.getMarkerList(st, end), cl = "map", st = str(st), end = str(end))

@app.route ('/Pollutants')
def Pollutants ():
	return render_template ("gasses.html", title = "Pollutants", list = db.getMarkerList(), d=db)

@app.route('/locations')
def Locations ():
	return render_template ("locations.html", title = "Locations", list= db.getMarkerNames())

@app.route('/locations/<loc>')
def Area (loc):
	return render_template("area.html", loc= Location (loc), title = loc.upper())


@app.route('/about')
def About ():
	return render_template ('about.html', title = "About Us")