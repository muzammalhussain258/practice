import os
import webbrowser
import pyautogui

def handle(command):
    command = command.lower()

    # Apps & Tools
    if "open notepad" in command:
        os.system("notepad")
        return "Opening Notepad"
    elif "open calculator" in command:
        os.system("calc")
        return "Opening Calculator"
    elif "open file explorer" in command:
        os.system("explorer")
        return "Opening File Explorer"
    elif "open control panel" in command:
        os.system("control")
        return "Opening Control Panel"
    elif "open task manager" in command:
        os.system("taskmgr")
        return "Opening Task Manager"
    elif "open vs code" in command:
        os.system("vs code")
        return "Opening VS Code"
    elif "take screenshot" in command:
        pyautogui.screenshot("screenshot.png")
        return "Screenshot saved as screenshot.png"
    elif "lock computer" in command or "lock pc" in command:
        os.system("rundll32.exe user32.dll,LockWorkStation")
        return "Locking Computer"
    elif "open camera" in command:
        os.system("start microsoft.windows.camera:")
        return "Opening Camera"

    # Social Media
    elif "open facebook" in command or "facebook open" in command:
        webbrowser.open("https://www.facebook.com")
        return "Opening Facebook"
    elif "open whatsapp" in command or "whatsapp open" in command:
        webbrowser.open("https://web.whatsapp.com")
        return "Opening WhatsApp"
    elif "open chatgpt" in command or "chat gpt" in command:
        webbrowser.open("https://chat.openai.com")
        return "Opening ChatGPT"
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube"
    elif "open instagram" in command:
        webbrowser.open("https://www.instagram.com")
        return "Opening Instagram"
    elif "open twitter" in command or "open x" in command:
        webbrowser.open("https://twitter.com")
        return "Opening Twitter (X)"
    elif "open linkedin" in command:
        webbrowser.open("https://www.linkedin.com")
        return "Opening LinkedIn"
    elif "open telegram" in command:
        webbrowser.open("https://web.telegram.org")
        return "Opening Telegram"

    # Volume Control
    elif "volume up" in command:
        for _ in range(5): pyautogui.press("volumeup")
        return "Volume Increased"
    elif "volume down" in command:
        for _ in range(5): pyautogui.press("volumedown")
        return "Volume Decreased"
    elif "mute" in command:
        pyautogui.press("volumemute")
        return "Volume Muted"

    # System Control
    elif "shutdown" in command:
        os.system("shutdown /s /t 1")
        return "Shutting Down"
    elif "restart" in command:
        os.system("shutdown /r /t 1")
        return "Restarting Computer"

    return "Command not recognized"
