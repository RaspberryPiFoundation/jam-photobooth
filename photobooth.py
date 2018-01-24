from jam_picamera import JamPiCamera
from auth import CON_KEY, CON_SEC, ACC_TOK, ACC_SEC
from gpiozero import Button
from twython import Twython
from time import sleep

camera = JamPiCamera()
button = Button(25, hold_time=5)
twitter = Twython(CON_KEY, CON_SEC, ACC_TOK, ACC_SEC)

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
        photo = camera.capture()
        camera.annotate_text = "Tweeting..."
        with open(photo, 'rb') as p:
            response = twitter.upload_media(media=p)
        media = response['media_id']
        twitter.update_status(status="testing...", media_ids=media)
        camera.annotate_text = "Tweeted!"
        sleep(1)
        camera.annotate_text = None
