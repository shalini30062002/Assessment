import re
import string

def clean_text(text):
    # Convert to lowercase
    text = text.lower()

    # Remove HTML tags (if applicable)
    text = re.sub(r'<.*?>', '', text)

    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # Tokenization
    tokens = text.split()

    # Remove punctuation
    tokens = [word.strip(string.punctuation) for word in tokens]

    # Remove stopwords (if you have a custom list)
    custom_stopwords = ['the', 'and', 'in', 'to', 'of', 'is', 'it', 'this', 'for', 'with']
    tokens = [word for word in tokens if word not in custom_stopwords]

    # Join tokens back to text
    cleaned_text = ' '.join(tokens)

    return cleaned_text
