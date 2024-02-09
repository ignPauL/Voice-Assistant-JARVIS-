import pyttsx3
import speech_recognition as sr 
import webbrowser
import datetime
import pyjokes
import os
import time

def spText():   #Speech to Text convert function
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source) #Noise Cancellation
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print (data)
            return data
        

        except sr.UnknownValueError:
            print("Unable to understand") 


def TextSp(x):   # Text to Speech conversion
    engine = pyttsx3.init()
    voice = engine.getProperty("voices")
    engine.setProperty("voice", voice[0].id) # here 0 means male voice and 1 means female voice
    rate = engine.getProperty('rate')
    engine.setProperty("rate", 130) # rate means the voice speed
    engine.say(x)
    engine.runAndWait()

if __name__ == "__main__":

            if "hey jarvis" in spText().lower():
                while True:
                    data1= spText();

                    if "your name" in data1:
                        name = "My name is Jarvis"
                        TextSp(name)

                    elif "is the time" in data1:
                        
                        time = datetime.datetime.now().strftime("%I%M%p")
                        TextSp(time)
                                                                
                    elif "open Google" in data1:
                        webbrowser.open("http://www.google.com")
                        
                    elif "Youtube" in data1:
                        webbrowser.open("https://www.youtube.com")

                    elif "joke" in data1:
                        joke_1 = pyjokes.get_joke(language="en",category="neutral")
                        print(joke_1)
                        TextSp(joke_1)

                    elif "play song" in data1:
                        address = "D:\song"
                        listsong = os.listdir(address)
                        print(listsong)
                        os.startfile(os.path.join(address,listsong[0]))
                    
                    elif "exit" in data1 :
                        TextSp("Thank you for having me ")
                        break

                    time.sleep(8)
            else:
                print("This is not my name. If you want to call me say hello jarvis!")
                exitsp = "This is not my name. If you want to call me say Hello Jarvis!"
                TextSp(exitsp)

