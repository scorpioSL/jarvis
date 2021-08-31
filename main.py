import datetime
from talk.google import google_talk
from listener.sr import take_command
from jokes.pyJoke import get_joke
from wiki.wiki import ask_wiki
from media.audio import play

error = False


def run_alexa():
    command = take_command()
    print(command)
    if command is None:
        global error
        error = True
        return
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        google_talk('playing ' + song)
        play(song)
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        google_talk('Current time is ' + current_time)
    elif 'who is' in command:
        person = command.replace('who the heck is', '')
        google_talk(ask_wiki(person))
    elif 'date' in command:
        google_talk('sorry, I have a headache')
    elif 'are you single' in command:
        google_talk('I am in a relationship with wifi')
    elif 'joke' in command:
        google_talk(get_joke())
    else:
        pass
        google_talk('Please say the command again.')


while not error:
    run_alexa()
    # time.sleep(5)
