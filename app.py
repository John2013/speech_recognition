import sys
import webbrowser

import pyttsx3
import speech_recognition as sr


def talk(words):
    print(f"talk: {words}")

    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()


def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("говорите")
        r.pause_threshold = .5
        r.adjust_for_ambient_noise(source=source, duration=1)
        audio = r.listen(source=source)
        print("записано")

    try:
        command = r.recognize_google(audio, language="ru-RU").lower()
        print(f"talked: {command}")
    except sr.UnknownValueError:
        talk("Я вас не поняла")
        command = listen_command()

    return command


def run_command(command):
    if 'открой сайт' in command:
        talk('открываю')
        url = "https://ya.ru"
        webbrowser.open(url)
    elif 'стоп' in command:
        talk("досвидания")
        sys.exit()


if __name__ == '__main__':
    talk("Привет, спроси что-нибудь")
    while True:
        run_command(listen_command())
