import speech_recognition as sr
import pyttsx3
import spacy
import pyaudio

# initialize speech recognition

recognizer = sr.Recognizer()


def listen():
    with sr.Microphone() as source:
        print("listening..")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio).lower()
            print(f"You said : {command}")
            return command
        except sr.UnkownValueError as e:
            speak(f"Sorry, I couldn't understand that :{e}")
            return ""
        except sr.RequestError as e:
            print(f"Speech Recognition request failed: {e}")
            return ""


# Natural Language Processing(NLP)
nlp = spacy.load('en_core_web_sm')


def process_command(command):
    doc = nlp(command)

    if "hello" in command:
        return "Hello! i am Jarvis how can i assist you today?"

    if "Good Morning jarvis" in command:
        return "Good Morning Sandy have a great day "

    if "Good After noon jarvis" in command:
        return "Good Afternoon Sandy "
    if "Good night jarvis" in command:
        return "Good night Sandy have a good dreams "
    if "Hey Jarvis" in command:
        return "hello sandy how can help you?"
    else:
        return "how can help you?"


# Text to speech

engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def main():
    print("hello")
    speak("Hello! sandy i am Jarvis how can i assist you today?")

    while True:
        command = listen()

        if "stop" in command:
            speak("Good bye")
            break

        response = process_command(command)
        speak(response)


if __name__ == '__main__':
    main()