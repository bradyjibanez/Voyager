from pynetgear import Netgear
from lockControl import LockControl
from smartSwitchControl import SmartSwitchControl
from occDetectionControl import OccDetectionControl
from processJson import ProcessJson
import os, time, datetime, threading

#Objects for all the interweiving to be done
switches = SmartSwitchControl()
lock = LockControl()
occDetectionControl = OccDetectionControl()
jsonProcessor = ProcessJson()

#Stuff to be referenced in OccDetect threads
netgear = Netgear(password = "3035highway7")
knownHosts = []
confirmedHosts = []

#Threaded to constantly update presentHosts for next method to verify async
checkRouter = threading.Thread(target=occDetectionControl.findPresentHosts, args=())
checkRouter.start()
#Called to do what said above with updated presentHosts
verifyRouter = threading.Thread(target=occDetectionControl.confirmPresentHosts, args=())
verifyRouter.start()
#Called to do what said above with updated presentHosts
updateJSON = threading.Thread(target=jsonProcessor.updateJson, args=())
updateJSON.start()

