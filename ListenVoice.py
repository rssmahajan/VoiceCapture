import speech_recognition as sr
import threading

stop_listening = False

def listen_to_voice():
    global stop_listening
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Press Enter to stop.")
        while not stop_listening:
            try:
                audio = recognizer.listen(source, timeout=1, phrase_time_limit=5)
                text = recognizer.recognize_google(audio)
                print(f"You said: {text}")
            except sr.WaitTimeoutError:
                continue  # No speech detected within timeout
            except sr.UnknownValueError:
                print("Sorry, could not understand audio.")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")

def stop_listen_on_enter():
    global stop_listening
    input()
    stop_listening = True
