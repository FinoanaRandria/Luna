import speech_recognition as sr
import pyttsx3 as ttx
import datetime
import pywhatkit


listener = sr.Recognizer()
engine = ttx.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', 'french')


def parler(text):
    engine.say(text)
    engine.runAndWait()


def ecouter():
    try:
        with sr.Microphone() as source:
            print('Parler maintenant')
            voix = listener.listen(source)
            command = listener.recognize_google(voix, language='fr-FR')
            command.lower()

    except:
        pass
    return command     

def lancer_assistant():
    command=ecouter()
    print(command)
    if 'Met la chansons de' in command:
        chanteur=command.replace('Met la chansons de','')
        print(chanteur)
        pywhatkit.playonyt(chanteur)
        
        
    elif 'Bonjour' in command:
        text='boujour, ca va ?'
        parler(text)   
        
    elif 'Luna'  in command:
        text='Je suis luna un assistant creer par finoana!'
        parler(text)
    
    elif 'heure' in command:
        heure= datetime.datetime.now().strftime('%H'+'heure'+'%M')
        parler('il est'+heure)
      
        
lancer_assistant()