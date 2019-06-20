from datetime import datetime
from astral import Astral
from pyHS100 import Discover, SmartPlug, SmartBulb
import time, socket, requests, pytz, simplejson

#Used to determine daylight status, occupancy status, and does the things
#if the things are needed based on prior info
class SmartSwitchControl():
        a = Astral()
        city = a['Toronto']
        count = 0

        def run(self):
                global count
                global lightson
                now = datetime.now(pytz.utc)
                sun = city.sun(date = now, local = True)
                time.sleep(0.5)
                if now >= sun['dusk'] or now <= sun['dawn']:
                        requests.post("https://maker.ifttt.com/trigger/motion/with/key/ctOeqYQKH00WbPhjj-fCRyio_MW6GdmEQ2as2h5bQvI")
                        Lightson = True
                        #print("Lights on")
                elif now >= sun['dawn']:
                        #print("It's not dark yet")
                        pass

        #Creates JSON syntaxed representation of current smart device info and status
        def updateStatus(self):
                devices = []
                deviceCount = 0
                try:
                        for dev in Discover.discover().values():
                                ipBreak = str(dev).split(' (')[0]
                                ip = ipBreak.split('at ')[1]
                                idBreak = str(dev).split('(')[1]
                                ID = idBreak.split(')')[0]
                                statusBreak = str(dev).split('is_on: ')[1]
                                status = statusBreak.split(' - ')[0]
                                if status == "True":
                                        status = "on"
                                if status == "False":
                                        status = "off"
                                entry = {'id': "switch"+str(deviceCount), 
                                        'name': ID,
                                        'is_on': status,
                                        'ip': ip
                                }
                                devices.append(entry)
                                deviceCount += 1
                        return devices
                except Exception as e:
                        print("Error in device detection...resetting", e)
                        pass