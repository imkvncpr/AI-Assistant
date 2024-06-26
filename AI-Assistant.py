import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio as pya


engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
speak("This is the AI assistant")


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

time()

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak(day)
    speak(month)
    speak(year)
date()


def greeting():
    speak("Greetings")
    speak("The present time is")
    time()
    speak("Todays date is currently")
    date()
    hour = datetime.datetime.now().hour
    if hour >=6 and hour <12:
        speak("Good Morning")
    elif hour >=12 and hour <18:
        speak("Good Afternoon")
    elif hour >=18 and hour <24:
        speak("Good Evening")
    else:
        speak("Good Night")
        
    speak("I am here to assist")
    
greeting()


def voiceCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pauseThreshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        print(query)
           
    except Exception as e:
        print(e)
        speak("I did not understand. Can you please repeat?")
        
        return("none")
    return(query)

voiceCommand()