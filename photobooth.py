from jam_picamera import JamPiCamera
from auth import CON_KEY, CON_SEC, ACC_TOK, ACC_SEC
from text import get_text
from gpiozero import Button
from twython import Twython
from time import sleep
import logging

logger = logging.getLogger('photobooth')
logging.basicConfig(level=logging.INFO)
logger.info("starting")

text = get_text(language='en')

camera = JamPiCamera()
button = Button(14, hold_time=5)
if CON_KEY:
    twitter = Twython(CON_KEY, CON_SEC, ACC_TOK, ACC_SEC)
else:
    twitter = None

camera.resolution = (1024, 768)
camera.hflip = True
camera.start_preview()
camera.annotate_text_size = 70

def quit():
    logger.info("quitting")
    camera.close()

def countdown(n):
    logger.info("running countdown")
    for i in reversed(range(n)):
        camera.annotate_text = '{}...'.format(i + 1)
        sleep(1)
    camera.annotate_text = None

def capture_photos(n):
    """
    Capture n photos in sequence and return a list of file paths
    """
    photos = []
    for pic in range(n):
        camera.annotate_text = text['photo number'].format(pic + 1, n)
        sleep(1)
        camera.annotate_text = text['press to capture']
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
    """
    Upload the provided photo files to Twitter and return the list of media IDs
    """
    media_ids = []
    for photo in photos:
        try:
            with open(photo, 'rb') as f:
                response = twitter.upload_media(media=f)
            media_ids.append(response['media_id'])
        except:
            pass
    return media_ids

def tweet_photos(status, photos):
    """
    Send a tweet with the status provided, with the photos provided attached
    """
    logger.info("tweeting")
    camera.annotate_text = text['tweeting']
    twitter.update_status(status=status, media_ids=photos)
    logger.info("tweeted successfully")
    camera.annotate_text = text['tweeted']

button.when_held = quit

while True:
    camera.annotate_text = text['ready']
    logger.info("waiting for button press")
    button.wait_for_press()
    logger.info("button pressed")
    photos = capture_photos(4)
    if twitter:
        logger.info("twitter enabled")
        camera.annotate_text = text['tweeting with cancel']
        pressed = button.wait_for_press(timeout=3)
        if pressed:
            logger.info("button pressed - not tweeting")
            camera.annotate_text = text['not tweeting']
            button.wait_for_release()
            sleep(2)
        else:
            logger.info("button not pressed - tweeting")
            try:
                uploaded_photos = upload_photos(photos)
                tweet_photos(text['tweet'], uploaded_photos)
                sleep(1)
            except:
                logger.info("failed to tweet")
                camera.annotate_text = text['failed tweet']
                sleep(2)
    else:
        logger.info("twitter disabled")
    camera.annotate_text = None
