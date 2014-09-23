from naoqi import ALProxy
import sys
import math
import random
import time

args = sys.argv
IP = args[1]
PORT = 9559

try:
	leds = ALProxy("ALLeds", IP, PORT)
except Exception as e:
	print "ng"



def onLed(group, r, g, b, duration):
	# file:///Applications/Choregraphe.app/Contents/Resources/share/doc/naoqi/sensors/alleds.html
	leds.fadeRGB(group, r, g, b, duration)
	pass


onLed('RightFaceLeds', 0, 0, 0, 0.0)
onLed('LeftFaceLeds', 0, 0, 0, 0.0)
onLed('ChestLeds', 0, 0, 0, 0.0)
onLed('RightEarLeds', 0, 0, 0, 0.0)
onLed('LeftEarLeds', 0, 0, 0, 0.0)

# time.sleep(0.5)


