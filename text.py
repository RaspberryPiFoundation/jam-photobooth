# English
text_en = {
    'tweet': "#PiParty photo booth",
    'photo number': "Photo {} of {}",
    'press to capture': "Press the button to capture...",
    'tweeting': "Tweeting...",
    'tweeted': "Tweeted!",
    'tweeting with cancel': "Tweeting...\n" "Press the button to cancel",
    'ready': "Ready!\n" "Press the button to start...",
    'failed tweet': "Failed to tweet :(",
    'not tweeting': "Not tweeting",
}

# German - Deutsche
text_de = {
    'tweet': "#PiParty Fotoautomat",
    'photo number': "Foto {} von {}",
    'press to capture': "Drucke den Knopf fur ein Foto...",
    'tweeting': "Am Twittern...",
    'tweeted': "Getwittert!",
    'tweeting with cancel': "Am Twittern...\n" "Drucke den Knopf um abzubrechen",
    'ready': "Bereit!\n" "Drucke den Knopf um zu starten...",
    'failed tweet': "Fehler beim Twittern :(",
    'not tweeting': "Nicht am Twittern",
}

# French - Français
text_fr = {
    'tweet': "#PiParty photomaton",
    'photo number': "Photo {} de {}",
    'press to capture': "Appuyez sur le bouton pour capturer...",
    'tweeting': "Tweeting...",
    'tweeted': "Tweeted!",
    'tweeting with cancel': "Tweeting...\n" "Appuyez sur le bouton pour annuler",
    'ready': "Pret!\n" "Appuyez sur le bouton pour commencer...",
    'failed tweet': "Echec du tweet :(",
    'not tweeting': "Pas de tweeting",
}

# Spanish - Español
text_es = {
    'tweet': "#PiParty cabina de fotos",
    'photo number': "Foto {} de {}",
    'press to capture': "Presione el boton para capturar...",
    'tweeting': "Tweeting...",
    'tweeted': "Tweeted!",
    'tweeting with cancel': "Tweeting...\n" "Presione el boton para cancelar",
    'ready': "Listo!\n" "Presione el boton para comenzar...",
    'failed tweet': "Error al twittear :(",
    'not tweeting': "No twitteando",
}

# Welsh - Cymraeg
text_cy = {
    'tweet': "#PiParty bwth lluniau",
    'photo number': "Llun {} o {}",
    'press to capture': "Gwasgwch y botwm i'w dal...",
    'tweeting': "Tweetio...",
    'tweeted': "Tweetio!",
    'tweeting with cancel': "Tweetio...\n" "Gwasgwch y botwm i ganslo",
    'ready': "Yn barod!\n" "Gwasgwch y botwm i ddechrau...",
    'failed tweet': "Methwyd tweet :(",
    'not tweeting': "Ddim yn tweetio",
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
