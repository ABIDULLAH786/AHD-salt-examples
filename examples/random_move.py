import time
import math
import random
from naoqi import ALProxy

IP = '127.0.0.1'
port = 49249

motion_proxy = ALProxy('ALMotion',IP,port)

part = 'Body'

time.sleep(3.0)

for i in range(200):

	motion_proxy.setStiffnesses(part, 1.0)

	body_names = motion_proxy.getBodyNames(part)

	if i !=0:
		third_name = first_name
	else :
		third_name = random.choice(body_names)

	first_name  = random.choice(body_names)

	while True:
		if first_name != third_name:
			break
		else:
			first_name = random.choice(body_names)

	second_name = random.choice(body_names)


	while True:
		if (second_name != first_name) and (second_name != third_name):
			break
		else:
			second_name = random.choice(body_names)


	limits = motion_proxy.getLimits(first_name)[0]

	#limits of the specific joint
	first_target_angle = (limits[1]-limits[0]) * random.random() + limits[0]

	limits = motion_proxy.getLimits(second_name)[0]

	second_target_angle = (limits[1]-limits[0]) * random.random() + limits[0]

	limits = motion_proxy.getLimits(third_name)[0]

	third_target_angle = (limits[1]-limits[0]) * random.random() + limits[0]

	fractionMaxSpeed = 0.99

	names = [first_name,second_name,third_name]
	target_angles = [first_target_angle,second_target_angle,third_target_angle]

	#motion_proxy.changeAngles(names, changes, fractionMaxSpeed) #adds the angle to 
	motion_proxy.setAngles(names, target_angles, fractionMaxSpeed)

	time.sleep(0.05)
	# print 'joint name: '+ names
	# print math.degrees(motion_proxy.getAngles(names,True)[0])
	# print ''


motion_proxy.setStiffnesses(part, 0.0)