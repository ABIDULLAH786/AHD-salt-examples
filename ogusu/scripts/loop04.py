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
times.append([0.52, 0.8, 1.04])
keys.append([[-0.394233, [3, -0.173333, 0], [3, 0.0933333, 0]], [0.637045, [3, -0.0933333, 0], [3, 0.08, 0]], [0, [3, -0.08, 0], [3, 0, 0]]])

names.append("HeadYaw")
times.append([0.52])
keys.append([[0, [3, -0.173333, 0], [3, 0, 0]]])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  motion = ALProxy("ALMotion", IP, 9559)
  # motion = ALProxy("ALMotion")
  motion.angleInterpolationBezier(names, times, keys)
except BaseException, err:
  print err
