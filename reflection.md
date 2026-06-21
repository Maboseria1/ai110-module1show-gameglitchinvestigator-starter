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

I used Claude Code and ChatGPT as my AI teammates on this project. One suggestion that was correct came from Claude, which explained that the backwards hints were caused by the message text being paired with the wrong outcome inside `check_guess` (so "Too High" was returning the "go higher" message). I verified this by running the Streamlit app and using the Developer Debug Info to see the secret number, then comparing it to my guesses to confirm the hints pointed the right way after the fix. The misleading part was not one single wrong line of code but more of a behavior risk: AI tends to want to fix many bugs at once, which could have introduced new problems I did not ask for. To handle that, I kept my prompts focused on one bug at a time and reviewed the diff before accepting any change, instead of trusting the AI to rewrite everything safely.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided a bug was really fixed by testing it in two ways: manually in the running app and with automated tests. For the hint bug, I used Claude Code to refactor `check_guess` out of `app.py` into `logic_utils.py`, reviewed the diff before accepting it, and then played the game while checking the secret in Developer Debug Info to confirm the hints finally pointed the correct direction. I also fixed the attempts counter so the game starts at 0 attempts and Normal difficulty correctly shows 8 attempts left before the first guess. To back this up, I used Claude Code to create pytest tests in `tests/test_game_logic.py` that check a winning guess returns `"Win"`, a high guess returns `"Too High"` and tells the player to go lower, and a low guess returns `"Too Low"` and tells the player to go higher. AI helped me design these tests by suggesting the cases to cover, and running pytest gave me 3 passing tests, which made me confident the logic was actually correct and not just looking right in one playthrough.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

The biggest thing I learned is that Streamlit reruns the whole script from top to bottom every time the user interacts with the app, like clicking a button or typing in a box. That means normal variables get recreated each time, so they cannot remember anything between interactions on their own. To fix that, Streamlit gives you `st.session_state`, which is like a little storage box that survives across reruns. In this game, `st.session_state` is what lets the app remember the secret number, the attempts, the score, the status, and the guess history instead of resetting them every time I click "Submit." Once I understood that reruns happen constantly, a lot of the "the secret keeps changing" type of confusion started to make more sense.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to keep is making small, focused commits and asking AI to fix one bug at a time instead of letting it rewrite everything at once. Working bug-by-bug made it way easier to see what changed and to back out if something went wrong, and I also want to keep reviewing the diffs and testing my changes before I commit them. One thing I would do differently next time is ask the AI to explain its plan first before it starts editing, so I understand the approach instead of just trusting the code it spits out. The biggest mindset shift is that this project showed me AI-generated code can look completely correct while still having hidden logic bugs, like the backwards hints that "ran" fine but were wrong. Because of that, I now treat AI as a teammate whose work I still have to verify myself rather than something I can copy and trust blindly.
