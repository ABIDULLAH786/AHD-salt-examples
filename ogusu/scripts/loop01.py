# Choregraphe bezier export in Python.
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
times.append([0.52])
keys.append([[-0.19635, [3, -0.173333, 0], [3, 0, 0]]])

names.append("HeadYaw")
times.append([0.52])
keys.append([[0.00613595, [3, -0.173333, 0], [3, 0, 0]]])

names.append("HipPitch")
times.append([0.52])
keys.append([[-0.0475532, [3, -0.173333, 0], [3, 0, 0]]])

names.append("HipRoll")
times.append([0.52])
keys.append([[0.0122719, [3, -0.173333, 0], [3, 0, 0]]])

names.append("KneePitch")
times.append([0.52])
keys.append([[-0.0153399, [3, -0.173333, 0], [3, 0, 0]]])

names.append("LElbowRoll")
times.append([0.52, 0.92])
keys.append([[-0.69115, [3, -0.173333, 0], [3, 0.133333, 0]], [-0.00872665, [3, -0.133333, 0], [3, 0, 0]]])

names.append("LElbowYaw")
times.append([0.52, 0.92])
keys.append([[-0.862193, [3, -0.173333, 0], [3, 0.133333, 0]], [0, [3, -0.133333, 0], [3, 0, 0]]])

names.append("LHand")
times.append([0.52, 0.92])
keys.append([[0.35, [3, -0.173333, 0], [3, 0.133333, 0]], [1, [3, -0.133333, 0], [3, 0, 0]]])

names.append("LShoulderPitch")
times.append([0.52, 0.92])
keys.append([[1.56926, [3, -0.173333, 0], [3, 0.133333, 0]], [1.48178, [3, -0.133333, 0], [3, 0, 0]]])

names.append("LShoulderRoll")
times.append([0.52, 0.92])
keys.append([[0.765456, [3, -0.173333, 0], [3, 0.133333, 0]], [1.56207, [3, -0.133333, 0], [3, 0, 0]]])

names.append("LWristYaw")
times.append([0.52, 0.92])
keys.append([[-1.06291, [3, -0.173333, 0], [3, 0.133333, 0]], [-1.82387, [3, -0.133333, 0], [3, 0, 0]]])

names.append("RElbowRoll")
times.append([0.52, 0.92])
keys.append([[0.69115, [3, -0.173333, 0], [3, 0.133333, 0]], [0.00872665, [3, -0.133333, 0], [3, 0, 0]]])

names.append("RElbowYaw")
times.append([0.52, 0.92])
keys.append([[0.862193, [3, -0.173333, 0], [3, 0.133333, 0]], [0, [3, -0.133333, 0], [3, 0, 0]]])

names.append("RHand")
times.append([0.52, 0.92])
keys.append([[0.35, [3, -0.173333, 0], [3, 0.133333, 0]], [1, [3, -0.133333, 0], [3, 0, 0]]])

names.append("RShoulderPitch")
times.append([0.52, 0.92])
keys.append([[1.5708, [3, -0.173333, 0], [3, 0.133333, 0]], [1.48178, [3, -0.133333, 0], [3, 0, 0]]])

names.append("RShoulderRoll")
times.append([0.52, 0.92])
keys.append([[-0.763922, [3, -0.173333, 0], [3, 0.133333, 0]], [-1.56207, [3, -0.133333, 0], [3, 0, 0]]])

names.append("RWristYaw")
times.append([0.52, 0.92])
keys.append([[1.06291, [3, -0.173333, 0], [3, 0.133333, 0]], [1.82387, [3, -0.133333, 0], [3, 0, 0]]])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  motion = ALProxy("ALMotion", IP, 9559)
  # motion = ALProxy("ALMotion")
  motion.angleInterpolationBezier(names, times, keys)
except BaseException, err:
  print err
