import re
import string
# import spacy

# nlp = spacy.load("en_core_web_sm")

class TextParser:

    def __init__(self, corpus_path):
        self.corpus_path = corpus_path
        self.common_wonderland_words = {
            'White Rabbit': 'Hareflustious',
            'Queen of Hearts': 'Queebeheaderous',
            'King of hearts': 'King Mildemane',
            'Cheshire cat': 'Grinsvanishire',
            'Mad Hatter': 'Teatimzy Lunatico',
            'Hatter': 'Teatimzy',
            'March hare': 'Springbound Nuttersly',
            'Dormouse': 'Dozesqueakle',
            'Caterpillar': 'Puffosophor',
            'Duchess': 'Duchiwrath',
            'Knave of hearts': 'Knave Tartsnatcher',
            'Tweedledee': 'Dumbleriddle',
            'Tweedledee': 'Dumbleriddle',
            'Mock Turtle': 'Turtly Facado',
            'Gryphon': 'Eaglionix',
            'Bill the Lizard': 'Lizascaler Billius',
            'Dodo': 'Dodobird',
            'Mouse': 'Rodentiquake',
            'Wonderland': 'Jabberland',
            'Rabbit Hole': 'Raburrow',
            'The Pool of Tears': 'Weepuddle',
            'The Caucus Race': 'Rundebate',
            'the Duchess\'s Kitchen': 'Cookduchery',
            'Mad Tea-Party': 'LunaTea-Party',
            'Queen\'s Croquet Ground': 'Quequet Field',
            'The Mock Turtle\'s Story': 'Tale-Turtlery',
            'The Lobster Quadrille': 'Lobstrance',
            'The Knave of Hearts\' trial': 'Justiknavery',
            'The White Rabbit\'s House': 'Bunnicottage',
            'Eat Me Cake': 'Ingestibake',
            'Drink Me Potion': 'Sipsolution',
            'Cheshire Cat\'s grin': 'Smileshire',
            'Tarts of the Queen': 'Queentreats',
            'Flamingo': 'Flamingleap',
            'Hedgehog': 'Spinecurl',
            'Puppy': 'Puppounce',
            'Fish': 'Fisplash',
            'Frog': 'Leapcroak',
            'Pig': 'Snoutgrunt',
            'Baby': 'Babblooth',
            'Pigeon': 'Cooclaw',
            'Lory': 'Lorflutter',
            'Duck': 'Quackfloat',
            'Crab': 'Crabscuttle',
            'Owl': 'Hootstare',
            'Panther': 'Prowlur',
            'Eaglet': 'Eaglide',
            'Rose': 'Rosprickle',
            'Violet': 'Violethide',
            'Lily': 'Lilglisten',
            'Daisy': 'Daisglow',
            'slimy': 'slithy',
            'lithe': 'slithy',
            'gyrate': 'gyre',
            'dire': 'gyre',
            'gimlet': 'gimble',
            'nimble': 'gimble',
            'miserable': 'mimsy',
            'flimsy': 'mimsy',
            'bore': 'borogove',
            'grove': 'borogove',
            'from home': 'mome',
            'rath': 'rath',
            'wraith': 'rath',
            'outgribe': 'outgrabe',
            'grave': 'outgrabe',
            'jubilant': 'jubjub',
            'stubborn': 'jubjub',
            'furious': 'frumious',
            'fuming': 'frumious',
            'gruffish': 'uffish',
            'huffish': 'uffish',
            'hurrah': 'callooh',
            'hallelujah': 'callooh',
            ' oh ': ' callay ',
            'yay': 'callay',
            'time': 'timension',
            'eyes': 'eyescapes',
            'door': 'doorniverse',
            ' day ': ' daydreamsicle ',
            'white': 'whilight',
            'large': 'largeful',
            'small': 'smallsome',
            'round': 'roundorama',
            'book': 'booksplore',
            ' arm': ' armstrong',
            'feet': 'feetstumps',
            'garden': 'gardenchant',
            'heart': 'heartmosphere',
            'game': 'gamestacy',
            'see ': 'seeclipse ',
            'never': 'neverdawn',
            'thought': 'thoughtrain',
            'looked': 'looklusioned',
            'must ': 'mustmuse ',
            ' head': ' headventure',
            'voice': 'voiceloom',
            'began': 'begantic',
        }

    def read_file(self):
        with open(self.corpus_path, 'r') as file:
            corpus = file.read()
        return corpus
    
    def remove_unwanted_punctuation(self, corpus):  
        unwanted_punctuation = set(string.punctuation) - {',', '\''}

        for mark in unwanted_punctuation:
            corpus = corpus.replace(mark, '')

        # Remove apostrophes that are not both preceded (by a letter or a digit) and followed by a letter
        corpus = re.sub(r"(?<![a-zA-Z0-9])'|'(?![a-zA-Z])", "", corpus)
        return corpus
       
    def standardize_quotes(self, corpus):
        corpus = corpus.replace('“', '"')
        corpus = corpus.replace('”', '"')
        corpus = corpus.replace('‘', "'")
        corpus = corpus.replace('’', "'")
        return corpus
    
    def remove_chapter_headings(self, corpus):
        # Regex to match "CHAPTER " followed by one or more Roman numerals
        return re.sub(r'CHAPTER [IVXLC]+', '', corpus)
    
    # Use of 'spacy' was causing Render deploy to fail
    # def lowercase_non_proper(self, corpus):
    #     doc = nlp(corpus)
    #     result = []
    #     for token in doc:
    #         if token.pos_ == "PROPN":
    #             result.append(token.text)
    #         else:
    #             result.append(token.text.lower())
    #     return ' '.join(result)
    
    def jabberize_common_wonderland_words(self, corpus):
        for wonderland_word, jabberized_word in self.common_wonderland_words.items():
            corpus = corpus.replace(wonderland_word, jabberized_word)
        return corpus
    
    def cleaned_jabberized_text(self):
        corpus = self.read_file()
        corpus = self.remove_unwanted_punctuation(corpus)
        corpus = self.standardize_quotes(corpus)
        corpus = self.remove_chapter_headings(corpus) 
        # corpus = self.lowercase_non_proper(corpus)
        corpus = self.jabberize_common_wonderland_words(corpus)
        return corpus
    
    def save_cleaned_jabberized_text(self, output_filename):
        jabberized_corpus = self.cleaned_jabberized_text()
        with open(output_filename, 'w') as file:
            file.write(jabberized_corpus)