from naoqi import ALProxy
import sys


argvs = sys.argv 
ip = argvs[1]
port = 9559


# try:
# 	leds = ALProxy("ALLeds", IP, PORT)
# except Exception as e:
# 	print "ng"


# def onLed(group, r, g, b, duration):
# 	# file:///Applications/Choregraphe.app/Contents/Resources/share/doc/naoqi/sensors/alleds.html
# 	leds.fadeRGB(group, r, g, b, duration)
# 	pass


# onLed('RightFaceLeds', 0, 0, 0, 0.0)
# onLed('LeftFaceLeds', 0, 0, 0, 0.0)
# onLed('ChestLeds', 0, 0, 0, 0.0)
# onLed('RightEarLeds', 0, 0, 0, 0.0)
# onLed('LeftEarLeds', 0, 0, 0, 0.0)

#put off LED

try:
	motion_proxy = ALProxy('ALMotion',ip,port)
except Exception as e:
	print "ng"

motion_proxy.setExternalCollisionProtectionEnabled('All', True)
motion_proxy.rest()


