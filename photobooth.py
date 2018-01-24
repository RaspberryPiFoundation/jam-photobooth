from jam_picamera import JamPiCamera
from gpiozero import Button
from time import sleep

camera = JamPiCamera()

camera.resolution = (1024, 768)
camera.hflip = True
camera.start_preview()
camera.annotate_text_size = 70

while True:
    input("Press Enter ")
    for i in reversed(range(3)):
        camera.annotate_text = '{}...'.format(i + 1)
        sleep(1)
    camera.annotate_text = None
    camera.capture()
