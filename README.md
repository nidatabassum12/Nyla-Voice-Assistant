# 🎙️ Nyla – AI Voice Assistant

## 📌 Project Overview

Nyla is a Python-based AI Voice Assistant that listens to voice commands and performs various tasks such as opening websites, searching Google, providing weather updates, answering general knowledge questions, sending emails, setting reminders, opening desktop applications, and more.

The assistant uses Speech Recognition for voice input and Text-to-Speech to communicate naturally with the user.

---

# 🚀 Features

### Beginner Features

- 🎤 Voice recognition using SpeechRecognition
- 👋 Greets the user
- 🕒 Tells current time
- 📅 Tells current date
- 🔍 Performs Google search
- 🌐 Opens Google
- ▶️ Opens YouTube
- 🤖 Opens ChatGPT
- 🔊 Voice responses for every command
- ⚠️ Graceful error handling for speech recognition

---

### Advanced Features

- 🌦️ Live Weather Updates using OpenWeatherMap API
- 📧 Send Email using Gmail SMTP
- ⏰ Set Reminders
- 📚 Wikipedia-based General Knowledge
- 🤖 AI Chat using OpenAI API
- 🧠 Basic Natural Language Understanding
- 💻 Open Notepad
- 🧮 Open Calculator
- 🎨 Open Paint
- 📂 Open File Explorer
- 📸 Take Screenshots
- ➗ Voice Calculator
- 😂 Tell Jokes
- 📝 Add Custom Commands using `commands.json`

---

# 🛠 Technologies Used

- Python 3.x
- SpeechRecognition
- Edge-TTS
- Pygame
- Requests
- OpenAI API
- OpenWeatherMap API
- SMTP (Gmail)
- PyAutoGUI
- PyJokes

---

# 📦 Required Libraries

Install all required libraries using:

```bash
pip install SpeechRecognition
pip install edge-tts
pip install pygame
pip install requests
pip install pyautogui
pip install pyjokes
pip install openai
pip install pyaudio
```

---

# ▶️ How to Run

1. Install Python 3.x
2. Install all required libraries.
3. Add your API keys:

- OpenWeatherMap API Key
- OpenAI API Key
- Gmail App Password

4. Run the project:

```bash
python main.py
```

5. Speak your command when prompted.

---

# 🗣 Example Voice Commands

### Greetings

- Hello
- Hi

### Time & Date

- What is the time?
- Tell me today's date.

### Web

- Open Google
- Open YouTube
- Open ChatGPT
- Search Python tutorials

### Weather

- Weather in Hyderabad
- Tell me the weather in Delhi

### General Knowledge

- Who is Virat Kohli?
- What is Artificial Intelligence?

### AI Chat

- Ask What is Machine Learning?

### Email

- Send Email

### Reminder

- Set Reminder

### Applications

- Open Calculator
- Open Notepad
- Open Paint
- Open File Explorer

### Screenshot

- Take Screenshot

### Calculator

- Calculate 15 plus 25

### Custom Commands

- Add Custom Command

---

# 📂 Project Structure

```
VoiceAssistant/
│
├── main.py
├── commands.json
├── README.md
└── requirements.txt
```

---

# 🔒 Privacy Considerations

- Voice commands are processed only while the application is running.
- Voice recordings are not stored permanently.
- Internet access is required for:
  - Google Search
  - Weather Updates
  - Wikipedia Search
  - AI Chat
  - Email Sending
- API keys and Gmail App Password should be kept private and should never be shared publicly.
- No personal data is stored by the application unless explicitly configured by the user.

---

# 🔮 Future Enhancements

- Voice-based email recipient and message input
- Voice authentication
- Smart Home Device Integration
- Music Playback
- Calendar Integration
- Face Recognition
- WhatsApp Messaging
- Alarm System
- Multi-language Support

---

# 👩‍💻 Developed By

**Nida Tabassum**

Python Voice Assistant Project
