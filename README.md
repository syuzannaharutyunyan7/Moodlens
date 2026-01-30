# MoodLens 🧠

MoodLens is a small Python program I made that tries to understand how you’re feeling based on what you write. You just type a sentence (or a few) about your day or your thoughts, and it tells you:

* How you might be feeling (**emotions** like happy, sad, stressed, tired, angry, bored…)
* What you might be doing with your words (**intent** — venting, reflecting, celebrating, asking for help)
* Your overall **tone** (positive, neutral, or negative)

It’s simple — no AI magic here — just Python doing some clever text analysis. But it can actually give you a little snapshot of your mood or mindset.

---

## How It Works

1. You type something about how you’re feeling.
2. MoodLens looks for emotion keywords, phrases that hint at your intent, and figures out a simple tone score.
3. It prints a little summary explaining what it detected and why.
4. It logs your entry so you can look back at your mood history later.

---

## Example

```
Enter your text:
> I’m feeling a bit tired and stressed after a long day

🔍 Analysis Summary
----------------------------------------
Primary Emotion: Stressed (1 hits)
Secondary Emotion: Tired (1 hits)
Tone: Neutral (score: -1)
Intent: Reflection

📁 Session saved to logs/mood_history.txt
```
---

## Logs

All your entries are saved in `logs/mood_history.txt`. For each session, you’ll get:

* The text you typed
* The emotions detected
* The tone score
* Any intent it noticed

It’s kind of fun to look back and see how your moods and thoughts have changed over time.

---

## Future Ideas

* Pick up more subtle emotions like *confused*, *frustrated*, or *anxious*
* Suggest helpful things to do depending on your mood (like music, journaling, or breathing exercises)
* Make a GUI version so it’s a bit prettier to use
* Create charts or summaries to see your mood trends over time

---

