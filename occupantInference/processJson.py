from lockControl import LockControl
from smartSwitchControl import SmartSwitchControl
from occDetectionControl import OccDetectionControl
import simplejson, datetime, time

smartSwitches = SmartSwitchControl()
lock = LockControl()
occDetectionControl = OccDetectionControl()

#Creates JSON file for current house state
class ProcessJson():

	def processJson(self, devices, lockStatus, occupants):
		currentTime = datetime.datetime.now()
		now = (currentTime.strftime("%A, %b %d, %Y") + " @ " + currentTime.strftime("%I:%M:%S %p"))
		jsonResult = {"Time_Updated": now, "Lock_Status": lockStatus, 
					"Smart_Switches": devices, 
					"Occupants": occupants} 
		with open('./results/homeResults.json', 'w+') as itemsFile:
			itemsFile.write(simplejson.dumps(jsonResult, indent=4, sort_keys=True))
		with open('/home/brady/Code/Angular/homeApp/src/assets/homeResults.json', 'w+') as itemsFile:
			itemsFile.write(simplejson.dumps(jsonResult, indent=4, sort_keys=True))
		#print(simplejson.dumps(jsonResult, indent=4, sort_keys=True))
		print("json updated on " + str(now))

	def updateJson(self):
		while True:
			try:
				print("CHECKING")
				switches = smartSwitches.updateStatus()
				lockStatus = lock.getLockStatus()
				occupants = occDetectionControl.getRecentConfirmedOccupants()
				self.processJson(switches, lockStatus, occupants)
			except Exception as e:
				print("Exception in thread 3:", e)
				time.sleep(5)

