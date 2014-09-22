import time
import math
import random
from naoqi import ALProxy

IP = ['192.168.3.6','192.168.3.9','192.168.3.8']

IP = ['192.168.3.6']

port = 9559

count = 0

for ip in IP:
	motion_proxy = ALProxy('ALMotion',ip,port)

	motion_proxy.setCollisionProtectionEnabled('Arms', True)

	part = 'Body'

	crop = ['HipPitch','HipRoll','KneePitch']

	time.sleep(1.0)

	body_names = [p for p in motion_proxy.getBodyNames(part) if p not in crop]
	body_limits = [motion_proxy.getLimits(l)[0] for l in body_names]
	body_limits_angles = [ [l[0],l[1]] for l in body_limits]


	motion_proxy.setStiffnesses(part,1.0)

	for i in range(1):

		#if count == 0:
		target_angles = [ (angles[1]-angles[0])*random.choice([0,1])+angles[0] for angles in body_limits_angles]

		#target_angles = [ (angles[1]-angles[0])*random.choice([0,1])+angles[0] for angles in body_limits_angles]


		fractionMaxSpeed = 0.0033

		motion_proxy.setAngles(body_names,target_angles,fractionMaxSpeed)

		#motion_proxy.changeAngles(names, changes, fractionMaxSpeed) #adds the angle to 
		time.sleep(0.15)

	count += 1


	motion_proxy.setStiffnesses(part, 0.0)