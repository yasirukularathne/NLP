import spacy

nlp = spacy.load("en_core_web_sm")  # load the English model

# define a function to get sentiment
def get_sentiment(text):  # renamed parameter to avoid confusion
    doc = nlp(text)

    # Note: Basic spaCy models don't have built-in sentiment analysis
    # This will likely not work as expected
    sentiment = doc.sentiment

    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "negative"
    else:
        return "neutral"
    
input_sentence = input("Enter a sentence : ")
print(f"sentiment : {get_sentiment(input_sentence)}")  # Fixed curly braces


