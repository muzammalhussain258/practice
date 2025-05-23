import customtkinter as ctk
from threading import Thread
from modules.voice import speak
from modules.stt import listen
from modules.system_control import handle as sys_control
from modules.web_search import handle as web_search
from modules.chat import handle as chat
from modules.nlp import classify_intent
from config import LANGUAGE_MODE

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class JarvisUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Jarvis Assistant")
        self.geometry("600x600")
        self.resizable(False, False)

        self.label = ctk.CTkLabel(self, text="Jarvis Voice Assistant", font=("Arial", 28, "bold"))
        self.label.pack(pady=20)

        self.output_box = ctk.CTkTextbox(self, width=540, height=320, font=("Arial", 15), wrap='word')
        self.output_box.pack(pady=10)
        self.output_box.insert("end", "Welcome! Type or Speak your command below.\n\n")

        self.entry = ctk.CTkEntry(self, width=370, font=("Arial", 15))
        self.entry.pack(side="left", padx=(35, 0), pady=20)

        self.send_btn = ctk.CTkButton(self, text="Send", width=60, command=self.handle_text)
        self.send_btn.pack(side="left", padx=(10, 0))

        self.speak_btn = ctk.CTkButton(self, text="🎤 Speak", width=60, command=self.handle_speak)
        self.speak_btn.pack(side="left", padx=(10, 0))

        self.stop_btn = ctk.CTkButton(self, text="Exit", width=60, command=self.quit)
        self.stop_btn.pack(side="left", padx=(10, 0))

    def handle_text(self):
        command = self.entry.get().strip()
        self.entry.delete(0, 'end')
        if command:
            self.output_box.insert("end", f"\nYou: {command}\n")
            self.process_command(command)

    def handle_speak(self):
        self.output_box.insert("end", "\nListening...\n")
        Thread(target=self.listen_and_process).start()

    def listen_and_process(self):
        lang_code = "ur-PK" if LANGUAGE_MODE == "urdu" else "en-US"
        command = listen(lang_code=lang_code)
        if command:
            self.output_box.insert("end", f"You (Mic): {command}\n")
            self.process_command(command)
        else:
            self.output_box.insert("end", "Didn't catch that. Try again.\n")

    def process_command(self, command):
        intent = classify_intent(command)
        response = None
        if intent == "system control":
            response = sys_control(command)
        elif intent == "web search":
            response = web_search(command)
        else:
            response = chat(command)
        if response:
            self.output_box.insert("end", f"Jarvis: {response}\n")
            speak(response, lang="ur" if LANGUAGE_MODE == "urdu" else "en")
        else:
            self.output_box.insert("end", "Jarvis: Sorry, I did not understand.\n")

if __name__ == "__main__":
    app = JarvisUI()
    app.mainloop()