from jam_picamera import JamPiCamera
from gpiozero import Button
from time import sleep

camera = JamPiCamera()

camera.resolution = (1024, 768)
camera.hflip = True
camera.start_preview()

while True:
    input("Press Enter ")
    camera.capture()
