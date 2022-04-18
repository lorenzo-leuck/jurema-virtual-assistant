import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

# import webbrowser
# import random
# import os
# import pyaudio


v = 0
wikipedia.set_lang("pt")
listener = sr.Recognizer()
engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)
def fala(text):
    engine.say(text)
    engine.runAndWait()

def roda_jurema():
    global v
    try: 
        with sr.Microphone() as source:
            # fala("Tô te ouvindo..")
            print("Tô te ouvindo..")
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language="pt-BR")
            command = command.lower()
            print(command)
            if "jurema" in command:
                command = command.replace("jurema","")

                if "toca" in command:
                    song = command.replace("toca","")
                    fala("tocando" + song)
                    pywhatkit.playonyt(song)
                elif "hora" in command:
                    time = datetime.datetime.now().strftime("%H:%M")
                    fala("Agora é" + time)
                elif "wikipédia" in command:
                    wiki = command.replace("wikipédia","")
                    info = wikipedia.summary(wiki, 1)
                    print(info)
                    fala(info)
                elif "pesquisa" in command:
                    google = command.replace("pesquisa","")
                    pesquisa = pywhatkit.search(google)
                    print(pesquisa)
                    talk(pesquisa)
                elif "sentido da vida" in command:
                    fala("o sentido da vida é ser os olhos e os ouvidos de deus, seu idiota")
                elif "oi" in command:
                    fala("oi lorenzo")                    
                else:
                    fala("Não entendi")    
            elif "tchau" in command:
                fala("falou")    
                v = 1
            else:
                fala("te conheço, porra?")
    except:       
        pass
 
while (v == 0):
    roda_jurema()

