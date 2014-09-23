from naoqi import ALProxy
import sys
import math
import random
import time

args = sys.argv
IP = args[1]

COLOR = args[2]

PORT = 9559

try:
	leds = ALProxy("ALLeds", IP, PORT)
except Exception as e:
	quit()



def onLed(group, r, g, b, duration):
	# file:///Applications/Choregraphe.app/Contents/Resources/share/doc/naoqi/sensors/alleds.html
	leds.fadeRGB(group, r, g, b, duration)

col = [float(c) for c in COLOR.split(',')]

onLed('RightFaceLeds', col[0], col[1], col[2], 0.0)
onLed('LeftFaceLeds', col[0], col[1], col[2], 0.0)
onLed('ChestLeds', col[0], col[1], col[2], 0.0)
onLed('RightEarLeds', 0, 0, 0, 0.0)
onLed('LeftEarLeds', 0, 0, 0, 0.0)

# time.sleep(0.5)


