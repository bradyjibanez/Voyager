from pynetgear import Netgear
from lockControl import LockControl
#from smartSwitchControl import SmartSwitchControl
from astral import Astral
from subprocess import Popen, PIPE, call
import os, time, datetime, threading, json, simplejson, pytz

netgear = Netgear(password = "3035highway7")
#switches = SmartSwitchControl()
lock = LockControl()
knownHosts = []
seenHosts = []

class OccDetectionControl():

	#Seems unnecessary but leaving for call if needed, has no change verification pause
	def createLog(self, entry):
		log = open("./results/houseLogConfirmed.txt", "a+")
		time = datetime.datetime.now()
		log.write(entry + "- " + time.strftime("%A, %b %d, %Y") + " @ " + time.strftime("%I:%M:%S %p") + "\n")

	#Better representation to check if skipped out host really changed
	def createConfirmedLog(self, confirmedHosts):
		log = open("./results/houseLogConfirmed.txt", "a+")
		time = datetime.datetime.now()
		log.write(confirmedHosts + "- " + time.strftime("%A, %b %d, %Y") + " @ " + time.strftime("%I:%M:%S %p") + "\n")

	def findPresentHosts(self):
		while True:
			try:
				global knownHosts
				global seenHosts
				hostCheck = []
				entry = []

				#Old version that was router dependent
				for host in netgear.get_attached_devices():
					foundHost = [host[0], host[1], host[2]]
					if host[2] == "A0:CC:2B:C8:BE:21":
						entry.append("Brady.")
						hostCheck.append(foundHost)
						#print(foundHost)
					if host[2] == "10:98:C3:00:C6:86":
						entry.append("Amanda.")
						hostCheck.append(foundHost)
						#print(foundHost)
					if host[2] == "64:A2:F9:ED:4D:79":
						entry.append("Dan.")
						hostCheck.append(foundHost)
						#print(foundHost)

				#Works as a more efficient reference without dependency of router specific library
				'''arpList = Popen("sudo arp-scan --interface=wlx9c5c8eb53b9a --localnet", shell=True, stdout=PIPE).stdout
				arpList = str(arpList.read()) 
				entry, hostCheck = self.findOccupants(arpList, entry, hostCheck)'''

				if entry != []:
					entry = ''.join(entry)
					#Call to faster occ with no changes if needed
					#createLog(entry)
					#print(entry)
					seenHosts = entry
				else:
					entry = "No one."
					#print(entry)
					seenHosts = entry
					#createLog(entry)	
				if knownHosts != hostCheck:
					knownHosts = hostCheck
			except Exception as e:
				print("Exception in thread 1:", e)
				time.sleep(5)

	def confirmPresentHosts(self):
		count = 0
		global knownHosts
		global seenHosts
		#initializes reference to previous confirmed hosts (knownHosts)
		oldKnownHosts = knownHosts
		while True:
			try:
				if oldKnownHosts != knownHosts:
					same = False
					while same != True:
						if oldKnownHosts != knownHosts:
								count += 1
								#print("Waiting to see if changes back. ", count, "\n")
								time.sleep(1)
								if count > 9:
									#print("Too long, host list updating to confirmed log. \n", knownHosts, "should have matched", oldKnownHosts, "\n")
									with open('./results/homeResults.json', 'r') as itemsFile:
										data = json.load(itemsFile)
									lock.autoLock(seenHosts, data)
									self.createConfirmedLog(seenHosts)
									time.sleep(1)
									oldKnownHosts = knownHosts
									same = True
						if oldKnownHosts == knownHosts:
							count = 0
							#print("Changed back. Starting fresh loop. \n")
							time.sleep(1)
							same = True
				else:
					#print("All good in the hood. ", count, "\n")	
					time.sleep(1)
			except Exception as e:
				print("Exception in thread 2:", e)
				time.sleep(5)	

	#Reads most recently created houseLogConirmed to create JSON of occupants
	def getRecentConfirmedOccupants(self):
		with open('./results/houseLogConfirmed.txt', 'r') as log:
			lines = log.read().splitlines()
			lastEntry = lines[-1]
			hostCount = log.read().count('.')
			hosts = []
			while hostCount < lastEntry.count('.'):
				try:
					host = lastEntry.split('.')[hostCount]
					host = host.replace(' ', '')
					entry = {"id": str(hostCount), "name": host}
					hosts.append(entry)
					hostCount+=1
				except Exception as e:
					print("Exception in thread 3:", e)
					time.sleep(5)
		return hosts

	def findOccupants(self, arp, entry, hostCheck):
		item = [str(item) for item in arp]
		joined = "".join(item)
		if "a0:cc:2b:c8:be:21" in joined:
			entry.append("Brady.")
			hostCheck.append("A0:CC:2B:C8:BE:21")
		if "10:98:c3:00:c6:86" in joined:
			entry.append("Amanda.")
			hostCheck.append("10:98:C3:00:C6:86")
		if "64:a2:f9:ed:4d:79" in joined:
			entry.append("Dan.")
			hostCheck.append("64:A2:F9:ED:4D:79")
		return entry, hostCheck