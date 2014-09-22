import time
import math
import random
from naoqi import ALProxy
import sys



#will be address via shell file 


#IP = ['192.168.3.6','192.168.3.9','192.168.3.8']
#IP = ['192.168.3.6']

argvs = sys.argv 
ip = argvs[1]
port = 9559

#proxy first!
# motion_proxies = [ALProxy('ALMotion',ip,port)  for ip in IP]
try:
	motion_proxy = ALProxy('ALMotion',ip,port)
except:
	quit()
motion_proxy.wakeUp()

#deactivate collision detection
#motion_proxy.setExternalCollisionProtectionEnabled('All', False)
#motion_proxy.setCollisionProtectionEnabled('Arms', False)



# cnt = 0
# for i in range(len(IP)):
# 	#motion_proxy = ALProxy('ALMotion',ip,port)
# 	motion_proxies[i].wakeUp()



