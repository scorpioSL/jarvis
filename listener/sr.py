import speech_recognition as sr
from talk.google import google_talk


def take_command():
    try:
        listener = sr.Recognizer()
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source=source)
            if voice:
                google_command = listener.recognize_google(voice)
                google_command = google_command.lower()
                if 'jarvis' in google_command:
                    google_command = google_command.replace('jarvis', '')
                    return google_command
                else:
                    return 'Not Found!'
            else:
                return None
    except Exception:
        return None
