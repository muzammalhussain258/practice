from config import LANGUAGE_MODE
from modules.voice import speak
from modules.stt import listen
from modules.system_control import handle as sys_control
from modules.web_search import handle as web_search
from modules.chat import handle as chat
from modules.nlp import classify_intent

def main():
    lang_code = "ur-PK" if LANGUAGE_MODE == "urdu" else "en-US"
    speak("Jarvis is ready. How can I help you?", lang="ur" if LANGUAGE_MODE == "urdu" else "en")
    while True:
        command = listen(lang_code=lang_code)
        if not command:
            continue
        if any(x in command for x in ["exit", "quit", "band karo"]):
            speak("Goodbye!", lang="ur" if LANGUAGE_MODE == "urdu" else "en")
            break

        # Deep learning/NLP intent detection
        intent = classify_intent(command)
        response = None
        if intent == "system control":
            response = sys_control(command)
        elif intent == "web search":
            response = web_search(command)
        else:
            response = chat(command)
        if response:
            speak(response, lang="ur" if LANGUAGE_MODE == "urdu" else "en")
        else:
            speak("Sorry, I did not understand.", lang="ur" if LANGUAGE_MODE == "urdu" else "en")

if __name__ == "__main__":
    main()