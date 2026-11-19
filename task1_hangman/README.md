# Task 1: Hangman (Console Game)

A terminal-based Hangman game written in Python 3. The player guesses a
hidden word one letter at a time, with 6 mistakes allowed. An ASCII gallows
is drawn progressively with each wrong guess.

## Features

- Random word chosen from a list of thousands of English words (`words.txt`)
- Built-in backup list of 100 words, used if the file is missing or empty
- ASCII gallows art that updates with each incorrect guess (7 stages)
- Display of the masked word (e.g. `P _ _ _ O _`) and the letters already guessed
- **No duplicate penalty**: guessing the same letter twice shows a message
  but does not cost a life
- Input validation: exactly one character, letters only
- Clean victory and defeat screens
- Option to play again at the end of each game

## Requirements

- Python 3 (3.6 or newer)
- No external libraries: only the standard library (`random`, `pathlib`)

## How to run

From the root of the repository:

```bash
python3 task1_hangman/hangman.py
```

Or from inside the `task1_hangman` folder:

```bash
python3 hangman.py
```

## How it works

The program is split into small functions, each with a single responsibility.

| Function | Role |
|---|---|
| `load_words()` | Reads and filters `words.txt` (letters only, minimum length) |
| `choose_word()` | Picks a random word, falling back to the built-in list |
| `display_word()` | Builds the masked word from the guessed letters |
| `display_gallows()` | Prints the ASCII drawing for the current number of mistakes |
| `ask_letter()` | Asks for a letter and validates it (length, letter, duplicate) |
| `display_victory()` / `display_defeat()` | Print the end-of-game screens |
| `play()` | Runs one complete game |
| `ask_play_again()` | Asks whether to play another game |
| `main()` | Repeats games until the player stops |

### Key design choices

- Guessed letters are stored in a **set**: no duplicates, and fast lookups.
- The game is won when `set(word) <= guessed_letters`, meaning every
  letter of the word has been guessed.
- Duplicates are rejected inside `ask_letter()`, so a repeated letter never
  reaches the game logic and can never cost a life.
