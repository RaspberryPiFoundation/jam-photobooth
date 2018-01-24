from jam_picamera import JamPiCamera
from gpiozero import Button
from time import sleep

camera = JamPiCamera()

button = Button(25, hold_time=5)

camera.resolution = (1024, 768)
camera.hflip = True
camera.start_preview()
camera.annotate_text_size = 70

def quit():
    global running
    running = False
    camera.annotate_text = "Button held. Release to exit..."

button.when_held = quit

running = True
while running:
    button.wait_for_press()
    button.wait_for_release()
    if running:
        for i in reversed(range(3)):
            camera.annotate_text = '{}...'.format(i + 1)
            sleep(1)
        camera.annotate_text = None
        camera.capture()
