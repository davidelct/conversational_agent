import speech_recognition as sr
import pyttsx3

#initialize speech
engine = pyttsx3.init()
def communicate(question):
    #open microphone and obtaining audio

    engine.say(question)
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    #recognize what you said and convert it to text
    try:
        return(r.recognize_google(audio))
        
        #errors responses 
    except sr.UnknownValueError:
        communicate("Sorry I didn't understand that, can you repeat what you said?")
    except sr.RequestError as e:
        communicate("Sorry I didn't understand that, can you repeat what you said?")

    
