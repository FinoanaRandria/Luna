import speech_recognition as sr

listener = sr.Recognizer()


try:
    with sr.Microphone() as source:
        print('Parler maintenant')