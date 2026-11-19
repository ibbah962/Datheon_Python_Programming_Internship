import random
from pathlib import Path

WORDS_FILE = Path(__file__).parent / "words.txt"
MAX_MISTAKES = 6
BANNER_WIDTH = 30
MIN_WORD_LENGTH = 2

WORDS = [
    "PYTHON", "HANGMAN", "PROGRAMMING", "CHALLENGE", "COMPUTER",
    "ALGORITHM", "KEYBOARD", "VARIABLE", "FUNCTION", "LIBRARY",
    "INTERNET", "NETWORK", "DATABASE", "SOFTWARE", "HARDWARE",
    "MONITOR", "MEMORY", "PROCESSOR", "COMPILER", "DEBUGGER",
    "BROWSER", "SERVER", "CLIENT", "SECURITY", "PASSWORD",
    "ENCRYPTION", "DOWNLOAD", "WEBSITE", "KEYWORD", "SYNTAX",
    "ELEPHANT", "GIRAFFE", "DOLPHIN", "PENGUIN", "KANGAROO",
    "BUTTERFLY", "CROCODILE", "SQUIRREL", "LEOPARD", "OCTOPUS",
    "MOUNTAIN", "RIVER", "FOREST", "DESERT", "ISLAND",
    "VOLCANO", "OCEAN", "WATERFALL", "VALLEY", "GLACIER",
    "CHOCOLATE", "SANDWICH", "PINEAPPLE", "STRAWBERRY", "WATERMELON",
    "SPAGHETTI", "PANCAKE", "BROCCOLI", "AVOCADO", "COCONUT",
    "GUITAR", "PIANO", "VIOLIN", "TRUMPET", "DRUMS",
    "ORCHESTRA", "MELODY", "CONCERT", "SINGER", "RHYTHM",
    "FOOTBALL", "BASKETBALL", "TENNIS", "SWIMMING", "CYCLING",
    "MARATHON", "VOLLEYBALL", "BOXING", "ARCHERY", "SKATING",
    "DOCTOR", "TEACHER", "ENGINEER", "PILOT", "FARMER",
    "ARTIST", "LAWYER", "NURSE", "DENTIST", "JOURNALIST",
    "ADVENTURE", "MYSTERY", "TREASURE", "JOURNEY", "FREEDOM",
    "KNOWLEDGE", "WISDOM", "COURAGE", "FRIENDSHIP", "HAPPINESS",
]

STAGES = [
    # 0 error
    r"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
    # 1 error
    r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    # 2 errors
    r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    # 3 errors
    r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
    # 4 errors
    r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    # 5 errors
    r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    # 6 errors
    r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
"""
]


def load_words():
    """Return the playable words from WORDS_FILE (empty list if file is missing)"""
    words = []
    try:
        with open(WORDS_FILE, encoding="utf-8") as file:
            for line in file:
                candidate = line.strip().upper()
                if candidate.isalpha() and len(candidate) >= MIN_WORD_LENGTH:
                    words.append(candidate)
    except FileNotFoundError:
        pass
    return words


def choose_word():
    """Pick a random word from the file, or from WORDS if the file gives nothing.."""
    words = load_words()
    if not words:
        words = WORDS
    return random.choice(words)


def display_word(word, found_letters):
    """Return the masked word: found letters visible, others replaced by '_'."""
    result = []
    for letter in word:
        if letter in found_letters:
            result.append(letter)
        else:
            result.append("_")
    return " ".join(result)


def display_gallows(mistakes):
    """Print the gallows drawing matching the number of mistakes (0 to 6)."""
    print(STAGES[mistakes])


def ask_letter(guessed_letters):
    """Ask the player for a letter and return it in uppercase.
    It keeps asking until the input is valid (exactly 1 character,
    a letter, and not already guessed).
    """
    while True:
        user_input = input("Please enter a letter: ")
        cleaned_input = user_input.strip().upper()
        if len(cleaned_input) != 1:
            print("Please enter a single letter !")
        elif not cleaned_input.isalpha():
            print("That is not a letter !")
        elif cleaned_input in guessed_letters:
            print("You already tried that letter !")
        else:
            return cleaned_input


def display_victory(word, mistakes):
    """Print the Victory screen."""
    print("=" * BANNER_WIDTH)
    print("YOU WON".center(BANNER_WIDTH))
    print("=" * BANNER_WIDTH)
    print(f"The word was: {word}")
    print(f"Mistakes made: {mistakes}/{MAX_MISTAKES}")
    print("=" * BANNER_WIDTH)


def display_defeat(word):
    """Print the Defeat screen."""
    print("=" * BANNER_WIDTH)
    print("GAME OVER".center(BANNER_WIDTH))
    print("=" * BANNER_WIDTH)
    print(f"The word was: {word}")
    print("Better Luck Next Time !")
    print("=" * BANNER_WIDTH)


def play():
    """Run a complete Hangman game in the terminal."""
    word = choose_word()
    guessed_letters = set()
    mistakes = 0

    print("=== WELCOME TO HANGMAN GAME ===")

    while (mistakes < MAX_MISTAKES) and not (set(word) <= guessed_letters):
        display_gallows(mistakes)
        print("Word :", display_word(word, guessed_letters))
        print("Guessed letters:", ", ".join(sorted(guessed_letters)))
        print("Attempts left:", MAX_MISTAKES - mistakes)

        letter = ask_letter(guessed_letters)
        guessed_letters.add(letter)

        if letter not in word:
            mistakes += 1
            print("Wrong !")
        else:
            print("Good guess !")

    display_gallows(mistakes)
    if set(word) <= guessed_letters:
        display_victory(word, mistakes)
    else:
        display_defeat(word)


def ask_play_again():
    """Ask the player whether to play again. Return True or False."""
    while True:
        answer = input("Do you want to play again ? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        elif answer in ("n", "no"):
            return False
        else:
            print("Please answer y or n")


def main():
    """Run games until the player decides to stop."""
    while True:
        play()
        if not ask_play_again():
            break
    print("Thanks for playing !")


if __name__ == "__main__":
    main()