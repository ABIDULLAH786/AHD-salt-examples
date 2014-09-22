import time
import math
import random
from naoqi import ALProxy
import sys

argvs = sys.argv 
ip = argvs[1]
port = 9559

#proxy first!
# motion_proxies = [ALProxy('ALMotion',ip,port)  for ip in IP]

motion_proxy = ALProxy('ALMotion',ip,port)
motion_proxy.killAll()