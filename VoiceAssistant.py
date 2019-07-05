#import modules

import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser


engine=pyttsx3.init('sapi5')   #for voice engine
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)   #selecting installed voice from your computer ( you can check and change property from 0 to 1 or so on)

def speak(audio):   #speak function
    engine.say(audio)
    engine.runAndWait()

def start():       #function that will start with
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am your Voice Assistant. How may I help you?")

def commands():    #speech to text.
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')   #it can be change acc. to you from google to bing or google_cloud
        print("You said : {}".format(query))
    except Exception as e:
        print("Please try again...")
        return "None"
    return query


if __name__ == "__main__":   #main function
    start()
    while True:
        query=commands().lower()
        if 'the time' in query:
             StrTim=datetime.datetime.now().strftime("%H:%M:%S")
             speak(f"The time is {StrTim}")
            
        elif 'play music' in query:
            music_dir = 'E:\\Mp3\\songs mp3\\audios'  #select your library of music
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com") 

        elif 'goodbye' in query:
            break

            #you can add more queries as you want.


        
