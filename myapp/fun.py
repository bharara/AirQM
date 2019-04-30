import aqi
from datetime import datetime, date

## Marker Functions


def dToInt (t):
	if isinstance(t, date):
		return (datetime.combine(t, datetime.min.time())- datetime(2019,1,1)).total_seconds()
	else:
		return (datetime.strptime(t, ('%Y-%m-%d')) - datetime(2019,1,1)).total_seconds()		

## AQI Calulator
def calculateAQI (lst):
	myaqi = aqi.to_aqi([
		(aqi.POLLUTANT_CO_8H, str(lst[0])),
		(aqi.POLLUTANT_PM25, str(lst[1])),
		(aqi.POLLUTANT_O3_8H, str(lst[2])),
		(aqi.POLLUTANT_SO2_1H, str(lst[3])),
		(aqi.POLLUTANT_NO2_1H, str(lst[4]))
		])

	return myaqi