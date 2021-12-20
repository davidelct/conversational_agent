import speech_recognition as sr
import pyttsx3
from skills.tickets import PurchaseTickets
from skills.interests import RecommendExhibit
from nlu_units.intent_classifier import IntentClassifier
from nlu_units.ner import EntityExtractor
import sys

TEXTUAL_INPUT = False
class Agent:

    def __init__(self):
        self.past_intents = []
        self.current_intent = None
        self.current_intent_text = None
        self.asr = sr.Recognizer()
        self.tts = self.configure_tts(rate=50)
        self.intent_classifier = IntentClassifier("models/model.sav", "models/tfidf1.pkl")
        self.ner = EntityExtractor("models/spacy_model/")
        self.memory = []

        self.output_file = open("output.txt", "w")
       
        self.start_sequence()

    def configure_tts(self, rate=0):
        engine = pyttsx3.init()
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate+50)
        return engine

    def start_sequence(self):
        response = self.ask("Hello, my name is Cosmo. How can I help you?")
        self.start_new_intent(response)

    def start_new_intent(self, sentence):
        intent = self.intent_classifier.classify_intent(sentence)
        if intent == "tickets":
            new_intent = PurchaseTickets()
        elif intent == "interests":
            new_intent = RecommendExhibit()
        # elif intent == "info":
        #     new_intent = ProvideInfo()
        # elif intent == "welcome":
        #     new_intent = Welcome()
        # else:
        #     new_intent = Fallback()

        self.current_intent = new_intent
        self.current_intent_text = intent
        self.past_intents.append(new_intent)
        self.solve_current_intent(sentence)

    def solve_current_intent(self, sentence):
        intent = self.intent_classifier.classify_intent(sentence)
        self.output_file.write("Matched to " + intent + " intent\n")
        if intent != self.current_intent_text and intent != "slot filling":
            self.output_file.write("Creating new intent " + intent + "\n")
            self.start_new_intent(sentence)
        else:
            if len(self.memory):
                output_string = "Stored entities: "
                for i in range(len(self.memory)):
                    if isinstance(self.memory[i], str):
                        self.memory[i] = self.ner.parse(self.memory[i])[0] 
                    output_string += str(self.memory[i]) + " "
                output_string += "\n"
                self.output_file.write(output_string)
                self.current_intent.add_entities(self.memory)

            entities = self.ner.parse(sentence)
            output_string = "Extracted entities: "
            for entity in entities:
                output_string += str(entity) + " "
            output_string += "\n"
            self.output_file.write(output_string)
            self.current_intent.add_entities(entities)
            
            if self.current_intent.missing_info():
                self.solve_current_intent(self.ask(self.current_intent.prompt()))
            else:
                response, error = self.current_intent.respond(self.output_file)
                if error:
                    self.say(response)
                else:
                    confirm = self.ask(response)
                    while confirm != "proceed":
                        confirm = self.ask("Please say proceed, stop or quit")
                    if confirm.lower() == "proceed":
                        response = self.current_intent.action()
                        for r in response:
                            self.say(r)
                        self.continue_conversation()
                    elif confirm.lower() == "stop":
                        self.continue_conversation()
                    elif confirm.lower() == "quit":
                        self.quit()

    def continue_conversation(self):
        response = self.ask("How can I help you?")
        if response.lower() == "quit":
            self.quit()
        else:
            self.log_memory()
            self.start_new_intent(response)
    
    def log_memory(self):
        self.memory = self.current_intent.get_entities()

    def quit(self):
        sys.exit(0)

    def say(self, sentence):
        self.output_file.write("<< " + sentence + "\n")
        print(sentence)
        self.tts.say(sentence)
        self.tts.runAndWait()
        

    def ask(self, question):
        self.say(question)
        with sr.Microphone() as source:
            audio = self.asr.listen(source)
            try:
                response = self.asr.recognize_google(audio)
            except sr.UnknownValueError:
                response = self.ask("Sorry, I didn't catch that, could you repeat?")
        self.output_file.write(">> " + response + "\n")
        print(response)
        return response

Agent()