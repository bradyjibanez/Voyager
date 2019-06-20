from astral import Astral
import requests, sys, json, datetime, pytz

#Everything in this class does what you think it does
class LockControl():

	def lockFrontDoor(self):
		lock = "https://api-production.august.com/remoteoperate/0D08460407664ACB8AC986848C218F11/lock"
		headers = {"x-august-api-key" : "79fd0eb6-381d-4adf-95a0-47721289d1d9",
	           "x-august-access-token" : "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpbnN0YWxsSWQiOiI3NmY2NWExYy03Nzc4LTExZTktOGY5ZS0yYTg2ZTQwODVhNTkiLCJhcHBsaWNhdGlvbklkIjoiIiwidXNlcklkIjoiZWIzYTMzNGMtZGVkMS00MDBlLTgwY2EtOTE0MjNmZjJhYjE2Iiwidkluc3RhbGxJZCI6dHJ1ZSwidlBhc3N3b3JkIjp0cnVlLCJ2RW1haWwiOmZhbHNlLCJ2UGhvbmUiOnRydWUsImhhc0luc3RhbGxJZCI6dHJ1ZSwiaGFzUGFzc3dvcmQiOnRydWUsImhhc0VtYWlsIjp0cnVlLCJoYXNQaG9uZSI6dHJ1ZSwiaXNMb2NrZWRPdXQiOmZhbHNlLCJjYXB0Y2hhIjoiIiwiZW1haWwiOltdLCJwaG9uZSI6WyJwaG9uZTorMTkwNTQ0NzY1OTUiXSwiZXhwaXJlc0F0IjoiMjAxOS0wOS0xM1QyMjo1NjowNy43NTJaIiwidGVtcG9yYXJ5QWNjb3VudENyZWF0aW9uUGFzc3dvcmRMaW5rIjoiIiwiaWF0IjoxNTU4MDQ0NDM5LCJleHAiOjE1Njg0MTUzNjcsIkxhc3ROYW1lIjoiSWJhbmV6IiwiRmlyc3ROYW1lIjoiQnJhZHkifQ.DGmKUUcAOzxEIxM5qV_owZEXwdI8YJgstag-cQCiDBg",
	           "Content-Type" : "application/json"}
		requests.put(lock, data=None, headers=headers)

	def unlockFrontDoor(self):
		unlock = "https://api-production.august.com/remoteoperate/0D08460407664ACB8AC986848C218F11/unlock"
		headers = {"x-august-api-key" : "79fd0eb6-381d-4adf-95a0-47721289d1d9",
	           "x-august-access-token" : "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpbnN0YWxsSWQiOiI3NmY2NWExYy03Nzc4LTExZTktOGY5ZS0yYTg2ZTQwODVhNTkiLCJhcHBsaWNhdGlvbklkIjoiIiwidXNlcklkIjoiZWIzYTMzNGMtZGVkMS00MDBlLTgwY2EtOTE0MjNmZjJhYjE2Iiwidkluc3RhbGxJZCI6dHJ1ZSwidlBhc3N3b3JkIjp0cnVlLCJ2RW1haWwiOmZhbHNlLCJ2UGhvbmUiOnRydWUsImhhc0luc3RhbGxJZCI6dHJ1ZSwiaGFzUGFzc3dvcmQiOnRydWUsImhhc0VtYWlsIjp0cnVlLCJoYXNQaG9uZSI6dHJ1ZSwiaXNMb2NrZWRPdXQiOmZhbHNlLCJjYXB0Y2hhIjoiIiwiZW1haWwiOltdLCJwaG9uZSI6WyJwaG9uZTorMTkwNTQ0NzY1OTUiXSwiZXhwaXJlc0F0IjoiMjAxOS0wOS0xM1QyMjo1NjowNy43NTJaIiwidGVtcG9yYXJ5QWNjb3VudENyZWF0aW9uUGFzc3dvcmRMaW5rIjoiIiwiaWF0IjoxNTU4MDQ0NDM5LCJleHAiOjE1Njg0MTUzNjcsIkxhc3ROYW1lIjoiSWJhbmV6IiwiRmlyc3ROYW1lIjoiQnJhZHkifQ.DGmKUUcAOzxEIxM5qV_owZEXwdI8YJgstag-cQCiDBg",
	           "Content-Type" : "application/json"}
		requests.put(unlock, data=None, headers=headers)

	def getLockStatus(self):
		#responseBody = {'status': lockStatus}
		status = "https://api-production.august.com/remoteoperate/0D08460407664ACB8AC986848C218F11/status"
		headers = {"x-august-api-key" : "79fd0eb6-381d-4adf-95a0-47721289d1d9",
				"x-august-access-token" : "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpbnN0YWxsSWQiOiI3NmY2NWExYy03Nzc4LTExZTktOGY5ZS0yYTg2ZTQwODVhNTkiLCJhcHBsaWNhdGlvbklkIjoiIiwidXNlcklkIjoiZWIzYTMzNGMtZGVkMS00MDBlLTgwY2EtOTE0MjNmZjJhYjE2Iiwidkluc3RhbGxJZCI6dHJ1ZSwidlBhc3N3b3JkIjp0cnVlLCJ2RW1haWwiOmZhbHNlLCJ2UGhvbmUiOnRydWUsImhhc0luc3RhbGxJZCI6dHJ1ZSwiaGFzUGFzc3dvcmQiOnRydWUsImhhc0VtYWlsIjp0cnVlLCJoYXNQaG9uZSI6dHJ1ZSwiaXNMb2NrZWRPdXQiOmZhbHNlLCJjYXB0Y2hhIjoiIiwiZW1haWwiOltdLCJwaG9uZSI6WyJwaG9uZTorMTkwNTQ0NzY1OTUiXSwiZXhwaXJlc0F0IjoiMjAxOS0wOS0xM1QyMjo1NjowNy43NTJaIiwidGVtcG9yYXJ5QWNjb3VudENyZWF0aW9uUGFzc3dvcmRMaW5rIjoiIiwiaWF0IjoxNTU4MDQ0NDM5LCJleHAiOjE1Njg0MTUzNjcsIkxhc3ROYW1lIjoiSWJhbmV6IiwiRmlyc3ROYW1lIjoiQnJhZHkifQ.DGmKUUcAOzxEIxM5qV_owZEXwdI8YJgstag-cQCiDBg", 
				"Content-Type" : "application/json"}
		theStatus = requests.put(status, data=None, headers=headers)
		text = theStatus.json()
		status = text['status']
		status = status.split('_')[1]
		return status

	def autoLock(self, seenHosts, data):
		a = Astral()
		city = a['Toronto']
		now = datetime.datetime.now(pytz.timezone('America/Toronto'))
		sun = city.sun(date = now, local = True)
		#works with confirmed (confirmed in lines 71-74 of occDetectionControl) seenHosts before updating knownHosts
		if seenHosts != "No one. " and data['Lock_Status'] == "Unlocked" and now >= sun['dusk']:
			#self.lockFrontDoor()
			#print("door stays locked at night")
			pass
		elif seenHosts != "No one. " and data['Lock_Status'] == "Locked" and now < sun['dusk']:
			#self.unlockFrontDoor()
			#print("door unlocked")
			pass
		elif seenHosts == "No one. ":
			#self.lockFrontDoor()	
			#print("door stays locked while no one's home")
			pass
		else:
			#print("Lock status stays the same")
			pass