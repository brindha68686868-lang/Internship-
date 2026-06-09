import tkinter as tk
import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            result_label.config(text="Listening...")
            window.update()

            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

            result_label.config(text="Recognizing...")
            window.update()

            text = recognizer.recognize_google(audio)

            result_label.config(text=f"You said:\n{text}")

    except sr.UnknownValueError:
        result_label.config(text="Could not understand audio.")

    except sr.RequestError:
        result_label.config(text="Internet connection required.")

    except Exception as e:
        result_label.config(text=f"Error: {e}")

# GUI Window
window = tk.Tk()
window.title("Speech Recognition App")
window.geometry("500x300")

title_label = tk.Label(
    window,
    text="Speech Recognition App",
    font=("Arial", 16, "bold")
)
title_label.pack(pady=20)

listen_button = tk.Button(
    window,
    text="🎤 Start Listening",
    font=("Arial", 12),
    command=recognize_speech
)
listen_button.pack(pady=10)

result_label = tk.Label(
    window,
    text="Click the button and speak.",
    wraplength=450,
    font=("Arial", 12)
)
result_label.pack(pady=20)

window.mainloop()