from collections import Counter
from data import (
    EMOTION_KEYWORDS,
    INTENT_PHRASES,
    POSITIVE_WORDS,
    NEGATIVE_WORDS
)
from utils import normalize_text, contains_phrase

def analyze_emotions(text):
    words = normalize_text(text)
    scores = Counter()

    for emotion, keywords in EMOTION_KEYWORDS.items():
        for word in words:
            if word in keywords:
                scores[emotion] += 1

    return scores

def analyze_intent(text):
    text = text.lower()
    for intent, phrases in INTENT_PHRASES.items():
        for phrase in phrases:
            if contains_phrase(text, phrase):
                return intent, phrase
    return "unknown", None

def analyze_tone(text):
    words = normalize_text(text)
    score = 0

    for word in words:
        if word in POSITIVE_WORDS:
            score += 1
        elif word in NEGATIVE_WORDS:
            score -= 1

    if score > 2:
        return "Positive", score
    elif score < -2:
        return "Negative", score
    else:
        return "Neutral", score
