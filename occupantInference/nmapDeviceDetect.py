##THIS INEFFICIENT AF
##try to imrove after netgear package version is working

from subprocess import Popen, PIPE, call
import time, difflib, os

#FNULL = open(os.devnull, 'w')
#call('sudo nmap -sn 192.168.1.1/24', shell=True)
arpList = Popen("sudo arp-scan --interface=wlx9c5c8eb53b9a --localnet", shell=True, stdout=PIPE).stdout
list = str(arpList.read())

def findMACs(string):
	found = False
	#for char in list:
	#	if char == "n":
	item = [str(item) for item in string]
	joined = "".join(item)
	if "a0:cc:2b:c8:be:21" in joined:
		print("Brady's online")
		found = True
	if "10:98:c3:00:c6:86" in joined:
		print("Amanda's online")
		found = True
	if "64:a2:f9:ed:4d:79" in joined:
		print("Dan's online")
		found = True

	if found != True:
		print("No match")

findMACs(list)
