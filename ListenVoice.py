import speech_recognition as sr
import threading
import keyboard  # New import
from TextFilter import extract_numbers
from SaveToDB import save_to_database
from TextTranslator import translate_to_english
from TextTranslator import translate_to_english
from NumberNormalizer import normalize_numbers


stop_listening = False
stop_keywords = ["stop processing", "terminate processing", "exit code", "terminate code" ]

def listen_to_voice():
    global stop_listening
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening...Say 'stop processing' or press Enter to stop.")
        while not stop_listening:
            try:
                audio = recognizer.listen(source, timeout=1, phrase_time_limit=5)

                # First try Marathi
                try:
                    text = recognizer.recognize_google(audio, language="hi-IN")
                except sr.UnknownValueError:
                    # If Marathi fails, try Hindi
                    text = recognizer.recognize_google(audio, language="mr-IN")

                print(f"You said (regional): {text}")

                translated_text = translate_to_english(text)
                normalized_text = normalize_numbers(translated_text)
                #print(f"Translated to English: {translated_text}")
                print(f"Normalized text (numbers): {normalized_text}")

                # Check if spoken text matches stop keywords
                if any(keyword in translated_text.lower() for keyword in stop_keywords):
                    print("Stop keyword detected. Stopping...")
                    stop_listening = True
                else:
                    numbers = extract_numbers(normalized_text)
                    if numbers:
                        save_to_database(numbers)


            except sr.WaitTimeoutError:
                continue  # No speech detected within timeout
            except sr.UnknownValueError:
                print("Sorry, could not understand audio.")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")

def stop_listen_on_enter():
    global stop_listening
    while not stop_listening:
        if keyboard.is_pressed('enter'):
            print("Enter key pressed. Stopping...")
            stop_listening = True


