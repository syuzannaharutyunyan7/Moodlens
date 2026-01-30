from datetime import datetime
import os

LOG_FILE = "logs/mood_history.txt"

# Make sure the logs folder exists
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

def log_session(text, emotions, intent, tone):
    with open(LOG_FILE, "a") as file:
        file.write(f"\n--- {datetime.now()} ---\n")
        file.write(f"Text: {text}\n")
        file.write(f"Emotions: {dict(emotions)}\n")
        file.write(f"Intent: {intent}\n")
        file.write(f"Tone: {tone}\n")
