from myapp.fun import calculateAQI, dToInt
from datetime import datetime, timedelta
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class Location:

	def __init__(self, name, st = datetime.today() - timedelta(days = 7), end = datetime.today()):
		self.name = name
		self.dbase = DataBase ()
		self.cord = self.dbase.getCordFromDB (name)
		self.color = self.markerColor (self.getAQI(st, end))
		self.link =  "https://aqm-project-c5355.firebaseio.com/" + self.name + ".json"
		

	def getAQI_Days (self, ndays):
		return self.getAQI (datetime.now(), datetime.today() - timedelta(days = ndays))

	def getAQI (self, startDT, endDT = datetime.now()):
		lst = self.dbase.getGasesAVG (self.name, endDT, startDT)
		return calculateAQI (lst)


	def getAQIData (self):
		l = []
		for s, i in [("Day",1), ("Week",7), ("Month",30)]:
			a = self.getAQI_Days (i)
			b = self.getAQI(datetime.today() - timedelta(days = i), datetime.today() - timedelta(days = 2*i))
			if a == 0 or b == 0 or a==b:
				c = "-"
			elif a > b:
				c = "Down"
			else:
				c = "UP"
			l.append((s,a,b,c))

		return l

	def setColor (self, startDT, endDT = datetime.now()):
		if startDT == (datetime.today() - timedelta(days = 7)):
			pass
		else:
			aqi = getAQI (startDT, endDT)
			self.color = self.markerColor(aqi)


	def markerColor (self, aqi):
		if aqi < 51:
			return "green"
		elif aqi < 101:
			return "yellow"
		elif aqi < 151:
			return "orange"
		elif aqi < 200:
			return "red"
		elif aqi < 301:
			return "purple"
		else:
			return "brown"

	def getDataPoints (self, n):
		result = db.reference(self.name).order_by_child('time').limit_to_last(n).get()

		lst = []
		for x in result:
			l = []
			for y in result[x]:
				l.append (result[x][y])
			lst.append(l)
		return lst




class DataBase :
	def __init__ (self):
		self.cred = credentials.Certificate("D:\\AirQM\\myapp\\static\\aqm-project-c5355-firebase-adminsdk-d3zf8-84517bf4bc.json")
		self.url = 'https://aqm-project-c5355.firebaseio.com/aqm-project-c5355'

		#Intiliaze database
		try:
			firebase_admin.initialize_app(self.cred,{
			'databaseURL' : self.url
			})
		except:
			pass


	def getMarkerNames (self):
		root = db.reference("locations")
		
		lst = []
		for x in root.get():
			root = db.reference("locations/" + x + "/name")
			lst.append(root.get())
		return lst


	def getMarkerList (self, st = datetime.today() - timedelta(days = 7), end = datetime.today()):
		lst = []
		for name in self.getMarkerNames ():
			lst.append(Location (name, st, end))

		return lst

	def getGasesAVG (self, name, stDT, endDT):

	    result = db.reference(name).order_by_child('time').start_at(dToInt(stDT)).end_at(dToInt(endDT)).get()

		#Data recieved as dictionary can modify as wish
	    lst = [0,0,0,0,0]
	    for x in result:
	        z=0
	        for y in (result[x]):
	            if y!="time":
	                lst[z] += (result[x][y])
	                z += 1
	            else:
	                continue

	        lst = [x/len(result) for x in lst]

	    return lst

	def getCordFromDB (self, name):
		for x in db.reference("locations").get():
			if db.reference("locations/" + x + "/name").get() == name:
				return db.reference("locations/" + x + "/coord").get()


