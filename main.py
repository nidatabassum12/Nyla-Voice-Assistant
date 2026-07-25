# ==========================================
# IMPORT LIBRARIES
# ==========================================

import speech_recognition as sr
import asyncio
import edge_tts
import pygame
import os
import datetime
import webbrowser
import pyjokes
import time
import requests
import subprocess
import pyautogui
import json
import smtplib

from email.message import EmailMessage
from openai import OpenAI


# ==========================================
# API KEYS
# ==========================================

WEATHER_API_KEY = "47db8366d859ef794200cebe48159112"


EMAIL_ADDRESS = "nidatabassum403@gmail.com"

EMAIL_PASSWORD = "ptla hbod nwpd umkj"





# ==========================================
# TEXT TO SPEECH
# ==========================================

async def speak_async(text):

    print("Assistant:", text)

    communicate = edge_tts.Communicate(
        text=text,
        voice="en-US-JennyNeural"
    )

    await communicate.save("voice.mp3")


def speak(text):

    asyncio.run(speak_async(text))

    pygame.mixer.init()

    pygame.mixer.music.load("voice.mp3")

    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue

    pygame.mixer.quit()

    if os.path.exists("voice.mp3"):
        os.remove("voice.mp3")


# ==========================================
# SPEECH RECOGNITION
# ==========================================

recognizer = sr.Recognizer()

speak("I'm Nyla, your voice assistant. Ready to assist.")
# ==========================================
# WEATHER
# ==========================================

def get_weather(city):

    url = (
        f"https://api.openweathermap.org/data/2.5/weather?"
        f"q={city}&appid={WEATHER_API_KEY}&units=metric"
    )

    try:

        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()

            temperature = data["main"]["temp"]

            description = data["weather"][0]["description"]

            return (
                f"The temperature in {city} is "
                f"{temperature} degree Celsius with {description}."
            )

        elif response.status_code == 401:

            return "Weather API key is invalid or not active."

        else:

            return "Sorry, I couldn't find that city."

    except Exception:

        return "Unable to connect to weather service."




# ==========================================
# WIKIPEDIA
# ==========================================

def search_wikipedia(query):

    try:

        search_url = (
            "https://en.wikipedia.org/w/api.php"
            "?action=opensearch"
            f"&search={query}"
            "&limit=1"
            "&namespace=0"
            "&format=json"
        )

        headers = {

            "User-Agent": "NylaVoiceAssistant/1.0"

        }

        search_response = requests.get(search_url, headers=headers)

        results = search_response.json()

        if len(results[1]) == 0:

            return "Sorry, I couldn't find any information."

        page_title = results[1][0]

        summary_url = (
            f"https://en.wikipedia.org/api/rest_v1/page/summary/"
            f"{page_title.replace(' ', '_')}"
        )

        summary_response = requests.get(summary_url, headers=headers)

        if summary_response.status_code == 200:

            data = summary_response.json()

            summary = data.get("extract", "")

            if summary:

                sentences = summary.split(". ")

                return ". ".join(sentences[:2])

        return "Sorry, I couldn't find any information."

    except Exception as e:

        print("Wikipedia Error:", e)

        return "Unable to connect to Wikipedia."


# ==========================================
# CALCULATOR
# ==========================================

def calculate(expression):

    expression = expression.replace("plus", "+")

    expression = expression.replace("minus", "-")

    expression = expression.replace("times", "*")

    expression = expression.replace("multiplied by", "*")

    expression = expression.replace("x", "*")

    expression = expression.replace("divided by", "/")

    try:

        result = eval(expression)

        return f"The answer is {result}"

    except:

        return "Sorry, I couldn't calculate that."


# ==========================================
# SCREENSHOT
# ==========================================

def take_screenshot():

    try:

        filename = datetime.datetime.now().strftime("Screenshot_%Y%m%d_%H%M%S.png")

        screenshot = pyautogui.screenshot()

        screenshot.save(filename)

        return f"Screenshot saved as {filename}"

    except Exception as e:

        print(e)

        return "Sorry, I couldn't take the screenshot."


# ==========================================
# EMAIL
# ==========================================

def send_email(receiver, subject, message):

    try:

        email = EmailMessage()

        email["From"] = EMAIL_ADDRESS

        email["To"] = receiver

        email["Subject"] = subject

        email.set_content(message)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

            smtp.send_message(email)

        return "Email sent successfully."

    except Exception as e:

        print(e)

        return "Sorry, I couldn't send the email."


# ==========================================
# REMINDER
# ==========================================

def set_reminder(seconds, reminder_text):

    speak(f"Okay! I will remind you in {seconds} seconds.")

    time.sleep(seconds)

    speak(reminder_text)


# ==========================================
# CUSTOM COMMANDS
# ==========================================

try:
    with open("commands.json", "r") as file:
        custom_commands = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    custom_commands = {}


# ==========================================
# TAKE COMMAND
# ==========================================

def take_command():

    try:

        with sr.Microphone() as source:

            recognizer.adjust_for_ambient_noise(source, duration=0.5)

            print("Listening...")

            audio = recognizer.listen(source)

        command = recognizer.recognize_google(audio).lower()

        print("You said:", command)

        return command

    except sr.UnknownValueError:

        speak("Sorry, I couldn't understand. Please repeat.")

        return ""

    except sr.RequestError:

        speak("Please check your internet connection.")

        return ""

    except Exception as e:

        print(e)

        return ""
# ==========================================
# MAIN PROGRAM
# ==========================================

