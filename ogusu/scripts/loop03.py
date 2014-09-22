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

names.append("HeadPitch")
times.append([1])
keys.append([[0.637045, [3, -0.333333, 0], [3, 0, 0]]])

names.append("HeadYaw")
times.append([1])
keys.append([[0.00153399, [3, -0.333333, 0], [3, 0, 0]]])

names.append("HipPitch")
times.append([1])
keys.append([[-0.656544, [3, -0.333333, 0], [3, 0, 0]]])

names.append("HipRoll")
times.append([1])
keys.append([[-0.00766992, [3, -0.333333, 0], [3, 0, 0]]])

names.append("KneePitch")
times.append([1])
keys.append([[0.185612, [3, -0.333333, 0], [3, 0, 0]]])

names.append("LElbowRoll")
times.append([1])
keys.append([[-0.00872665, [3, -0.333333, 0], [3, 0, 0]]])

names.append("LElbowYaw")
times.append([1])
keys.append([[-1.23179, [3, -0.333333, 0], [3, 0, 0]]])

names.append("LHand")
times.append([1])
keys.append([[0.593146, [3, -0.333333, 0], [3, 0, 0]]])

names.append("LShoulderPitch")
times.append([1])
keys.append([[0.905826, [3, -0.333333, 0], [3, 0, 0]]])

names.append("LShoulderRoll")
times.append([1])
keys.append([[0.363028, [3, -0.333333, 0], [3, 0, 0]]])

names.append("LWristYaw")
times.append([1])
keys.append([[-0.0123138, [3, -0.333333, 0], [3, 0, 0]]])

names.append("RElbowRoll")
times.append([1])
keys.append([[0.00872665, [3, -0.333333, 0], [3, 0, 0]]])

names.append("RElbowYaw")
times.append([1])
keys.append([[1.23639, [3, -0.333333, 0], [3, 0, 0]]])

names.append("RHand")
times.append([1])
keys.append([[0.594025, [3, -0.333333, 0], [3, 0, 0]]])

names.append("RShoulderPitch")
times.append([1])
keys.append([[0.905826, [3, -0.333333, 0], [3, 0, 0]]])

names.append("RShoulderRoll")
times.append([1])
keys.append([[-0.363028, [3, -0.333333, 0], [3, 0, 0]]])

names.append("RWristYaw")
times.append([1])
keys.append([[0.0152981, [3, -0.333333, 0], [3, 0, 0]]])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  motion = ALProxy("ALMotion", IP, 9559)
  # motion = ALProxy("ALMotion")
  motion.angleInterpolationBezier(names, times, keys)
except BaseException, err:
  print err
