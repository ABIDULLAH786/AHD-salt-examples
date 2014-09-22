# Choregraphe bezier export in Python.
from naoqi import ALProxy
import time
import sys
from naoqi import ALProxy

args = sys.argv
IP = args[1]
PORT = 9559

names = list()
times = list()
keys = list()

names.append("RElbowRoll")
times.append([1])
keys.append([[1.24105, [3, -0.333333, 0], [3, 0, 0]]])

names.append("RElbowYaw")
times.append([1])
keys.append([[0.754686, [3, -0.333333, 0], [3, 0, 0]]])

names.append("RHand")
times.append([1])
keys.append([[0.166571, [3, -0.333333, 0], [3, 0, 0]]])

names.append("RShoulderPitch")
times.append([1])
keys.append([[-0.613558, [3, -0.333333, 0], [3, 0, 0]]])

names.append("RShoulderRoll")
times.append([1])
keys.append([[-0.833004, [3, -0.333333, 0], [3, 0, 0]]])

names.append("RWristYaw")
times.append([1])
keys.append([[-0.067538, [3, -0.333333, 0], [3, 0, 0]]])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  motion = ALProxy("ALMotion", IP, 9559)
  # motion = ALProxy("ALMotion")
  motion.angleInterpolationBezier(names, times, keys)
except BaseException, err:
  print err
