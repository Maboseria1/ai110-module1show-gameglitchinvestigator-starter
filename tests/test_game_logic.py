from logic_utils import check_guess


def test_winning_guess():
    # If the secret is 50 and the guess is 50, it should be a win.
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high_says_go_lower():
    # Guess (60) is higher than the secret (50).
    # Outcome should be "Too High" and the hint should tell the player to go LOWER.
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "lower" in message.lower()


def test_guess_too_low_says_go_higher():
    # Guess (40) is lower than the secret (50).
    # Outcome should be "Too Low" and the hint should tell the player to go HIGHER.
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "higher" in message.lower()
