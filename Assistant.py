import random

import datetime

import speech_recognition as sr
import pyttsx3

import wikipedia
import wolframalpha

import webbrowser
import os

#Wikipedia
#search on google
#open google
#search on youtube
#open youtube
#play music 


#"""Voice (pyttsx3) settings"""
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)
rate= engine.getProperty('rate')
engine.setProperty('rate',130)

#"""Changing Browser to chrome"""
chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome',None, webbrowser.BackgroundBrowser(chrome_path))
search_on_browser=webbrowser.get('chrome')

#pyttsx3
#"""speak function, with argumnet what to speak named audio"""
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#datetime
#"""Wish me according to time on starting of application"""
def wishme():
    '''It will take input from datetime module in form of hour and wishes me according to time'''
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<4:
        speak("Good Mid-Night")

    elif hour>=4 and hour<6:
        speak("Good Dawn")

    elif hour>=6 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<16:
        speak("Good Afternoon")

    elif hour>=16 and hour<20:
        speak("Good Evening")

    else:
        speak("Good Night")

    speak("I am Assistant From Lovish, My name is Anonymous.. hehe. How Can I Help You?")

#speech_recognition as sr
def takeCommand():
    #'''It will takes input from microphone and return inpu in form of string'''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en-in")
        engine.setProperty('rate', 170)
        print(f'you said "{query}"\n')
        speak(f"you said {query}")

    except Exception as e:
        err_speech = " Say That Again"
        print(err_speech)
        speak(err_speech)
        return "None"   #None is just a string // returning a string
    return query


#"""Main Function"""
if __name__== "__main__":
    wishme()
    while True:
        command = takeCommand().lower()
        #-------Lists-----------#
        praise = ["buddy",'friend',"mate","oppo","pal"]
        initials = ["hey","hello","hi"]
        if "who are you" in command:
            if "hi" or "hey" or "hello" in command:
                speak(f"{random.choice(initials)}I am Your Assistant {random.choice(praise)}")
            else:
                speak(f"I am Your Assistant {random.choice(praise)}")

        
        elif "wikipedia" in command:
            try:
                speak("Searching....")
                command = command.replace("wikipedia","")
                # #wikipedia
                wikipedia.set_lang("en")
                print(wikipedia.summary(command, sentences=2))
                a = wikipedia.summary(command, sentences=2)
                # print("\nwikipedia")
                rate = engine.getProperty('rate')
                engine.setProperty('rate', 200)
                speak(a)


            except:
                # wolframaplha
                app_id = "E5TGYA-HQVEYL4LH9"
                client = wolframalpha.Client(app_id)
                out = client.query(command)
                answer = next(out.results).text
                rate = engine.getProperty('rate')
                engine.setProperty('rate', 200)
                print(answer)
                speak(answer)
                print("\nWolframalpha")

        elif 'search' in command :
            try:
                speak("Searching....")
                command = command.replace("search", "")
                command = command.replace("on google","")
                search_on_browser.open(f"https://www.google.com/search?q= {command}")

            except:
                # wolframaplha
                app_id = "E5TGYA-HQVEYL4LH9"
                client = wolframalpha.Client(app_id)
                out = client.query(command)
                answer = next(out.results).text
                rate = engine.getProperty('rate')
                engine.setProperty('rate', 200)
                print(answer)
                speak(answer)
                print("\nWolframalpha")

        elif 'open' in command :
            if 'google' in command:
                speak("Opening...")
                search_on_browser.open("https:\\www.google.com")
            elif 'youtube' in command :
                search_on_browser.open("https:\\www.youtube.com")
                speak("Opening")
        

        elif 'on youtube' in command :
            speak("Playing...")
            command=command.replace("play","")
            command = command.replace("on youtube", "")
            search_on_browser.open(f"https://www.youtube.com/results?search_query={command}",autoraise=True)

        elif 'play music' in command:
            speak("Playing...")
            music_dir= 'G:\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            for i in range(0,len(songs)):
                if '.mp3' in songs[i]:
                    os.startfile(os.path.join(music_dir,songs[i]))
                    break
        elif 'exit' or 'bye' or 'see you soon' in command:
            speak("Thanks For using, Goodbye")
            exit()

        else:
            pass