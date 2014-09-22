from naoqi import ALProxy

IP = '127.0.0.1'
port = 49249

joints = ['Body','Head','RArm','LArm','Leg']

for j in joints:
	motion_proxy = ALProxy('ALMotion',IP,port)
	body_names = motion_proxy.getBodyNames(j)
	print j
	print str(body_names)
	print ''

#body_names = ['HeadYaw', 'HeadPitch', 'LShoulderPitch', 'LShoulderRoll', 'LElbowYaw', 'LElbowRoll', 'LWristYaw', 'LHand', 'HipRoll', 'HipPitch', 'KneePitch', 'RShoulderPitch', 'RShoulderRoll', 'RElbowYaw', 'RElbowRoll', 'RWristYaw', 'RHand', 'WheelFL', 'WheelFR', 'WheelB']