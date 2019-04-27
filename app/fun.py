import aqi
from datetime import datetime, timedelta


## Marker Functions

def markerColor (aqi):
	if aqi < 51:
		return "Green"
	elif aqi < 101:
		return "Yellow"
	elif aqi < 151:
		return "Orange"
	elif aqi < 200:
		return "Red"
	elif aqi < 301:
		return "Purple"
	else:
		return "DarkRed"


def getMarkerList ():
	return [["{lat: 33.684, lng: 73.0479}", "m1", "red"], ["{lat: 33.712, lng: 73.0979}", "m2", "blue"] ]
	lst = []
	for title, cord in getMarkersFromDB ():
		aqi = getLastWeekAQI (title)
		color = markerColor(aqi)
		lst.append([cord, title, color])

	return lst

## AQI Calulator
def calculateAQI (oz, pr, co, so2, no2):
	myaqi = aqi.to_aqi([
		(aqi.POLLUTANT_CO_8H, str(co)),
		(aqi.POLLUTANT_PM25, str(pr)),
		(aqi.POLLUTANT_O3_8H, str(oz)),
		(aqi.POLLUTANT_SO2_1H, str(so2)),
		(aqi.POLLUTANT_NO2_1H, str(no2))
		])

	return myaqi

## Gasses Functions
def getGasesAVG (loc, startDT, endDT = datetime.now()):
	s = """SELECT avg(index)
	FROM Data
	WHERE time >= startDT
	AND time <= endDT
	GROUP BY location;
	"""
	return 0, 0, 0, 0, 0


## Get AQI of a Location

def getAQI (loc, startDT, endDT = datetime.now()):
	g1, g2, g3, g4, g5 = getGasesAVG (loc, startDT, endDT)
	return calculateAQI (g1, g2, g3, g4, g5)

def getTodayAQI (loc):
	return getAQI (loc, datetime.now(), datetime.today() - timedelta(days = 1))

def getLastWeekAQI (loc):
	return getAQI (loc, datetime.now(), datetime.today() - timedelta(days = 7))

def getLastMonthAQI (loc):
	return getAQI (loc, datetime.now(), datetime.today() - timedelta(days = 30))

def getAQI_Days (loc, ndays):
	return getAQI (loc, datetime.now(), datetime.today() - timedelta(days = ndays))



