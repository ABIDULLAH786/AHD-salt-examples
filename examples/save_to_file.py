import sys
from naoqi import ALProxy

IP = '127.0.0.1'
PORT = 49340

tts = ALProxy("ALTextToSpeech", IP, PORT)

#Says a test std::string, and save it into a file
#tts.sayToFile("This is a sample text, written in a file!", "/Users/yasushisakai/Desktop/sample_text.wav")

#Says a test std::string, and save it into a file
tts.sayToFile("This is another sample text", "/Users/yasushisakai/Desktop/sample_text.raw")
