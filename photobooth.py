from jam_picamera import JamPiCamera
from auth import CON_KEY, CON_SEC, ACC_TOK, ACC_SEC
from gpiozero import Button
from twython import Twython
from time import sleep
import logging

logger = logging.getLogger('photobooth')
logging.basicConfig(level=logging.INFO)
logger.info("starting")

camera = JamPiCamera()
button = Button(25, hold_time=5)
if CON_KEY:
    twitter = Twython(CON_KEY, CON_SEC, ACC_TOK, ACC_SEC)
else:
    twitter = None

camera.resolution = (1024, 768)
camera.hflip = True
camera.start_preview()
camera.annotate_text_size = 70

tweet_text = "Test tweet #somehashtag"

def quit():
    logger.info("quitting")
    global running
    running = False
    camera.annotate_text = "Button held. Release to exit..."

def countdown(n):
    logger.info("running countdown")
    for i in reversed(range(n)):
        camera.annotate_text = '{}...'.format(i + 1)
        sleep(1)
    camera.annotate_text = None

def capture_photos(n):
    photos = []
    for pic in range(n):
        camera.annotate_text = "Photo {} of 4".format(pic + 1)
        sleep(1)
        camera.annotate_text = "Press the button to capture..."
        button.wait_for_press()
        logger.info("button pressed")
        button.wait_for_release()
        logger.info("button released")
        sleep(1)
        countdown(3)
        logger.info("capturing photo")
        photo = camera.capture()
        photos.append(photo)
    return photos

def upload_photos(photos):
    media_ids = []
    for photo in photos:
        try:
            with open(photo, 'rb') as f:
                response = twitter.upload_media(media=f)
            media_ids.append(response['media_id'])
        except:
            pass
    return media_ids

button.when_held = quit

running = True
while running:
    logger.info("waiting for button press")
    camera.annotate_text = "Ready!\n" "Press the button to start..."
    button.wait_for_press()
    photos = capture_photos(4)
    if twitter:
        logger.info("twitter enabled")
        camera.annotate_text = "Tweeting...\n" "Press the button to cancel"
        sleep(3)
        camera.annotate_text = "Tweeting..."
        try:
            uploaded_photos = upload_photos(photos)
            twitter.update_status(status=tweet_text, media_ids=uploaded_photos)
            logger.info("tweeted successfully")
            camera.annotate_text = "Tweeted!"
            sleep(1)
        except:
            logger.info("failed to tweet")
            camera.annotate_text = "Failed to tweet :("
            sleep(2)
    else:
        logger.info("twitter disabled")
    camera.annotate_text = None
