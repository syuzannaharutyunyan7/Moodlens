from analyzer import analyze_emotions, analyze_intent, analyze_tone
from logger import log_session

print("🧠 MoodLens – Text Emotion & Intent Analyzer")
print("-" * 40)

user_text = input("Enter your text:\n> ")

emotions = analyze_emotions(user_text)
intent, trigger = analyze_intent(user_text)
tone, tone_score = analyze_tone(user_text)

print("\n🔍 Analysis Summary")
print("-" * 40)

if emotions:
    primary_emotion = emotions.most_common(1)[0]
    print(f"Primary Emotion: {primary_emotion[0].capitalize()} ({primary_emotion[1]} hits)")
else:
    print("Primary Emotion: Not detected")

print(f"Tone: {tone} (score: {tone_score})")
print(f"Intent: {intent.capitalize()}")

if trigger:
    print(f"Triggered by phrase: \"{trigger}\"")

log_session(user_text, emotions, intent, tone)

print("\n📁 Session saved to logs/mood_history.txt")
