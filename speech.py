import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS
import os

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak in English...")
    audio = recognizer.listen(source)

try:
    # Speech to text
    text = recognizer.recognize_google(audio)
    print("You said:", text)

    # Translate English to Kannada
    translated = GoogleTranslator(source='en', target='kn').translate(text)
    print("Kannada Translation:", translated)

    # Text to speech (Kannada)
    tts = gTTS(text=translated, lang='kn')
    filename = "output.mp3"
    tts.save(filename)

    # Play audio using Windows default player
    os.startfile(filename)

except Exception as e:
    print("Error:", e)