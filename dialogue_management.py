from intent import Welcome, Fallback
from tickets import PurchaseTickets
from info import GiveInformation
from interests import RecommendExhibit
from intent_classifier import get_intent
from communication import ask, say

def str_to_intent(label):
    if label == "tix":
        return(PurchaseTickets())
    if label == "interest":
        return(RecommendExhibit())
    if label == "info":
        return(GiveInformation())
    if label == "welcome":
        return(Welcome())
    else:
        return(Fallback())


query = ask("Hello, my name is Cosmo. How can I help you?")
answer = "yes"
while(answer == "yes"):
    intent = str_to_intent(get_intent(query))
    if type(intent) == type(GiveInformation):
        intent.classify_question(query)
        if intent.query == "Are there exhibitions for kids?":
            say("The museum is a beautiful place for all the members of the family to enjoy learning while playing")
            ''' or with grounding
            response = ask("If I understand correctly you want to know if there are exhibitions for kids?")
            if response == "yes":
                say("The museum is a beautiful place for all the members of the family to enjoy learning while playing")
            if response == "no":
                response = ask("Can you repeat the question?")
                intent.classify_question(response)''' 
        elif intent.query == "I want to know which exhibitions the museum has":
            say("The museum has five permanent exhibitions: the flooded forest, the universe room, the antartic base, the geologic wall and the sustainable building")
        else: intent.new_sentence(query)
    else: intent.new_sentence(query)
    answer = ask("Can I help you with anything else?")
    if answer == "yes":
        query = ask("What can I help you with?")
    if answer == "no":
        say("Okay, have a nice day!")





















'''
def get_intent(query):
    model = pickle.load(open('model.sav', 'rb'))
    tf1 = pickle.load(open("tfidf1.pkl", 'rb'))
    tf1_new = TfidfVectorizer(vocabulary = tf1.vocabulary_)
    classes = ["tix", "interests", "info", "fallback", "welcome"]
    query = clean_text(query)
    query = tf1_new.fit_transform([query])
    pred = model.predict(query)
    return classes[pred[0]]

def confirm(case):
    if type(case) == type(intent.Tickets()):
        while(not case.ticket_available()):
            new_date = communication.communicate(case.prompt("NOT_AVAIL"))
            case.ents_new_sentence(new_date)
    text = communication.communicate(case.prompt("FULL"))
    if text.lower() == "yes":
        communication.communicate(case.response(text))
        new_intent()
    elif text.lower() == "no":
        missing_info = communication.communicate(case.response(text))
        case.ents_new_sentence(missing_info)
        confirm()

def do_intent(case):
    i = 0
    while not(case.empty_slot() == None):
        sent_fill_slot = communication.communicate(case.empty_slot())
        case.ents_new_sentence(sent_fill_slot)
    confirm(case)

def new_intent():
    check = communication.communicate("Can I help you with something else? Please respond with YES or NO.")
    if check == "yes": 
        text = communication.communicate("How can I help you?")
        intent_ = get_intent(text)            
        do_intent(intent_)
    if check == "no":
        communication.communicate("I hope I solved all your questions. Have a nice day!")
        
intents = []
text = communication.communicate("How can I help you?")
intent_ = get_intent(text)

if intent_ == "tix":
    intents.append(intent.Tickets())
elif intent_ == "interest":
    intents.append(intent.Interest())
elif intent_ == "info":
    intents.append(intent.Info())
elif intent_ == "welcome":
    intents.append(intent.Welcome())
else:
    intents.append(intent.Fallback())

for case in intents:
    case.ents_new_sentence(text)
    do_intent(case)


start conversation: how can i help you? or hello!
wait for response: '...'
classify response as one of the intents with get_intent. Make a bool that says which intent is active
e.g. for tickets: start slot filling, ask for information slot, wait for response, extract info, repeat till slots filled
confirm if the slots are correct, wait for response, continue conversation or (change slots and repeat)
action: print ticket & response tell about printing the ticket
ask for any other problems --> repeat untill goodbye 
'''
