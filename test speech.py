# coding=<UTF-8>

import pyttsx3

from pyttsx3 import voice

import wikipedia

import datetime

import speech_recognition as sr

import webbrowser

import os

import random

import smtplib

engine = pyttsx3.init()

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

engine.setProperty('rate', 145)

def speak(audio):
 engine.say(audio)

 engine.runAndWait()


def wishMe():
 hour = int(datetime.datetime.now().hour)

 if hour >= 0 and hour < 12:

  speak("Good Morning! Divik.")

 elif hour >= 12 and hour < 18:

  speak("Good Afternoon! Divik.")

 else:

  speak("Good Evening Divik")

  speak("I'm JARVIS Sir. Please let me know how can i assist you?")

def takeCommand():

 r = sr.Recognizer()

 with sr.Microphone() as source:

  print("Listening....")

  r.pause_threshold = 1

  audio = r.listen(source)

 try:

  print("Recognizing....")

  query = r.recognize_google(audio, language="en_us")
  # query = r.recognize_google_cloud(audio, "language = en_us")

  print(f"user Said : {query}\n")

 except Exception as e:

  print("Say that again Please...")
  print(e)

  speak("Say that again Please")

  return 'None'

 return query

def sendEmail(to, content):

 server = smtplib.SMTP(' smtp.gmail.com', 587)

 server.ehlo()

 server.starttls()

 server.login('divik1113@gmail.com', 'passwd')

 server.send_message('divik1113@gmail.com',to ,content)

 server.close()


if __name__ == "__main__":

 #while True:

 if True:

  query = takeCommand().lower()

  if 'wikipedia' in query:

   speak("Searching Wikipedia...")

   query = query.replace("wikipedia", "" )

   result = wikipedia.summary(query, sentences=3)

   speak("According to Wikipedia")

   print(result)

   speak(result)

  elif 'open youtube' in query:

   speak("Opening... Just a moment")

   a_website = "https://www.youtube.com"
   webbrowser.open_new(a_website)

   speak("Opened")

  elif 'open google' in query:

   speak("Opening... Just a moment")

   a_website = "https://www.google.com"
   webbrowser.open_new(a_website)

   speak("Opened")

  elif 'open facebook' in query:

   speak("Opening... Just a moment")
   #
   a_website = "https://facebook.com\ItsDivik"
   webbrowser.open_new(a_website)

   speak("Opened")

  elif 'open instagram' in query:

   speak("Opening... Just a moment")

   a_website = "https://instagram.com/ItsDivik"
   webbrowser.open_new(a_website)

   speak("Opened")

  elif 'open stackoverflow' in query:

   speak("Opening... Just a moment")

   a_website = "https://stackoverflow.com"
   webbrowser.open_new(a_website)

   speak("Opened")

  elif 'open website' in query:

   speak("Opening... Just a moment")

   a_website = "https://www.invacialabs.com"
   webbrowser.open_new(a_website)

   speak("Opened")

  elif 'play music' in query:

   music_dir = "E:\Music"

   songs = os.listdir(music_dir)

   random_gen = random.randint(0 , len(songs) - 1)

   os.startfile(os.path.join(music_dir, songs[random_gen]))

  elif 'the time' in query:

   strTime = datetime.datetime.now().strftime("%H, %M, %S")

   speak(f"Sir, The time is {strTime}" )

   print(f"Time -{strTime}\n")

  elif 'send email' in query:

   try:

    speak("To whom you wanna send Sir? kindly enter a email")

    to = input("Kindly Enter email : ")

    speak("what should i write?")

    content = takeCommand()

    sendEmail(to, content)

    speak("Email has been sent!")

   except Exception as e:

    speak("sorry Divik! I'm not able to send the mail. Please Try again")

   print("Please try again...")

  elif 'exit':

   speak('SIGNING OFF')

   exit

#DIVIK DWIVEDI