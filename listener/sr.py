import speech_recognition as sr


def take_command():
    try:
        listener = sr.Recognizer()
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            print(voice)
            google_command = listener.recognize_google(voice)
            google_command = google_command.lower()
            print(google_command)
            if 'jarvis' in google_command:
                google_command = google_command.replace('jarvis', '')
                print(google_command)
                return google_command
            else:
                return 'Not Found!'
    except Exception:
        print(Exception.with_traceback())
        return None
