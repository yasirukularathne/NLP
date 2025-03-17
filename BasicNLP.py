import nltk
 
nltk.download('punkt_tab') #pukt vs punkt_tab

from nltk.tokenize import sent_tokenize #splitting sentences into words 

input_sentence = input ("Enter your sentence here:")

def sentence_type(sentence):
    sentence = sentence.strip()

    if sentence.endswith('?'):
         return 'question'
    elif sentence.endswith('.'):
         return 'statement'
    elif sentence.endswith('!'):
         return 'exclamation'
    else:
         return 'unknown'
    
sentences = sent_tokenize(input_sentence)

for sent in sentences :
         print(f"Sentence: {sent} → Type: {sentence_type(sent)}")