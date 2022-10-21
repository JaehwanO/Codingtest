import spacy

nlp = spacy.load("en_core_web_sm")

def find_persons(text):
     # Create Doc object
     doc2 = nlp(text)

     # Identify the persons
     persons = [ent.text for ent in doc2.ents if ent.label_ == 'PERSON']

     # Return persons
     return persons
     
def anonymize_text(sentences):
    print(find_persons("John is old"))

    