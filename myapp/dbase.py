
#from firebase import firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


class DataBase :
	def __init__ (self):
		self.cred = credentials.Certificate("D:\\AirQM\\aqm-project-c5355-firebase-adminsdk-d3zf8-84517bf4bc.json")
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
			lst.append(root.get ())
		return lst




	def getMarkerList (self):
		lst = []
		for name in self.getMarkerNames ():
			lst.append(Location (name))

		return lst

	def getGAV (self, name, stDT, endDT):
		nameCh = db.reference(name)
		return nameCh.order_by_child('time').start_at(stDT).end_at(endDT).get()


#root = db.reference('locations//name')
#root = db.Query.limit_to_last(2)
#root = db.reference.__getattribute__()
#root = db.chlid('locations/name')


#Function for location names to be printed

    

#d = DataBase ()
#print(d.getGAV("BlueArea", 166, 200))

import datetime

print (str(datetime.datetime.today().date()))