import pyttsx3 #pip install pyttsx3
import datetime #pip install datetime
import speech_recognition as sr
import wikipedia #pip install wikipedia
import smtplib 
import webbrowser as wb
import psutil #pip install psutil
import pyjokes #pip install pyjokes
import os
import pyautogui #pip install pyautogui
import random #pip install random
import wolframalpha #pip install wolframalpha
import json 
import requests
from urllib.request import urlopen
import time

#for GUI Interface

#==========================================================================

engine = pyttsx3.init()
wolframalpha_app_id = ""#put your id
#for girl voice
listener = sr.Recognizer()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
#==============


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time_():
    # for 12 hours/for 24 hours formate %I convert to %H
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)


def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)


def wishme():
    speak("Wellcome back Mohammad Forhad sir!")
    time_()
    date_()

    hour = datetime.datetime.now().hour

    if hour >= 6 and hour < 12:
        speak("Good morning sir!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir!")
    elif hour >= 18 and hour < 24:
        speak("Good evening sir!")
    else:
        speak("Good night sir!")

    speak("I am Jarvis. please tell me how can i help you today?")


def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...............")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.............")
        query = r.recognize_google(audio, language="en-US")
        print(query)

    except Exception as e:
        print(e)
        print("Say that again please.............")
        return "None"
    return query


def sendemail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()

    server.login("username@gmail.com", "password")
    server.sendmail("username@gmail.com", to, content)
    server.close()


def screenshot():
    img = pyautogui.screenshot()
    img.save("")#put file location


def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+usage)

    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)

def how():
    ok = TakeCommand().lower()
    if "how" in ok:
        speak("I am fine, Thank you sir, how can i help you?")
        ans = TakeCommand().lower()
            



def joke():
    speak(pyjokes.get_joke())


if __name__ == '__main__':
    wishme()
    how()

    while True:
        query = TakeCommand().lower()

        # for easy recognition

        if "time" in query:  # tell us time when asked
            time_()

        elif "date" in query:  # tell us date when asked
            date_()

        elif "wikipedia" in query:
            speak("Searching..............")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(result)
            speak(result)

           
            


        elif "send email" in query:
            try:
                speak("What should i say?")
                content = TakeCommand()
                # provide reciver email address
                speak("Who is the reciever?")
                reciever = input("Enter reciever's Email : ")

                to = reciever
                sendemail(to, content)
                speak(content)
                speak("Email has been sent.")

            except Exception as e:
                print(e)
                speak("Unable to send email.")


        elif "search in chrome" in query:
            speak("What should i search?")
            chromepath = ""#put path location

            search = TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')  # only open websites with .com domain



        elif "open youtube" in query:
            speak("Here we go to youtube")
            wb.open("https://www.youtube.com/")



        elif "search in youtube" in query:
            speak("What should i search ?")
            search_Term = TakeCommand().lower()
            speak("Here we go to youtube")
            wb.open("https://www.youtube.com/results?search_query="+search_Term)


        elif "search in google" in query:
            speak("What should i search ?")
            search_Term =TakeCommand().lower()
            speak("Searching...............")
            wb.open("https://www.google.com/search?q="+search_Term)


        elif "cpu" in query:
            cpu()

        elif "joke" in query:
            joke()

        elif "go offline" in query:
            speak("Going offline sir!. Allah Hafez")
            quit()

        elif "open word" in query:
            speak("Opening ms word............")
            ms_word = r""#put file location
            os.startfile(ms_word)

        elif "write a note" in query:
            speak("what should i write ? sir!")
            notes = TakeCommand()
            file = open("notes.txt",'w')
            speak("Sir should i include date and Time?")
            ans = TakeCommand()
            if 'yes' in ans or 'sure' in ans:
                strTime = datetime.datetime.now().strftime("%I:%M:%S")
                file.write("~: ")
                file.write(notes)
                speak("Writting Notes are Done, SIR!")
            else:
                file.write(notes)

        elif "show note" in query:
            speak("Showing notes")
            file = open("notes.txt","r")
            print(file.read())
            speak(file.read())
            
        elif "screenshot" in query:
            screenshot()

        elif "play music" in query:
            song_dir = ""#put file location
            music = os.listdir(song_dir)
            speak("What should i play? sir!")
            speak("Select a number..............")
            ans = TakeCommand().lower()
            while("number" not in ans and ans != "random" and ans != "choose you"):
                speak("I could not understand you. please tell me again.")
                ans = TakeCommand().lower()
            if "number" in ans:
                no = int(ans.replace("number",""))
            elif "random" or "choose you" in ans:
                no = random.randint(1, 100)

            os.startfile(os.path.join(song_dir,music[no]))

        elif "calculate" in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            indx = query.lower().split().index("calculate")
            query = query.split()[indx + 1:]
            res = client.query("".join(query))
            answer = next(res.results).text
            print("The answer is : "+answer)
            speak("The answer is : "+answer) 

        elif "what is" in query or "who is" in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak((next(res.results).text))
            except StopIteration:
                print("No Results")


        elif "remember that" in query:
            speak("What should i remember?")
            memory = TakeCommand()
            speak("You asked me to remember that"+memory)
            remember = open("memory.txt","w")
            remember.write(memory)
            remember.close()
        
        elif "do you remember anything" in query:
            remember = open("memory.txt","r")
            speak("You asked me to remember that"+remember.read())
        

        elif "where is" in query:
            query = query.replace("where is","")
            location = query
            speak("User asked to locate"+location)
            wb.open_new_tab("https://www.google.com/maps/place/"+location)
        
        elif "news" in query:
            try:
                jsonObj = urlopen("http://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=65d96e277a684dc18b684b19f9df2f0e")
                data = json.load(jsonObj)
                i = 1

                speak("Here are some top Headlines from the Entertainment Industry")
                print("=======================TOP HEADLINES==================="+"\n")
                for item in data["articles"]:
                    print(str(i)+". "+item["title"]+"\n")
                    print(item["description"]+"\n")
                    speak(item["title"])
                    i += 1

            except Exception as e:
                print(str(e))

        elif "stop listening" in query:
            speak("How many Secounds you want me to stop listening, sir!")
            ans = float(TakeCommand())
            time.sleep(ans)
            print(ans)

        elif "log out" in query:
            os.system("shutdown -l")


            
          
