# -*- encoding: UTF-8 -*-

from naoqi import ALProxy

IP = '127.0.0.1'
PORT = 49340

motion_proxy = ALProxy("ALMotion",IP,PORT)
motion_proxy.openHand('LHand')
motion_proxy.openHand('RHand')
