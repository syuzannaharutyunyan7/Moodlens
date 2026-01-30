import string
from data import FILLER_WORDS

def normalize_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    words = [w for w in words if w not in FILLER_WORDS]
    return words

def contains_phrase(text, phrase):
    return phrase in text
