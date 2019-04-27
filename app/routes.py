from flask import render_template
from run import app
from app.fun import getMarkerList

key = "AIzaSyBcOf3GLe78ZNRLIEOxZ9zzzWMnYXo5tiQ"
url = "https://maps.googleapis.com/maps/api/js?key=AIzaSyBcOf3GLe78ZNRLIEOxZ9zzzWMnYXo5tiQ&callback=initMap"

@app.route('/')
def Index():
    return render_template("home.html", url = url)


@app.route('/map')
def Map():
	return render_template("map.html", title = "Map", data = getMarkerList (), cl = "map")