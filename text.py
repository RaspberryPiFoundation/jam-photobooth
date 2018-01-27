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
    'failed tweet': "Echec du tweet :(",
}

# Spanish - Español
text_es = {
    'tweet': "#PiParty cabina de fotos",
    'photo number': "Foto {} de 4",
    'press to capture': "Presione el boton para capturar...",
    'tweeting': "Tweeting...",
    'tweeted': "Tweeted!",
    'tweeting with cancel': "Tweeting...\n" "Presione el boton para cancelar",
    'ready': "Ready!\n" "Presione el boton para comenzar...",
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

language_dicts = {
    'en': text_en,
    'de': text_de,
    'fr': text_fr,
    'es': text_es,
    'cy': text_cy,
}

def get_text(language='en'):
    """
    Retrieve a dictionary of text in the specified language, if available
    """
    return language_dicts[language]

# test for non-ascii characters not supported by the camera firmware
for language in language_dicts.values():
    for key, text in language.items():
        if key != 'tweet':
            assert all(ord(c) in range(128) for c in text), text
