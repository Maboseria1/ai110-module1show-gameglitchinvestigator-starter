# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

An AI built a simple "Number Guessing Game" using Streamlit, but it shipped the code full of bugs and left it nearly unplayable. The starting problems were:

- The hints were backwards, so following them made you lose.
- The attempts counter started one too low.
- The secret number seemed to change between guesses, and "New Game" didn't fully reset things.

This project was about investigating those glitches and fixing them. I fixed the backwards hints and the attempts counter, refactored `check_guess` into `logic_utils.py`, and added pytest tests for the game logic (see the sections below). Some of the other reported issues (like the secret changing on certain guesses, "New Game" not fully resetting, and the difficulty range) are still on my list and not fully fixed yet, so I'm not claiming those.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `python -m streamlit run app.py`
3. Run the tests: `pytest`

## 🕵️‍♂️ The Debugging Tasks

These were the tasks I worked through to investigate and fix the game (they describe the assignment, not the game's current behavior):

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number and try to win.
2. **Investigate the state bug.** Look into why the secret number can seem to change between guesses in Streamlit. *(Still investigating — not fully fixed yet.)*
3. **Fix the logic.** The "Higher/Lower" hints were wrong. ✅ Fixed.
4. **Refactor & test.** Move the logic into `logic_utils.py` and run `pytest`. ✅ Refactored `check_guess` and added passing tests.

## 📝 Document Your Experience

- [x] Describe the game's purpose.
- [x] Detail which bugs you found.
- [x] Explain what fixes you applied.

**Purpose:** This is a simple Streamlit number guessing game. The app picks a secret number based on the difficulty you choose, and you try to guess it within a limited number of attempts. After each guess it gives you a hint (go higher or go lower) and tracks your attempts and score.

**Bugs I found:** The high/low hints were backwards (guessing too high told me to "Go HIGHER!" and too low told me to "Go LOWER!"). The attempts counter started one too low, so on Normal difficulty it said 7 attempts left before I had even guessed once, even though 8 are allowed. The game logic was also still sitting inside `app.py` instead of being refactored into `logic_utils.py`, where the functions were just placeholders raising `NotImplementedError`.

**Fixes I applied:**
- Fixed the backwards high/low hints so "Too High" tells the player to go LOWER and "Too Low" tells them to go HIGHER.
- Fixed the attempts counter so the game starts at 0 attempts and Normal difficulty correctly shows 8 attempts left before the first guess.
- Refactored `check_guess` out of `app.py` and into `logic_utils.py`.
- Added pytest tests for the game logic in `tests/test_game_logic.py`.

## Demo Walkthrough

Here is a text-based walkthrough of a sample game on Normal difficulty (secret number is 50, 8 attempts allowed). No screenshot or video needed — you can follow the flow just by reading.

1. **Start the game.** The app shows "Attempts left: 8" before I make any guess, which is correct now that the counter starts at 0.
2. **Guess too low.** I enter `30`. Since 30 is lower than the secret (50), the hint says "📈 Go HIGHER!" and attempts left drops to 7.
3. **Guess too high.** I enter `70`. Since 70 is higher than the secret (50), the hint says "📉 Go LOWER!" and attempts left drops to 6.
4. **Guess correctly.** Using the hints, I enter `50`. The game says "🎉 Correct!" and I win.
5. **Attempts update correctly.** Throughout the game the "Attempts left" number counts down by one with each guess, instead of starting one too low like it used to.

## 🧪 Test Results

```
============================= test session starts ==============================
collected 3 items

tests/test_game_logic.py::test_winning_guess PASSED
tests/test_game_logic.py::test_guess_too_high_says_go_lower PASSED
tests/test_game_logic.py::test_guess_too_low_says_go_higher PASSED

============================== 3 passed in 0.02s ==============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
