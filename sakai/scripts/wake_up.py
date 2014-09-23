from naoqi import ALProxy
import sys



#will be addressed via shell file 

argvs = sys.argv 
ip = argvs[1]
port = 9559

try:
	motion_proxy = ALProxy('ALMotion',ip,port)
except:
	quit()

motion_proxy.wakeUp()
motion_proxy.setExternalCollisionProtectionEnabled('All', False)

try:
	leds = ALProxy("ALLeds", ip, port)
except Exception as e:
	quit()

#led controller
def onLed(group, r, g, b, duration):
	# file:///Applications/Choregraphe.app/Contents/Resources/share/doc/naoqi/sensors/alleds.html
	leds.fadeRGB(group, r, g, b, duration)

# change LED to color to white
onLed('RightFaceLeds', 1.0, 1.0, 1.0, 0.0)
onLed('LeftFaceLeds', 1.0, 1.0, 1.0, 0.0)
onLed('ChestLeds', 1.0, 1.0, 1.0, 0.0)
onLed('RightEarLeds', 0, 0, 0, 0.0)
onLed('LeftEarLeds', 0, 0, 0, 0.0)





