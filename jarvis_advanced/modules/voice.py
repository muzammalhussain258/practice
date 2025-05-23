import pyttsx3

def speak(text, lang="en"):
    engine = pyttsx3.init()
    # Optional: Set Urdu voice if available
    if lang == "ur":
        voices = engine.getProperty('voices')
        for voice in voices:
            if "urdu" in voice.name.lower():
                engine.setProperty('voice', voice.id)
                break
    engine.say(text)
    engine.runAndWait()