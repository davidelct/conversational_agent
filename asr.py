import speech_recognition as sr

#open microphone and obtaining audio
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Hi there, How can I help you?")
    audio = r.listen(source)

#recognize what you said and convert it to text
try:
    text = r.recognize_google(audio)
    print("did you say that: {}".format(text))
    #print(r.recognize_google(audio))
    #errors responses 
except sr.UnknownValueError:
    print("I could not understand what you said")
except sr.RequestError as e:
    print("Apologies, I couldn't understand what you said; {0}".format(e))
