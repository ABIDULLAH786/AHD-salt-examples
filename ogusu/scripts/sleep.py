import time
import math
import random
from naoqi import ALProxy
import sys



#IP = ['192.168.3.6','192.168.3.9','192.168.3.8']
#IP = ['192.168.3.6']

argvs = sys.argv 
ip = argvs[1]
port = 9559


motion_proxy = ALProxy('ALMotion',ip,port)


motion_proxy.setExternalCollisionProtectionEnabled('All', True)
motion_proxy.setCollisionProtectionEnabled('Arms', True)
motion_proxy.rest()
