# Title :- AI Voice assistant project.
# Description :- This is the clone that work as a Jarvis AI in iron man movie. In reality, the concept of Jarvis AI has been implemented in a number of forms, including software applications and voice-activated virtual assistants. These systems are designed to assist users with tasks such as setting reminders, providing information, controlling smart home devices, and more.

'''This are some command that are implemented by this project :-

    1. While run - Wish the user according to time.
    2. jarvis tell srk according to wikipedia - search anything in wikipedia.
    3. jarvis open youtube - AI run the youtube for user.
    4. jarvis open google - AI run the google chrome for user.
    5. jarvis open stackoverflow  - open stackoverflow website for user.
    6. jarvis play music - play the music that are store in a user pc.
    7. jarvis what time it is - tell the current time based on world clock.
    8. jarvis open python - open pycharm in pc if pycharm is already installed in system.
    9. jarvis open notepad - open notepad for user.
    10. jarvis open blue - open bluestack website for user.
    11. jarvis send mail - They will send an email to whoever you want.
    12. jarvis shutdown yourself - They switch off himself.'''

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5') #--> It is pre build windows api that provide voice.
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)#--> [0] = DAVID / [1] = ZIRA

def speak(audio): #--> This method is use to speak jarvis whatever we want to talk.
    engine.say(audio)
    engine.runAndWait()

def wishMe(): #--> This method wish users based on time.
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir...")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir...")
    else:
        speak("Good Evening Sir...")

    speak("I Am Jarvis. How May I Help You Sir...")

def takecommand():#--> it takes microphone input from user and return a string output.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 #--> It is a Timegap Between 2 Word While Speaking.
        audio = r.listen(source)
        try :
            print("Recognizing...")
            query = r.recognize_google(audio,language='en-in')
            print(f"User Said : {query}\n")
        except Exception as e:
            print("Say That Again Please...")
            return "None"
        return query

def sendEmail(to,content): #--> use to send mail to our choice.
    server = smtplib.SMTP('smtp.gmail.com',587) # smtplib module use to send mail on local host.
    server.ehlo()
    server.starttls()
    server.login('youremail@example.gmail.com','your-password')
    server.sendmail('youremail@example.gmail.com',to,content)
    server.close()

if __name__ == '__main__': #--> this is the main method that execute jarvis AI.
    wishMe()
    while True:
        query = takecommand().lower()
        #--> Logic that execute task based on query.
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            speak("According To Wikipedia")
            print(result)
            speak(result)

        elif 'open youtube' in query:
            speak("Opening Youtube...")
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            speak("Opening Google...")
            webbrowser.open('google.com')

        elif 'open stackoverflow' in query:
            speak("Opening Stackoverflow...")
            webbrowser.open('stackeoverflow.com')

        elif 'play music' in query:
            speak("Playing Music...")
            music_dir = 'D:\\Python\\Projects\\Jarvis\\Musics'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[1]))

        elif 'the time' in query:
            strtime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,The Time Is : {strtime}")

        elif 'open python' in query:
            speak("Opening Pycharm...")
            pathpy = 'C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.1.3\\bin\\pycharm64.exe'
            os.startfile(pathpy)

        elif 'open notepad' in query:
            speak("Opening Notepad...")
            pathpy = 'C:\\Program Files\\Notepad++\\notepad++.exe'
            os.startfile(pathpy)

        elif 'open blue' in query:
            speak("Opening Bluestack...")
            pathbs = 'C:\\Program Files\\BlueStacks_nxt\\HD-Player.exe'
            os.startfile(pathbs)

        elif 'send email' in query:
            try:
                speak("What should I Write??")
                content =takecommand()
                to = 'reciveremail@example.gmail.com'
                sendEmail(to,content)
                speak("Email Has Been Sent!")

            except Exception as e:
                print(e)
                speak("Sorry!! I am not able to send email right now.")

        elif 'shutdown' in query:
            speak("AI Shutdown Process Executed...")
            break