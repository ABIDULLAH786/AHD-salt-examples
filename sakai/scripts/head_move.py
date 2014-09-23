import time
import random
import sys

from naoqi import ALProxy

REPEAT = 50

argvs = sys.argv 
ip = argvs[1]
port = 9559

speed = float(argvs[2])

try:
	motion_proxy = ALProxy('ALMotion',ip,port)
except:
	quit()

part = 'Body'
body_names = ['HeadPitch']
body_limits = [motion_proxy.getLimits(l)[0] for l in body_names]
body_limits_angles = [ [l[0],l[1]] for l in body_limits]

#stiffen to move
motion_proxy.setStiffnesses(part,1.0)

for i in range(REPEAT):

	if i%2 == 0: 
		target_angles = [angles[0]+(angles[1]-angles[0])*0.1 for angles in body_limits_angles]
	else :
		target_angles = [angles[0]+(angles[1]-angles[0])*0.9 for angles in body_limits_angles]

	fractionMaxSpeed = speed
	motion_proxy.setAngles(body_names,target_angles,fractionMaxSpeed)

	time.sleep(0.10)