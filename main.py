import speech_recognition as sr

listener = sr.Recognizer()


try:
    with sr.Microphone() as source:
        print('Parler maintenant')
        voix = listener.listen(source)
        command = listener.recognize_google(voix)
        print(command)
except:
    pass