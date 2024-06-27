import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia as wiki
import smtplib as smtp
import webbrowser as wb
import os
from PIL import Image, ImageGrab
import psutil


engine = pyttsx3.init('sapi5') 

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

def screenshot():
    img = ImageGrab.grab()
    img.save('C:\\Users\\abcd\\OneDrive\\Pictures\\Screenshots\\AI-Assistant') #Test Path
    
def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is presently at' + usage)
    battery = psutil.sensors_battery()
    speak('Power level is presently at')
    speak(battery.percent)
    
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
                speak(content) #Use in testing
                #speak("Email has been sent!")
                
            except Exception as e:
                print(e)
                speak("Unable to send email")
                
        elif 'google search' in query:
            speak("What would you like me to search?")
            search_query = voiceCommand().lower()
            try:
                url = f"https://www.google.com/search?q={search_query}"
                wb.open(url)
                speak(f"Here are the search results for {search_query}")
            except Exception as e:
                print(e)
                speak("An error occurred while trying to search Google.")
                
        elif 'logout'in query:
            os.system("shutdown -l")
            
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
            
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
            
        elif 'play song' in query:
            songs_dir = 'D:\\Music'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))
            
        elif 'please take note' in query:
            speak("sure thing. I'm listening...")
            data = voiceCommand()
            speak('Ok. Just to confirm. You said' + data + 'Is that correct?')
            confirmation = voiceCommand().lower()
            if 'yes' in confirmation:
                with open('data.txt', 'w') as note:
                    note.write(data)
                speak("Note saved successfully.")  
                note.close()
            else:
                speak("Alright, let's try that again.")           

        elif 'read back notes' in query:
            try:
                with open('data.txt', 'r') as note:
                     content = note.read()
                if content:
                    speak("Sure thing. Here are your notes: " + content)
                else:
                    speak("The note file is empty.")
            except FileNotFoundError:
                speak("I'm sorry, but I couldn't find any saved notes.")
            except Exception as e:
                speak("An error occurred while trying to read the notes.")
                print(f"Error: {e}")   
                     
        elif 'screenshot' in query:
            screenshot()
            speak("Done!")
            
        elif 'cpu' in query:
            cpu()
            
        elif 'exit' in query or "thank you" in query:
            quit()
            