while True:

    text = take_command()

    if text == "":
        continue

    # ======================================
    # Greeting
    # ======================================

    if (
        "hello" in text
        or "hi" in text
        or "hey" in text
    ):

        speak("Hello! How can I help you?")

    # ======================================
    # Time
    # ======================================

    elif (
        "time" in text
        or "current time" in text
        or "what time is it" in text
    ):

        current_time = datetime.datetime.now().strftime("%I:%M %p")

        speak(f"The current time is {current_time}")

    # ======================================
    # Date
    # ======================================

    elif (
        "date" in text
        or "today's date" in text
        or "what is the date" in text
        or "today" in text
    ):

        current_date = datetime.datetime.now().strftime("%d %B %Y")

        speak(f"Today's date is {current_date}")

    # ======================================
    # Google
    # ======================================

    elif (
        "open google" in text
        or "launch google" in text
        or "start google" in text
    ):

        speak("Opening Google")

        webbrowser.open("https://www.google.com")

    # ======================================
    # YouTube
    # ======================================

    elif (
        "open youtube" in text
        or "launch youtube" in text
        or "start youtube" in text
    ):

        speak("Opening YouTube")

        webbrowser.open("https://www.youtube.com")

    # ======================================
    # ChatGPT
    # ======================================

    elif (
        "open chat gpt" in text
        or "open chat g p t" in text
        or "chatgpt" in text
    ):

        speak("Opening ChatGPT")

        webbrowser.open("https://chatgpt.com")

    # ======================================
    # Google Search
    # ======================================

    elif (
        "search" in text
        or "google" in text
    ):

        query = text.replace("search", "")
        query = query.replace("google", "")
        query = query.strip()

        if query == "":

            speak("What would you like me to search?")

        else:

            speak(f"Searching for {query}")

            webbrowser.open(
                "https://www.google.com/search?q=" + query
            )

    # ======================================
    # Joke
    # ======================================

    elif (
        "joke" in text
        or "make me laugh" in text
    ):

        speak(pyjokes.get_joke())

    # ======================================
    # Weather
    # ======================================

    elif "weather" in text:

        city = (
            text.replace("weather", "")
            .replace("in", "")
            .replace("of", "")
            .strip()
        )

        if city == "":

            speak("Please tell me the city name.")

        else:

            speak(get_weather(city))

    # ======================================
    # Wikipedia
    # ======================================

    elif (
        "who is" in text
        or "what is" in text
    ):

        topic = (
            text.replace("who is", "")
            .replace("what is", "")
            .strip()
        )

        if topic == "":

            speak("Please tell me what you want to know.")

        else:

            speak("Searching Wikipedia")

            speak(search_wikipedia(topic))
            # ======================================
    # Calculator
    # ======================================

    elif "calculate" in text:

        expression = text.replace("calculate", "").strip()

        if expression == "":

            speak("Please tell me what to calculate.")

        else:

            speak(calculate(expression))

    # ======================================
    # Screenshot
    # ======================================

    elif (
        "take screenshot" in text
        or "capture screen" in text
        or "screenshot" in text
    ):

        speak("Taking screenshot")

        speak(take_screenshot())

    
    # ======================================
    # Notepad
    # ======================================

    elif (
        "open notepad" in text
        or "launch notepad" in text
        or "start notepad" in text
    ):

        speak("Opening Notepad")

        subprocess.Popen("notepad.exe")

    # ======================================
    # Calculator App
    # ======================================

    elif (
        "open calculator" in text
        or "launch calculator" in text
        or "start calculator" in text
    ):

        speak("Opening Calculator")

        subprocess.Popen("calc.exe")

    # ======================================
    # Paint
    # ======================================

    elif (
        "open paint" in text
        or "launch paint" in text
        or "start paint" in text
    ):

        speak("Opening Paint")

        subprocess.Popen("mspaint.exe")

    # ======================================
    # File Explorer
    # ======================================

    elif (
        "open file explorer" in text
        or "open explorer" in text
        or "launch explorer" in text
    ):

        speak("Opening File Explorer")

        subprocess.Popen("explorer.exe")

    # ======================================
    # Email
    # ======================================

    elif "send email" in text:

        receiver = "23311a6930@iot.sreenidhi.edu.in"

        subject = "Voice Assistant"

        message = "This email was sent using my Python Voice Assistant."

        speak("Sending email.")

        speak(send_email(receiver, subject, message))

    # ======================================
    # Reminder
    # ======================================

    elif (
        "set reminder" in text
        or "remind me" in text
    ):

        speak("After how many seconds?")

        try:

            seconds = int(input("Enter seconds: "))

        except ValueError:

            speak("Please enter a valid number.")

            continue

        speak("What should I remind you about?")

        reminder = input("Reminder: ")

        set_reminder(seconds, reminder)

    # ======================================
    # Add Custom Command
    # ======================================

    elif "add custom command" in text:

        speak("What is the command?")

        command = take_command()

        if command == "":

            continue

        speak("What should I reply?")

        response = take_command()

        if response == "":

            continue

            save_custom_command(command.lower(), response)

        speak("Custom command saved successfully.")

    # ======================================
    # Run Custom Commands
    # ======================================

    elif any(command in text for command in custom_commands):

        for command, response in custom_commands.items():

            if command in text:

                speak(response)

                break

    # ======================================
    # Exit
    # ======================================

    elif (
        "exit" in text
        or "bye" in text
        or "goodbye" in text
        or "stop" in text
    ):

        speak("Bye! Have a wonderful day.")

        break

    # ======================================
    # Unknown Command
    # ======================================

    else:

        speak("Sorry, I didn't understand that command.")