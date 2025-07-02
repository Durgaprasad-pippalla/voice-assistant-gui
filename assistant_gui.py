import tkinter as tk
from tkinter import scrolledtext
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import sys
import threading

# Initialize engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)
engine.setProperty('voice', engine.getProperty('voices')[1].id)

def talk(text):
    log_output(f"🎙️ GIRI: {text}")
    engine.say(text)
    engine.runAndWait()

def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        log_output("🎧 Listening...")
        listener.adjust_for_ambient_noise(source)
        voice = listener.listen(source)
    try:
        command = listener.recognize_google(voice)
        command = command.lower()
        log_output(f"🗣️ You said: {command}")
    except sr.UnknownValueError:
        talk("Sorry bro, I didn’t catch that.")
        return ""
    except sr.RequestError:
        talk("Network issue with Google service.")
        return ""
    return command

def run_bannu():
    command = take_command()

    if "play" in command:
        song = command.replace("play", "")
        talk("Playing on YouTube 🎶")
        pywhatkit.playonyt(song)

    elif "what's the time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"It’s {time} ⏰")

    elif "who is" in command:
        person = command.replace("who is", "").strip()
        try:
            info = wikipedia.summary(person, sentences=1)
            talk(info)
        except:
            talk("Sorry, I couldn’t find info.")

    elif "joke" in command:
        talk(pyjokes.get_joke())

    elif "open chrome" in command:
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        if os.path.exists(chrome_path):
            talk("Opening Chrome 🚀")
            os.startfile(chrome_path)
        else:
            talk("Chrome not found 😬")

    elif "open code" in command or "open vs code" in command:
        talk("Opening VS Code 💻")
        os.system("code")

    elif "exit" in command or "stop" in command:
        talk("Okay bro, see you later 👋")
        root.destroy()
        sys.exit()

    elif command != "":
        talk("I heard you, but I don’t understand that yet 😅")

# ---------------------- GUI -----------------------

def log_output(text):
    output_box.insert(tk.END, text + "\n")
    output_box.see(tk.END)

def start_listening():
    threading.Thread(target=run_bannu).start()

root = tk.Tk()
root.title("Voice Assistant – Bannu")
root.geometry("500x400")
root.resizable(False, False)

tk.Label(root, text="🎤 Click to Talk to Bannu", font=("Arial", 16)).pack(pady=10)
tk.Button(root, text="Start Listening", font=("Arial", 14), command=start_listening, bg="green", fg="white").pack(pady=10)

output_box = scrolledtext.ScrolledText(root, font=("Arial", 12), width=60, height=15, wrap=tk.WORD)
output_box.pack(padx=10, pady=10)

talk("Yo! I'm Bannu – your personal voice assistant 💡")
root.mainloop()
