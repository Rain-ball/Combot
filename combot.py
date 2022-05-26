import pyttsx3
import speech_recognition as sr
import webbrowser as wb
import os
from googlesearch import search
from translate import Translator
engine = pyttsx3.init()
voices = engine.getProperty("voices")
r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()
wbsearch = wb.get()
x = 2

engine.setProperty("voice", voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

print("Hello, I am ComBot, your voice assistant. Nice to meet you.")
speak("Hello, I am ComBot, your voice assistant. Nice to meet you.")
print("How may I help you?")
speak("How may I help you?(make sure you have internet connected)")
with sr.Microphone() as source:
    defaultvoice = voices[0]
    prevvoice = defaultvoice
    while x == 2:
        engine.setProperty("voice", defaultvoice.id)
        if prevvoice != defaultvoice:
            print("How may I help you?")
            speak("How may I help you?(make sure you have internet connected)")
            prevvoice = defaultvoice
        print("Listening...")
        audio = r3.listen(source)
        print("You said : " + r1.recognize_google(audio))
        speak("You said : " + r1.recognize_google(audio))
        try:
            if r1.recognize_google(audio) == "search YouTube":
                speak("Search query please")
                print("Listening...")
                audio = r1.listen(source)
                print("You said : " + r1.recognize_google(audio))
                get = r1.recognize_google(audio)
                url = "https://www.youtube.com/results?search_query="
                wbsearch.open(url + get)
            if r1.recognize_google(audio) == "open oneline compiler":
                get = "https://onlinegdb.com"
                wbsearch.open_new(get)
            if r1.recognize_google(audio) == "search Google":
                speak("Search query please")
                print("Listening...")
                audio = r1.listen(source)
                query = r1.recognize_google(audio)
                print("You said : " + query)
                for j in search(query, tld="com", num=15, stop=15, pause=2):
                    print(j)
            if r1.recognize_google(audio) == "open Notepad":
                os.startfile("notepad.exe")
            if r1.recognize_google(audio) == "open 1 note":
                os.startfile("onenote.exe")
            if r1.recognize_google(audio) == "open Microsoft paint":
                os.startfile("mspaint.exe")
            if r1.recognize_google(audio) == "translate to Japanese":
                translator = Translator(to_lang = "Japanese")
                speak("Translate phrase please")
                engine.setProperty("voice", voices[2].id)
                audio = r1.listen(source)
                query = r1.recognize_google(audio)
                translation = translator.translate(query)
                print("You said : " + query)
                print(translation)
                speak(translation)
                engine.setProperty("voice", voices[0].id)
            if r1.recognize_google(audio) == "translate to French":
                translator = Translator(to_lang = "French")
                speak("Translate phrase please")
                engine.setProperty("voice", voices[1].id)
                audio = r1.listen(source)
                query = r1.recognize_google(audio)
                translation = translator.translate(query)
                print("You said : " + query)
                print(translation)
                speak(translation)
                engine.setProperty("voice", voices[0].id)
            if r1.recognize_google(audio) == "translate to German":
                translator = Translator(to_lang = "German")
                speak("Translate phrase please")
                engine.setProperty("voice", voices[1].id)
                audio = r1.listen(source)
                query = r1.recognize_google(audio)
                translation = translator.translate(query)
                print("You said : " + query)
                print(translation)
                speak(translation)
                engine.setProperty("voice", voices[0].id)
            if r1.recognize_google(audio) == "translate to Spanish":
                translator = Translator(to_lang = "Spanish")
                speak("Translate phrase please")
                engine.setProperty("voice", voices[1].id)
                audio = r1.listen(source)
                query = r1.recognize_google(audio)
                translation = translator.translate(query)
                print("You said : " + query)
                print(translation)
                speak(translation)
                engine.setProperty("voice", voices[0].id)
            if r1.recognize_google(audio) == "exit":
                input("Press enter to exit.")
                break
            if r1.recognize_google(audio) == "evaluate":
                print("Enter evaluation expression.")
                speak("Enter evaluation expression.")
                evexp = input()
                evalexp = float(eval(evexp))
                print(evalexp)
                speak(evalexp)
            if r1.recognize_google(audio) == "change volume":
                vol = engine.getProperty("volume")
                csx = 1
                while csx == 1:
                    print("Enter new volume.")
                    speak("Enter new volume.")
                    newvol = int(input())
                    engine.setProperty("volume", newvol)
                    speak("Volume testing, Is this volume okay for you?")
                    audio = r1.listen(source)
                    speak = r1.recognize_google(source)
                    if "yes" in speak:
                        csx == 0
                    elif "no" in speak:
                        continue
                    else:
                        speak("Either say yes or no.")
                print("Successfully changed volume!")
            if r1.recognize_google(audio) == "change rate":
                rate = engine.getProperty("rate")
                csx = 1
                while csx == 1:
                    print("Enter new rate.")
                    speak("Enter new rate.")
                    newrate = int(input())
                    engine.setProperty("volume", newrate)
                    speak("Rate testing, Is this rate okay for you?")
                    audio = r1.listen(source)
                    speak = r1.recognize_google(source)
                    if "yes" in speak:
                        csx = 0
                    elif "no" in speak:
                        continue
                    else:
                        speak("Either say yes or no.")
                print("Successfully changed rate!")
            if r1.recognize_google(audio) == "change your voice":
                print("Enter voice number.")
                speak("Enter voice number. 1 for male, and 2 for female. If you have a 3rd voice please enter 3.")
                vnumber = int(input())
                if (vnumber > 0) and (vnumber < 4):
                    vnumber = vnumber - 1
                    defaultvoice = voices[vnumber]
        except sr.UnknownValueError:
            print("Error")
        except sr.RequestError:
            print("Failed Error")
