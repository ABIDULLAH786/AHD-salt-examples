import time
import math
import random
from naoqi import ALProxy

IP = '127.0.0.1'
port = 49249

motion_proxy = ALProxy('ALMotion',IP,port)

part = 'Body'

time.sleep(3.0)

body_names = motion_proxy.getBodyNames(part)
body_limits = [motion_proxy.getLimits(l)[0] for l in body_names]
body_limits_angles = [ [l[0],l[1]] for l in body_limits]


motion_proxy.setStiffnesses(part,1.0)

for i in range(200):

	target_angles = [ (angles[1]-angles[0])*random.choice([0,1])+angles[0] for angles in body_limits_angles]

	fractionMaxSpeed = 0.99

	motion_proxy.setAngles(body_names,target_angles,fractionMaxSpeed)

	#motion_proxy.changeAngles(names, changes, fractionMaxSpeed) #adds the angle to 
	time.sleep(0.15)


motion_proxy.setStiffnesses(part, 0.0)