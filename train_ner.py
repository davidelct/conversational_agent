import spacy

nlp=spacy.load('en_core_web_sm')

TRAIN_DATA = [
        ("a ticket", {"entities": [(0,1,"CARDINAL")]}),
        ("a ticket please", {"entities": [(0,1,"CARDINAL")]}),
        ("can i get a ticket please", {"entities": [(10,11,"CARDINAL")]}),
        ("could i get a ticket", {"entities": [(12,13,"CARDINAL")]}),
        ("could i please get a ticket", {"entities": [(19,20,"CARDINAL")]}),
        ("i'd like a ticket", {"entities": [(9,10,"CARDINAL")]}),
        ("i'd like a ticket please", {"entities": [(9,10,"CARDINAL")]}),
        ("i'd like to get a ticket", {"entities": [(16,17,"CARDINAL")]}),
        ("i'd like to get a ticket please", {"entities": [(16,17,"CARDINAL")]}),
        ("a ticket for 29 Nov", {"entities": [(0,1,"CARDINAL"),(13,19,"DATE")]}),
        ("a ticket for Sep 15", {"entities": [(0,1,"CARDINAL"),(13,19,"DATE")]}),
        ("a ticket for Apr 11", {"entities": [(0,1,"CARDINAL"),(13,19,"DATE")]}),
        ("a ticket for Apr 05", {"entities": [(0,1,"CARDINAL"),(13,19,"DATE")]}),
        ("a ticket for next week", {"entities": [(0,1,"CARDINAL"),(13,22,"DATE")]}),
        ("a ticket on Friday", {"entities": [(0,1,"CARDINAL"),(9,18,"DATE")]}),
        ("a ticket for next Saturday", {"entities": [(0,1,"CARDINAL"),(13,26,"DATE")]}),
        ("a ticket for next Friday", {"entities": [(0,1,"CARDINAL"),(13,26,"DATE")]}),
        ("one ticket for Mar 09", {"entities": [(0,3,"CARDINAL"),(15,21,"DATE")]}),
        ("one ticket for 10 Jun", {"entities": [(0,3,"CARDINAL"),(15,21,"DATE")]}),
        ("one ticket for May 07", {"entities": [(0,3,"CARDINAL"),(15,21,"DATE")]}),
        ("one ticket for 06 Feb", {"entities": [(0,3,"CARDINAL"),(15,21,"DATE")]}),
        ("two tickets for 18 Dec", {"entities": [(0,3,"CARDINAL"),(16,22,"DATE")]}),
        ("two tickets for Jul 17", {"entities": [(0,3,"CARDINAL"),(16,22,"DATE")]}),
        ("two tickets for 16 Jun", {"entities": [(0,3,"CARDINAL"),(16,22,"DATE")]}),
        ("two tickets for Aug 06", {"entities": [(0,3,"CARDINAL"),(16,22,"DATE")]}),
        ("three tickets for 26 Feb", {"entities": [(0,5,"CARDINAL"),(18,24,"DATE")]}),
        ("three tickets for 22 Sep", {"entities": [(0,5,"CARDINAL"),(18,24,"DATE")]}),
        ("three tickets for 10 Nov", {"entities": [(0,5,"CARDINAL"),(18,24,"DATE")]}),
        ("three tickets for 14 May", {"entities": [(0,5,"CARDINAL"),(18,24,"DATE")]}),
        ("four tickets for 21 Apr", {"entities": [(0,4,"CARDINAL"),(17,23,"DATE")]}),
        ("four tickets for Sep 01", {"entities": [(0,4,"CARDINAL"),(17,23,"DATE")]}),
        ("four tickets for 26 Dec", {"entities": [(0,4,"CARDINAL"),(17,23,"DATE")]}),
        ("four tickets for Nov 04", {"entities": [(0,4,"CARDINAL"),(17,23,"DATE")]}),
        ("five tickets for Jun 04", {"entities": [(0,4,"CARDINAL"),(17,23,"DATE")]}),
        ("five tickets for May 15", {"entities": [(0,4,"CARDINAL"),(17,23,"DATE")]}),
        ("five tickets for 13 Aug", {"entities": [(0,4,"CARDINAL"),(17,23,"DATE")]}),
        ("five tickets for 24 Feb", {"entities": [(0,4,"CARDINAL"),(17,23,"DATE")]}),
        ("six tickets for 21 Jul", {"entities": [(0,3,"CARDINAL"),(16,22,"DATE")]}),
        ("six tickets for Aug 09", {"entities": [(0,3,"CARDINAL"),(16,22,"DATE")]}),
        ("six tickets for Apr 17", {"entities": [(0,3,"CARDINAL"),(16,22,"DATE")]}),
        ("six tickets for 09 Aug", {"entities": [(0,3,"CARDINAL"),(16,22,"DATE")]}),
        ("a ticket for 09 Dec please", {"entities": [(0,1,"CARDINAL"),(13,19,"DATE")]}),
        ("a ticket for 30 Mar please", {"entities": [(0,1,"CARDINAL"),(13,19,"DATE")]}),
        ("a ticket for 01 Sep please", {"entities": [(0,1,"CARDINAL"),(13,19,"DATE")]}),
        ("a ticket for 04 Dec please", {"entities": [(0,1,"CARDINAL"),(13,19,"DATE")]}),
        ("a ticket for tomorrow please", {"entities": [(0,1,"CARDINAL"),(13,21,"DATE")]}),
        ("a ticket on Thursday please", {"entities": [(0,1,"CARDINAL"),(12,20,"DATE")]}),
        ("a ticket for next Monday please", {"entities": [(0,1,"CARDINAL"),(13,24,"DATE")]}),
        ("a ticket on Tuesday please", {"entities": [(0,1,"CARDINAL"),(12,19,"DATE")]}),
        ("one ticket for 13 Nov please", {"entities": [(0,3,"CARDINAL"),(16,21,"DATE")]}),
        ("one ticket for 26 Feb please", {"entities": [(0,3,"CARDINAL"),(16,21,"DATE")]}),
        ("one ticket for 18 Oct please", {"entities": [(0,3,"CARDINAL"),(16,21,"DATE")]}),
        ("one ticket for 21 Oct please", {"entities": [(0,3,"CARDINAL"),(16,21,"DATE")]}),
        ("two tickets for 06 Jun please", {"entities": [(0,3,"CARDINAL"),(16,22,"DATE")]}),
        ("two tickets for 07 Oct please", {"entities": [(0,3,"CARDINAL"),(16,22,"DATE")]}),
        ("two tickets for Apr 25 please", {"entities": [(0,3,"CARDINAL"),(16,22,"DATE")]}),
        ("two tickets for Jun 07 please", {"entities": [(0,3,"CARDINAL"),(16,22,"DATE")]}),
        ("three tickets for 08 Sep please", {"entities": [(0,5,"CARDINAL"),(18,24,"DATE")]}),
        ("three tickets for 15 Nov please", {"entities": [(0,5,"CARDINAL"),(18,24,"DATE")]}),
        ("three tickets for 30 Nov please", {"entities": [(0,5,"CARDINAL"),(18,24,"DATE")]}),
        ("three tickets for Mar 20 please", {"entities": [(0,5,"CARDINAL"),(18,24,"DATE")]}),
        ("four tickets for Mar 22 please", {"entities": [(0,4,"CARDINAL"),(17,23,"DATE")]}),
        ("four tickets for 31 Oct please", {"entities": [(0,4,"CARDINAL"),(17,23,"DATE")]}),
        ("four tickets for Mar 16 please", {"entities": [(0,4,"CARDINAL"),(17,23,"DATE")]}),
        ("four tickets for 15 Feb please", {"entities": [(0,4,"CARDINAL"),(17,23,"DATE")]}),
        ("five tickets for Jul 16 please", {"entities": [(0,4,"CARDINAL"),(17,23,"DATE")]}),
        ("five tickets for Apr 22 please", {"entities": [(0,4,"CARDINAL"),(17,23,"DATE")]}),
        ("five tickets for 31 May please", {"entities": [(0,4,"CARDINAL"),(17,23,"DATE")]}),
        ("five tickets for Feb 27 please", {"entities": [(0,4,"CARDINAL"),(17,23,"DATE")]}),
        ("six tickets for 13 Sep please", {"entities": [(0,3,"CARDINAL"),(16,22,"DATE")]}),
        ("six tickets for 25 Oct please", {"entities": [(0,3,"CARDINAL"),(16,22,"DATE")]}),
        ("six tickets for 08 May please", {"entities": [(0,3,"CARDINAL"),(16,22,"DATE")]}),
        ("six tickets for Aug 09 please", {"entities": [(0,3,"CARDINAL"),(16,22,"DATE")]}),
        ("two tickets for next Sunday", {"entities": [(0,3,"CARDINAL"),(16,27,"DATE")]}),
        ("three tickets for next Tuesday", {"entities": [(0,5,"CARDINAL"),(18,30,"DATE")]}),
        ("five tickets on Wednesday please", {"entities": [(0,4,"CARDINAL"),(16,25,"DATE")]}),
        ("i want to buy a ticket for the universe room exhibition", {"entities": [(14,15,"CARDINAL"),(31,44,"EXHIBIT")]}),
        ("i want to buy one ticket for the flooded forest exhibition", {"entities": [(14,17,"CARDINAL"),(33,47,"EXHIBIT")]}),
        ("i want to buy five tickets for the antarctic base exhibition", {"entities": [(14,18,"CARDINAL"),(35,49,"EXHIBIT")]}),
        ("i want to buy six tickets for the geological wall exhibition", {"entities": [(14,18,"CARDINAL"),(34,49,"EXHIBIT")]}),
        ("a ticket for the sustainable building exhibition", {"entities": [(0,1,"CARDINAL"),(16,37,"EXHIBIT")]}),
        ("two tickets for the universe room exhibition", {"entities": [(0,3,"CARDINAL"),(20,33,"EXHIBIT")]}),
        ("three tickets for the sustainable building exhibition", {"entities": [(0,5,"CARDINAL"),(22,42,"EXHIBIT")]}),
        ("four tickets for the universe room exhibition", {"entities": [(0,4,"CARDINAL"),(21,34,"EXHIBIT")]}),
        ("six tickets for the flooded forest exhibition", {"entities": [(0,3,"CARDINAL"),(20,34,"EXHIBIT")]}),
        ("five tickets for the geological wall exhibition", {"entities": [(0,4,"CARDINAL"),(21,36,"EXHIBIT")]}),
        ("one ticket for the universe room exhibition", {"entities": [(0,3,"CARDINAL"),(19,32,"EXHIBIT")]}),
        ("i'd like to get one ticket for the universe room exhibition", {"entities": [(16,19,"CARDINAL"),(35,48,"EXHIBIT")]}),
        ("i wanna buy three tickets for the flooded forest exhibition", {"entities": [(12,17,"CARDINAL"),(34,48,"EXHIBIT")]}),
        ("get me five tickets for the antarctic base exhibition", {"entities": [(7,11,"CARDINAL"),(28,42,"EXHIBIT")]}),
        ("can i get four tickets for the geological wall exhibition", {"entities": [(10,14,"CARDINAL"),(31,46,"EXHIBIT")]}),
        ("can i get a ticket for the sustainable building exhibition", {"entities": [(10,11,"CARDINAL"),(27,47,"EXHIBIT")]}),
        ("tickets for the universe room exhibition", {"entities": [(16,29,"EXHIBIT")]}),
        ("two tickets for the sustainable building exhibition tomorrow", {"entities": [(0,3,"CARDINAL"),(20,40,"EXHIBIT"),(50,60,"DATE")]}),
        ("four tickets for the universe room exhibition next week", {"entities": [(0,4,"CARDINAL"),(21,34,"EXHIBIT"),(46,55,"DATE")]}),
        ("six tickets for the flooded forest exhibition on Feb 15", {"entities": [(0,3,"CARDINAL"),(20,34,"EXHIBIT"),(49,55,"DATE")]}),
        ("five tickets for the geological wall exhibition next week", {"entities": [(0,4,"CARDINAL"),(21,36,"EXHIBIT"),(48,57,"DATE")]}),
        ("one ticket for the universe room exhibition this weekend", {"entities": [(0,3,"CARDINAL"),(19,32,"EXHIBIT"),(44,56,"DATE")]}),
        ("i want to go on Jun 23 are there tickets for that day", {"entities": [(16,22,"DATE")]}),
        ("i'd like to go this Wednesday are there tickets for that day", {"entities": [(15,29,"DATE")]}),
        ("this Saturday are there tickets for that day", {"entities": [(0,13,"DATE")]}),
        ("i like evolution", {"entities": [(7,16,"INTEREST")]}),
        ("i like mars", {"entities": [(7,11,"INTEREST")]}),
        ("i like planets", {"entities": [(7,14,"INTEREST")]}),
        ("i like forest", {"entities": [(7,13,"INTEREST")]}),
        ("i'm interested in physics", {"entities": [(18,25,"INTEREST")]}),
        ("i'm interested in stars", {"entities": [(18,23,"INTEREST")]}),
        ("i'm interested in plants", {"entities": [(18,24,"INTEREST")]}),
        ("i'm interested in climate change", {"entities": [(18,32,"INTEREST")]}),
        ("what do you have related to universe", {"entities": [(28,36,"INTEREST")]}),
        ("what do you have related to big bang", {"entities": [(28,36,"INTEREST")]}),
        ("what do you have related to brain", {"entities": [(28,33,"INTEREST")]}),
        ("what do you have related to technology", {"entities": [(28,38,"INTEREST")]}),
        ("i love brazil", {"entities": [(7,13,"INTEREST")]}),
        ("i love environment", {"entities": [(7,18,"INTEREST")]}),
        ("i love rocks", {"entities": [(7,12,"INTEREST")]}),
        ("show me exhibits about sun", {"entities": [(23,26,"INTEREST")]}),
        ("show me exhibits about jungle", {"entities": [(23,29,"INTEREST")]}),
        ("show me exhibitions about water", {"entities": [(26,31,"INTEREST")]}),
        ("show me exhibits about sustainability", {"entities": [(23,37,"INTEREST")]}),
        ("show me exhibitions about architecture", {"entities": [(26,38,"INTEREST")]}),
        ("show me stuff on science", {"entities": [(17,24,"INTEREST")]}),
        ("show me stuff on moon", {"entities": [(17,21,"INTEREST")]}),
        ("show me stuff on animals", {"entities": [(17,24,"INTEREST")]}),
        ("is there an exhibition about gravity", {"entities": [(29,36,"INTEREST")]}),
        ("is there an exhibition about amazon", {"entities": [(29,35,"INTEREST")]}),
        ("is there an exhibition about photos", {"entities": [(29,35,"INTEREST")]}),
        ("i'd like to hear about cosmos", {"entities": [(23,29,"INTEREST")]}),
        ("i want to learn more about universe which exhibition do you recommend", {"entities": [(27,35,"INTEREST")]}),
        ("ecology is a passion of mine does any of the exhibitions in the caixa museum cover this", {"entities": [(0,7,"INTEREST")]}),
        ("architecture is a passion of mine does any of the exhibitions cover this", {"entities": [(0,12,"INTEREST")]}),
        ("i want to buy two tickets for the exhibition about technology", {"entities": [(14,17,"CARDINAL"),(51,61,"INTEREST")]}),
        ("i'd like five tickets for the exhibition about cosmos", {"entities": [(9,13,"CARDINAL"),(47,53,"INTEREST")]}),
        ("one ticket for the exhibition on rocks", {"entities": [(0,3,"CARDINAL"),(33,38,"INTEREST")]}),
        ("tickets for the exhibition on big bang today", {"entities": [(30,38,"INTEREST"),(39,44,"DATE")]}),
        ("two tickets for the exhibition about stars on Apr 22", {"entities": [(0,3,"CARDINAL"),(37,42,"INTEREST"),(46,52,"DATE")]}),
        ("a ticket for the exhibition on ice tomorrow", {"entities": [(0,1,"CARDINAL"),(31,34,"INTEREST"),(35,43,"DATE")]}),
        ("tickets for exhibit on forest next weekend", {"entities": [(23,29,"INTEREST"),(30,42,"DATE")]})
]
ner=nlp.get_pipe("ner")
for _, annotations in TRAIN_DATA:
  for ent in annotations.get("entities"):
    ner.add_label(ent[2])

pipe_exceptions = ["ner", "trf_wordpiecer", "trf_tok2vec"]
unaffected_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]

import random
from spacy.util import minibatch, compounding
from spacy.training import Example
from pathlib import Path

# TRAINING THE MODEL
with nlp.disable_pipes(*unaffected_pipes):

  # Training for 30 iterations
  for iteration in range(30):

    # shuufling examples  before every iteration
    random.shuffle(TRAIN_DATA)
    losses = {}
    # batch up the examples using spaCy's minibatch
    batches = minibatch(TRAIN_DATA, size=compounding(4.0, 32.0, 1.001))
    for batch in batches:
        for text, annotations in batch:
            # create Example
            doc = nlp.make_doc(text)
            example = Example.from_dict(doc, annotations)
            nlp.update(
                [example],
                drop=0.5,  # dropout - make it harder to memorise data
                losses=losses,
                    )
        print("Losses", losses)

doc = nlp("i want to go on Aug 22 are there tickets for that day")
print("Entities", [(ent.text, ent.label_) for ent in doc.ents])

output_dir = Path('./spacy_model/')
nlp.to_disk(output_dir)
print("Saved model to", output_dir)