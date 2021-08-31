import wikipedia


def ask_wiki(question):
    try:
        info = wikipedia.summary(question, 1)
        print(info)
        return info
    except Exception:
        return "sorry, I didn't find any result"
