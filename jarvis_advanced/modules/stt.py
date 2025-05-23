import speech_recognition as sr

def listen(lang_code="en-US"):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language=lang_code)
            print(f"You said: {text}")
            return text.lower()
        except Exception as e:
            print("Error:", e)
            return ""