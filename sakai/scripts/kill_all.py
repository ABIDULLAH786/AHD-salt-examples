from naoqi import ALProxy
import sys

argvs = sys.argv 
ip = argvs[1]
port = 9559

motion_proxy = ALProxy('ALMotion',ip,port)
motion_proxy.killAll()