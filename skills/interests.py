from random import sample
import json

class RecommendExhibit:

    def __init__(self):
        data_file = open("data/exhibits_data.json")
        self.data = json.load(data_file)
        self.interests = []
        self.matched_exhibits = []
        self.complete = False

    def add_entities(self, entities):
        for entity in entities:
            if entity.label_ == "INTEREST":
                self.interests.append(entity)

    def missing_info(self):
        return len(self.interests) == 0

    def prompt(self):
        prompts = ["What are you interested in?", "What's your passion?", "What do you like?"]
        return sample(prompts, 1)[0]

    def find_match(self):
        counters = {}
        for exhibit in self.data.keys():
            counter = 0
            for interest in self.interests:
                if interest.text in self.data[exhibit]["interests"]:
                    counter += 1
            counters[exhibit] = counter

        matches = []
        for exhibit,counter in counters.items():
            matches.append((exhibit,counter))
        matches.sort(key=lambda x:x[1],reverse=True)
        top_matches = []
        if matches[0][1] > 0:
            top_matches.append(matches[0][0])
            if matches[1][1] > 0:
                top_matches.append(matches[1][0])
        self.matched_exhibits = top_matches

    def get_entities(self):
        entities = []
        for interest in self.interests:
            entities.append(interest)
        for match in self.matched_exhibits:
            entities.append(match)
        return entities

    def respond(self, output_file):
        self.find_match()
        if len(self.matched_exhibits):
            output_string = "Found following matches: "
            for match in self.matched_exhibits:
                output_string += str(match) + " "
            output_file.write(output_string + "\n")
            response = "Awesome! Based on your interest in " + self.interests[0].text
            if len(self.interests) > 1:
                for interest in self.interests[1:-1]:
                    response += ", " + interest.text
                response += " and " + self.interests[-1].text
            response += " I think you should check out our " + self.matched_exhibits[0]
            if len(self.matched_exhibits) > 1:
                response += " and " + self.matched_exhibits[1] + " exhibitions. Would you like to hear more about them?"       
            else:
                response += " exhibition. Would you like to hear more about it?"
            error = False
        else:
            response = "Sorry, it seems like we don't have anything matching your interests at the moment."
            error = True
        output_file.write(">> " + response + "\n")
        return response, error

    def action(self):
        response = []
        for exhibit in self.matched_exhibits:
            response.append(self.data[exhibit]["description"])
        self.complete = True
        return response