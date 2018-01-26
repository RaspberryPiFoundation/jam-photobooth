# English
text_en = {
    'tweet': "#PiParty photobooth",
    'photo number': "Photo {} of 4",
    'press to capture': "Press the button to capture...",
    'tweeting': "Tweeting...",
    'tweeted': "Tweeted!",
    'tweeting with cancel': "Tweeting...\n" "Press the button to cancel",
    'ready': "Ready!\n" "Press the button to start...",
    'failed tweet': "Failed to tweet :(",
}

# German - Deutsche
text_de = {
    'tweet': "#PiParty fotoautomat",
    'photo number': "Foto {} von 4",
    'press to capture': "Drucken Sie die Taste, um zu erfassen...",
    'tweeting': "Twittern...",
    'tweeted': "Getwittert!",
    'tweeting with cancel': "Twittern...\n" "Drucken Sie die Taste, um abzubrechen",
    'ready': "Bereit!\n" "Drucken Sie die Taste um zu starten...",
    'failed tweet': "Fehler beim Twittern :(",
}

# French - Français
text_fr = {
    'tweet': "#PiParty photobooth",
    'photo number': "Photo {} de 4",
    'press to capture': "Appuyez sur le bouton pour capturer...",
    'tweeting': "Tweeting...",
    'tweeted': "Tweeted!",
    'tweeting with cancel': "Tweeting...\n" "Appuyez sur le bouton pour annuler",
    'ready': "Ready!\n" "Appuyez sur le bouton pour commencer...",
    'failed tweet': "Échec du tweet :(",
}

# Spanish - Español
text_es = {
    'tweet': "#PiParty cabina de fotos",
    'photo number': "Foto {} de 4",
    'press to capture': "Presione el botón para capturar...",
    'tweeting': "Tweeting...",
    'tweeted': "Tweeted!",
    'tweeting with cancel': "Tweeting...\n" "Presione el botón para cancelar",
    'ready': "Ready!\n" "Presione el botón para comenzar...",
    'failed tweet': "Error al twittear :(",
}

# Welsh - Cymraeg
text_cy = {
    'tweet': "#PiParty photobooth",
    'photo number': "Llun {} o 4",
    'press to capture': "Gwasgwch y botwm i'w dal...",
    'tweeting': "Tweeting...",
    'tweeted': "Tweeted!",
    'tweeting with cancel': "Tweeting...\n" "Gwasgwch y botwm i ganslo",
    'ready': "Ready!\n" "Gwasgwch y botwm i ddechrau...",
    'failed tweet': "Methwyd tweet :(",
}

def get_text(language='en'):
    """
    Retrieve a dictionary of text in the specified language, if available
    """
    return {
        'en': text_en,
        'de': text_de,
        'fr': text_fr,
        'es': text_es,
        'cy': text_cy,
    }[language]
