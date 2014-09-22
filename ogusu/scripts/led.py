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
	exit()



def onLed(group, r, g, b, duration):
	# file:///Applications/Choregraphe.app/Contents/Resources/share/doc/naoqi/sensors/alleds.html
	leds.fadeRGB(group, r, g, b, duration)
	pass

for i in range(20):
	r = random.uniform(0, 1)
	g = random.uniform(0, 1)
	b = random.uniform(0, 1)
	onLed('RightFaceLeds', r, g, b, 0.0)

	r = random.uniform(0, 1)
	g = random.uniform(0, 1)
	b = random.uniform(0, 1)
	onLed('LeftFaceLeds', r, g, b, 0.0)

	r = random.uniform(0, 1)
	g = random.uniform(0, 1)
	b = random.uniform(0, 1)
	onLed('ChestLeds', r, g, b, 0.0)

	onLed('RightEarLeds', 0, 0, 1, 0.0)
	onLed('LeftEarLeds', 0, 0, 1, 0.0)

	time.sleep(0.1)

	onLed('RightFaceLeds', 0, 0, 0, 0.0)
	onLed('LeftFaceLeds', 0, 0, 0, 0.0)
	onLed('ChestLeds', 0, 0, 0, 0.0)
	onLed('RightEarLeds', 0, 0, 0, 0.0)
	onLed('LeftEarLeds', 0, 0, 0, 0.0)
	time.sleep(0.05)
	


