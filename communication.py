import speech_recognition as sr
import pyttsx3

#initialize speech
def ask(question):
    #open microphone and obtaining audio
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate+50)
    engine.say(question)
    print(question)
    engine.runAndWait()
    return input("")
    # r = sr.Recognizer()
    # with sr.Microphone() as source:
    #     audio = r.listen(source)

    # #recognize what you said and convert it to text
    # try:
    #     print(r.recognize_google(audio))
    #     return(r.recognize_google(audio))
        
    #     #errors responses 
    # except sr.UnknownValueError:
    #     return(ask("Sorry I didn't understand that, can you repeat?"))
    # except sr.RequestError as e:
    #     return(ask("Sorry I didn't understand that, can you repeat?"))

def say(sentence):
    engine = pyttsx3.init()
    engine.say(sentence)
    print(sentence)
    engine.runAndWait()