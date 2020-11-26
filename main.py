import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import googlesearch
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<14:
        speak("Good Afternoon")
    else:
        speak('Good Evening')
    speak('I am Zira Mam. Please tell me how may I help you')
def respond():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio =r.listen(source)
    try:
        print('Recognizing....')
        query = r.recognize_google(audio, language='en-GB')
        print("User said: ", query)
    except Exception as e:
        print("Say that again please......")
        return "none"
    return query
if __name__ == '__main__':
    wishMe()
    while True:
        query = respond().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia.....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak("According to Wikipedia...")
            print(results)
            speak(results)
        elif 'search' in query:
            query= query.replace('search', "")
            speak("According to Google")
            link = "www.google.com/search?q=" + query
            webbrowser.open(link)
        elif 'exit' in query:
            speak("Thank You Mam for spending your time with me")
            exit()


