import os
from playsound import playsound
import time
from gtts import gTTS

language = 'en'


def google_talk(text):
    tts = gTTS(text, lang=language, slow=True)
    tts.save('response.mp3')
    time.sleep(1)
    playsound('response.mp3', block=False)
    time.sleep(2)
    os.remove('./response.mp3')
