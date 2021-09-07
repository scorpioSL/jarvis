from datetime import datetime
from talk.google import google_talk
from listener.sr import take_command
from jokes.pyJoke import get_joke
from wiki.wiki import ask_wiki
from media.audio import play
import time


def get_talk(command):
    if 'play' in command:
        song = command.replace('play', '')
        play(song)
        return 'playing ' + song
    elif 'time' in command:
        current_time = datetime.now().strftime('%I:%M %p')
        return  'Current time is ' + current_time
    elif 'who is' in command:
        person = command.replace('who is', '')
        return ask_wiki(person)
    elif 'what is' in command:
        person = command.replace('what is', '')
        return ask_wiki(person)
    elif 'date' and 'what' and 'today' in command:
        return 'Today is ' + datetime.today().strftime('%Y-%m-%d')
    elif 'are you single' in command:
        return 'I am in a relationship with wifi'
    elif 'joke' in command:
        return get_joke()
    else:
        return None


class Jarvis:
    error = False

    def run(self):
        while not self.error:
            command = take_command()
            print(command)
            if command is not None:
                tell = get_talk(command)
                if tell is not None:
                    google_talk(tell)
