import speech_recognition as sr

#obtaining audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say Something:")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print("You said : {}".format(text))
except sr.UnknownValueError: 
    print ("Could not undersatnd the audio")
except sr.RequestError as e:
    print("Sorry could not recognize what you said; {0}".format(e))
