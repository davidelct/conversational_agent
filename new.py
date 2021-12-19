from ner import parse
import datetime_handling
from random import sample
exhibit_names = ['universe room', 'flooded forest',
                 'antarctic base', 'geological wall', 'sustainable building']

class Intent():
    
    def __init__(self):
        self.parameters = []

    def ents_new_sentence(self, sentence):
        self.entities = parse(sentence)


class Info(Intent):

    def __init__(self, exhibition = None):
        super().__init__()
        self.parameters = {"DATE": datetime_handling.get_date("today"), "CARDINAL": None, "EXHIBITION": None}
        self.exhibition = exhibition
        self.fill_slots()

    def ents_new_sentence(self, sentence):
        self.entities = parse(sentence)
        self.fill_slots()

    def prompt(self, slot):
        if slot == "EXHIBITION_TOPIC":
            sentences = ["That will be great! Which are your interests?", "Fantastic! Do you need any recommendations?", "Super duper! What do you want to visit at the cosmocaixa?"]
            return sample(sentences, 2)
        elif slot == "UNIVERSE_ROOM":
            sentences = ["Here you can find The Universe Room presents a storyline that, chronologically, spans from the Big Bang to the last frontiers of knowledge, a free tour whose objective is to stimulate the visitor's scientific curiosity through interactive experiences, real objects and scientific and artistic reproductions of the highest quality."]
            return sample(sentences, 2)
        elif slot == "FLOODED_FOREST":
            sentences = ["Here you can find The Flooded Forest offers you the opportunity to immerse yourself in this ecosystem where 50 percent of the planet's biodiversity lives. In this fragment of rainforest you will be able to discover some of the most representative species of the Amazon: alligators, ants, boas, fish, tropical birds and plants."]
            return sample(sentences, 2)
        elif slot == "ANTARTIC_BASE":
            sentences = ["Here you can find and discover large-format photographs of its biodiversity and images documenting the expeditions that promoted the golden age of polar exploration in Antarctica."]
            return sample(sentences, 2)
        elif slot == "GEOLOGICAL_WALL":
            sentences = ["Here you can find The Geological Wall is made up of seven large real pieces originated by different geological processes, which have contributed to shaping the structure of our planet."]
            return sample(sentences, 2)
        elif slot == "SUSTAINABLE_BUILDING":
            sentences = ["Here you can find The Green Building project, pursues education showing the public current and future environmental improvements."]
            return sample(sentences, 2)
        elif slot == "EXHIBITION":
            sentences = ["Which exhibition do you want to visit?"]
        else: return "fault"
    

    def fill_slots(self):
        for ent in self.entities:
            if ent.label_ == "DATE":
                self.date = ent.text
            elif ent.label == "EXHIBITION":
                self.exhibition = ent.text
        if self.exhibition == None:
            self.ask_exhibition()
    
