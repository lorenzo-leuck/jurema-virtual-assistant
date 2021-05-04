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




# def wish():
#     hour = int(datetime.datetime.now().hour)
#     if hour >= 0 and hour < 12:
#         speak("good morning, i am your virtual assistant")
#     elif hour >= 12 and hour < 18:
#         speak("good afternoon, i am your virtual assistant")
#     else:
#         speak("hello, i am your virtual assistant")

# elif "what's up" in query:
#                 stMsgs = ['asif now im only helping you with whatever you need me for', 'I am fine!, lets talk about you are you fine?', 'oh, nothing','i am okay ! How are you']
#                 ans_q = random.choice(stMsgs)
#                 speak(ans_q)  
#                 ans_take_from_user_how_are_you = takeCommand()


# if "whats the weather " in query:
#                 speak("looking for the weather...")
#                 #r = sr.Recognizer()
#                 results =webbrowser.open("https://www.google.com/search?rlz=1C1CHBF_enIN911IN911&biw=1536&bih=763&sxsrf=ALeKk02WEeO5ibqsklVfK4AaRYshJYil7g%3A1598262964246&ei=tI5DX63LDrSX4-EP_bOA8A4&q=google+weather&oq=googweather&gs_lcp=CgZwc3ktYWIQAxgAMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB46BAgAEEdQ7i1Y0jJgwTxoAHACeAGAAYEDiAHmBZIBBzEuMi4wLjGYAQCgAQGqAQdnd3Mtd2l6wAEB&sclient=psy-ab")

#  elif "open youtube" in query:
#                 speak("opening youtube")
#                 webbrowser.open("www.youtube.com")

# elif "music from laptop" in query or "music" in query:
#     speak("ok playing music")
#     music_dir = "./music"
#     musics = os.listdir(music_dir)
#     os.startfile(os.path.join(music_dir, musics[0]))


# elif "open my gmail" in query:
#                 speak("okay, opening your gmail")
#                 webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

#             elif "open spotify" in query:
#                 speak("opening spotify")
#                 webbrowser.open("https://open.spotify.com/")