import pyjokes
import datetime
import wikipedia

def handle(command):
    if "joke" in command:
        return pyjokes.get_joke()
    elif "time" in command:
        return f"Current time is {datetime.datetime.now().strftime('%I:%M %p')}"
    elif "who is" in command or "what is" in command:
        try:
            return wikipedia.summary(command, 2)
        except:
            return "Sorry, I couldn't find information."
    return None