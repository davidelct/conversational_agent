import pyttsx3

#initialaize
engine = pyttsx3.init()

#sentence to TTS
engine.say("How many tickets do you want?")
engine.say("How many tickets do you want to buy?")
engine.say("How many tickets do you need?")

engine.runAndWait()
