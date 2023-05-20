import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

mailids = {"ambika" : "amazingamm01@gmail.com"}

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour < 12:
        speak("Good Morning!")
    elif hour >=12 and hour <17:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
     
    speak("I am Aria , Your reliable AI servant. How may I help you today?")

def takeCommand():
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said : {query}\n ")
    except Exception as e:
        print("Can you please say that again")
        return "none"
    return query



def tell_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Did you hear about the mathematician who's afraid of negative numbers? He will stop at nothing to avoid them!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "I'm reading a book about anti-gravity. It's impossible to put down!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
    ]

    joke = random.choice(jokes)
    speak(joke)

def tell_fact():
    facts = [
        "The world's oldest known living tree is named Methuselah and is over 4,800 years old.",
        "Honey never spoils. You can eat honey that's been stored for thousands of years.",
        "The Great Wall of China is visible from space.",
        "The average person walks the equivalent of three times around the world in a lifetime.",
        "The shortest war in history lasted only 38 to 45 minutes.",
    ]

    fact = random.choice(facts)
    speak(fact)
    
def calculate(expression):
    try:
        expression = expression.replace('x', '*') 
        result = eval(expression)
        speak(f"The result of {expression} is {result}")
    except Exception as e:
        speak("Sorry, I couldn't calculate that.")




    
if __name__ =='__main__':
    WishMe()
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query :
            speak(" Fetching your information , kindly wait...")
            query = query.replace('wikipedia' , "")
            results = wikipedia.summary( query, sentences = 3)
            speak(" Here's what i found on wikipedia")
            print(results)
            speak(results)
            speak(" anything else i can do for you?")
        elif 'youtube' in query:
            webbrowser.open("youtube.com")  
            speak(" anything else i can do for you?")
        elif 'google' in query:
            webbrowser.open("google.com")
            speak(" anything else i can do for you?")
        elif 'facebook' in query:
            webbrowser.open("facebook.com")     
            speak(" anything else i can do for you?")
        elif 'twitter' in query:
            webbrowser.open("twitter.com")   
            speak(" anything else i can do for you?")
        elif 'whatsapp' in query:
            webbrowser.open("web.whatsapp.com")     
            speak(" anything else i can do for you?")
        
        elif 'music' in query :
            music_dir = 'C:\\Users\\Ambika Ashapure\\Desktop\\New folder'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))  
            speak(" anything else i can do for you?")
         
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
            speak(" anything else i can do for you?")
            
        elif 'code' in query :
            codePath = "C:\\Users\\Ambika Ashapure\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak(" anything else i can do for you?")
            
        elif 'tell a joke' in query or 'joke' in query:
            tell_joke()
            speak(" anything else i can do for you?")
            
        elif 'tell a fact' in query or 'fact' in query:
            tell_fact()
            speak(" anything else i can do for you?")
            
        elif 'thank you' in query:
            speak("You're welcome, anything else i can do for you?")
            
        elif 'calculate' in query:
            speak("Sure, what expression would you like me to calculate?")
            expression = takeCommand().lower()
            calculate(expression)
            
        elif 'exit' in query or 'quit' or "bye" in query:
            speak("okay, Goodbye!")
            break
        
        
        
            