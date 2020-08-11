import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import datetime
from PIL import Image , ImageGrab

engine = pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening")
        r.pause_threshold=1
        audio =r.listen(source)
        try:
            query = r.recognize_google(audio,language="en-in")
        except Exception as e:
            print(e)
            # speak("soory i got exception")
            return "None"
        return query

    
# to send mail but generating a error that wrong username or password
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('dy43204@gmail.com', '9981395685')
    server.sendmail('dy34204@gmail.com', to, content)
    server.close()



def wish():
    hr =datetime.datetime.now().hour
    if hr>=0 and hr<12:
        audio = "Good morning sir"
    elif hr>=12 and hr<18:
        audio = "Good afternoon sir"
    else:
        audio = "Good evening sir"
    speak(audio)



if __name__=="__main__":
    wish()
    while True:
        query = takeCommand().lower()
        if "wikipedia" in query:
            print("searching query")
            query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=4)
            speak("According to wikipediia")
            print(results)
            speak(results)

        elif "google" in query:
            webbrowser.open("https://www.google.com/")

        elif "youtube" in query:
            webbrowser.open("https://www.youtube.com")

        # elif "game" in query:
        #     os.startfile("E:\\crack")

        elif "time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strtime)
            speak(f"time is {strtime}")
        elif "screenshot" in query:
            image = ImageGrab.grab()
            data = image.load()
            image.show()
        # to be done
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "deepak4d4@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")
        elif "quit" or "exit" in query:
            exit()
