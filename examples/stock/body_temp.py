import time
import math
import random
import sys

from naoqi import ALProxy

REPEAT = 1

argvs = sys.argv 
ip = argvs[1]
port = 9559

#speed = float(argvs[2])

body_temp_proxy = ALProxy('ALBodyTemperatureProxy',ip,port)

temp_diagnosis = body_temp_proxy.getTemperatureDiagnosis()

print temp_diagnosis
