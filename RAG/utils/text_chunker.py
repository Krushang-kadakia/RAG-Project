import nltk
from nltk.tokenize import sent_tokenize

nltk.download("punkt")

def chunk_text(text, chunk_size=10):
    sentences = sent_tokenize(text)
    return [" ".join(sentences[i:i+chunk_size]) for i in range(0, len(sentences), chunk_size)]
