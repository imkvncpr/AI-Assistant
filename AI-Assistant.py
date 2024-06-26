import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia as wiki
import smtplib as smtp


engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
#speak("This is the AI assistant")


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The present time is")
    speak(Time)

#time()

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("Todays date is currently")
    speak(day)
    speak(month)
    speak(year)
    
#date()


def greeting():
    speak("Greetings")
    time()
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
    
#greeting()


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

def sendEmail(to, content):
    server = smtp.SMTP('smtp.outlook.com', 587)
    server.ehlo
    server.starttls()
    server.login('abcd@outlook.com', 'ai-assit1!')
    server.sendmail('abcd@outlook.com', to, content)
    server.close()

#voiceCommand()

if __name__ == "__main__":
    greeting()
    while True:
        query = voiceCommand().lower()
        
        if 'time' in query:
            time()
            
        elif 'date' in query:
            date()
            
        elif 'wiki' in query:
            speak("searching")
            query = query.replace("wiki", "")
            result = wiki.summary(query, sentences=2)
            print(result)
            speak(result)
            
        elif 'send email' in query:
            try:
                speak('What should it say?')
                content = voiceCommand()
                to = 'xyx@gmail.com'
                #sendEmail(to, content)
                speak(content)
                #speak("Email has been sent!")
                
                
            except Exception as e:
                print(e)
                speak("Unable to send email")
        elif 'exit' in query or "thank you" in query:
            quit()
            
