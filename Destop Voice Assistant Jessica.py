import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import requests
import wolframalpha
import pyjokes
import requests
import subprocess
import warnings
import calendar
import random
import datefinder
import cv2
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jessica Maam . Please tell me how may I help you")       

def takeCommand():


    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Your Email', 'Password')
    server.sendmail('Your Email', to, content)
    server.close()
app = wolframalpha.Client("Number")
def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":","-")+"-note.txt"
    with open(file_name,"w") as f:
        f.write(text)
    subprocess.Popen(["notepad.exe" ,file_name])


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'Location'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Maam, the time is {strTime}")

           
        elif 'email to Gita' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "Gita@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry . I am not able to send this email")    
        elif 'email to Riya' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "Riya@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry . I am not able to send this email") 
        elif 'email to Kunal' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "Kunal@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry . I am not able to send this email")   
        elif 'email to Ram' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "Ram@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry . I am not able to send this email")
        elif 'temperature' in query:
            res = app.query(query) 
            speak(next(res.results).text)


        elif 'who are you' in query:
            speak (" I am Jessica.. your assistant.")
            speak("how may i help you")
        elif 'how are you' in query: 
            speak("I am fine, Thank you") 
            speak("How are you Maam") 
        elif 'fine' in query or "great" in query: 
            speak("It's good to know that your fine") 
        elif 'stop' in query: 
            speak("Thanks for giving me your time") 
            exit()
    
        elif "who made you" in query or "who created you" in query:  
            speak("I have been created by a Homo Sapien.")      


        elif 'tell me a joke' in query:
            speak(pyjokes.get_joke())
        
        elif 'calculate' in query: 
            speak("What should I calculate.") 
            gh = takeCommand().lower()
            res = app.query(gh)
            speak(next(res.results).text)
        
        elif 'make a note' in query:  
            speak(f"What would you like me to write down")
            note_text = takeCommand().lower()
            note(note_text)
            speak("I've made a note of that")
        
    