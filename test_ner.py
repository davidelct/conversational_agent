import spacy

nlp = spacy.load("spacy_model/")

def test_ner(text):
    doc = nlp(text)
    print(doc.text)
    print("Entities", [(ent.text, ent.label_) for ent in doc.ents])
    print()


texts = ["a ticket for next weekend", 
    "one ticket for next weekend",
    "five tickets for next weekend",
    "a ticket for Dec 24",
    "five tickets for Nov 25",
    "i want to buy six tickets",
    "i want to buy a ticket for the universe room exhibition",
    "six tickets for May 05 please",
    "i want to buy one ticket for the universe room exhibition",
    "i want to buy one ticket for tomorrow",
    "next tuesday",
    "i want to buy tickets for the exhibition about evolution",
    "a ticket for the antarctic base exhibition",
    "three tickets for the flooded forest exhibition",
    "i want to go on Aug 22 are there tickets for that day",
    "i want to go to the museum are there any tickets this week?", 
    "six tickets for the caixa museum please",
    "i would like to go to the sustainable building exhibition this Saturday",
    "i want to buy two tickets for the exhibition about floodings",
    "would you advise me to go to antarctic base",
    "i love education which exhibition should i go to",
    "i want to learn more about photos which exhibition do you recommend",
    "i'd like to learn about vulcanos",
    "show me exhibits about landscape",
    "show me exhibits about floodings",
    "evolution and nature",
    "cosmos and universe",
    "i like exploration and science",
    "what about climate change and sustainability"
    ]

for text in texts:
    test_ner(text)