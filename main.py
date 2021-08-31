import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init(driverName='espeak')
voices = engine.getProperty('voices')
engine.setProperty("rate", 178)
engine.setProperty('voice', 'english_rp+f3')
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)
error = False


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            google_command = listener.recognize_google(voice)
            google_command = google_command.lower()
            if 'jarvis' in google_command:
                google_command = google_command.replace('jarvis', '')
                print(google_command)
                return google_command
    except Exception:
        print(Exception.with_traceback())
        global error
        error = True
        return 'Not found!'


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        pass
        talk('Please say the command again.')


while not error:
    run_alexa()
