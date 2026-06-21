# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

When I first ran the app, it opened as a Streamlit number guessing game that looked mostly okay, but a bunch of things were off once I started playing. The first thing I noticed was that the attempt counter did not match itself: on Normal difficulty the screen says you get 8 attempts, but before I made a single guess it already showed “7 attempts left.” The hints were also backwards because when my guess was too high it told me to “Go HIGHER!”, and when my guess was too low it told me to “Go LOWER!”, which made the clues misleading. I also noticed that New Game did not fully reset the score, history, or status, and it generated the secret number from 1 to 100 even when a different difficulty range was selected. When I checked `logic_utils.py`, several functions were only placeholders that raised `NotImplementedError`, so the game logic was not actually refactored into the helper file yet.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Start a Normal game (says "8 attempts") and look before guessing | Should show 8 attempts left before any guess | Shows 7 attempts left before I guess anything | No error, counter just starts one too low |
| Guess a number that is higher than the secret | Hint should say "Go LOWER!" | Hint says "Go HIGHER!" (backwards) | No error, just wrong message |
| Guess a number that is lower than the secret | Hint should say "Go HIGHER!" | Hint says "Go LOWER!" (backwards) | No error, just wrong message |
| Click "New Game" after finishing a round | Score, guess history, and status should all reset | Score, history, and status are not fully cleared | No error, old game data carries over |
| Pick a harder difficulty, then click "New Game" | Secret should be generated within the difficulty's range | Secret is always generated from 1 to 100 | No error, range is ignored |
| Trigger a function still using a placeholder in logic_utils.py | Function should return real game logic | App crashes / function not implemented | NotImplementedError raised |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
