import sys
from naoqi import ALProxy

IP = '192.168.3.9'
PORT = 9559

tts = ALProxy("ALTextToSpeech", IP, PORT)
print tts

tts.setLanguage("English")

#Says a test std::string, and save it into a file
tts.sayToFile("This is a sample text, written in a file!", "/home/nao/recordings/cameras/sample_text.wav")

#Says a test std::string, and save it into a file
#tts.sayToFile("This is another sample text", "/Users/yasushisakai/Desktop/sample_text.raw")
