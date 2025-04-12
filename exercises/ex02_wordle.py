"""Creating my very own Wordle"""

__author__: str = "730824316"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    max_turns: int = 6  # max number of tries
    turn: int = 1  # Start from turn 1
    game_won: bool = False  # Track whether the game is won

    while turn <= max_turns and not game_won:  # looping game until reached max turns
        print(f"=== Turn {turn}/{max_turns} ===")  # Display turn count

        guess: str = input_guess(
            len(secret)
        )  # Get user's guess to be lentgh of secret word
        print(emojified(guess, secret))  # Print emoji feedback

        if guess == secret:
            game_won = True  # Player won
        else:
            turn += 1  # Update turn count and move to next turn

    if game_won:
        print(f"You won in {turn}/{max_turns} turns!")
    else:
        print(f"X/{max_turns} - Sorry, try again tomorrow!")


def contains_char(secret_word: str, letter_guessed: str) -> bool:
    """function that verifies guesses"""
    assert len(letter_guessed) == 1, f"len('{letter_guessed}') is not 1"

    idx: int = 0

    while idx < len(
        secret_word
    ):  # ensures that the idx is within the number of letters in secret word
        if secret_word[idx] == letter_guessed:
            return True
        idx += 1  # ensures we eventually stop the while loop
    return False


def emojified(guessed_word: str, secret_word: str) -> str:
    """returns a string of colored boxes based on guesses to prompt the secret word"""
    assert len(guessed_word) == len(secret_word), "Guess must be same length as secret"

    WHITE_BOX: str = "\U00002B1C"  # for letters not in secret word
    GREEN_BOX: str = (
        "\U0001F7E9"  # For letter matching in guess and secret in same index
    )
    YELLOW_BOX: str = "\U0001F7E8"  # for letters in secret but not in correct index

    result: str = ""

    idx: int = 0
    while idx < len(guessed_word):
        if guessed_word[idx] == secret_word[idx]:
            result += GREEN_BOX
        elif contains_char(secret_word, guessed_word[idx]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        idx += 1

    return result


def input_guess(expected_length: int) -> str:
    """Prompts user to guess word of correct length"""
    guess: str = input(
        f"Enter a {expected_length} character word:"
    )  # the variable is assigned a value that is guessed by user

    while len(guess) != expected_length:
        guess = input(
            f"That wasn't {expected_length} chars! Try again:"
        )  # variable is reassigned to eventually have the correct length og guess

    return guess


if __name__ == "__main__":
    main(secret="codes")
