# 🎮 Hangman Game – Python

A console-based Hangman word-guessing game developed using Python as part of the **CodeAlpha Python Programming Internship**.

The game randomly selects a word from a predefined collection. The player guesses one letter at a time and has up to six incorrect guesses to reveal the word.

## Features

- Random word selection from a large word collection
- Hidden-word display using underscores
- ASCII Hangman illustration
- Maximum of six incorrect guesses
- Single-letter input validation
- Repeated-guess detection
- Win and loss conditions
- Displays the correct word when the game ends

## Technologies and Concepts

- **Language:** Python 3
- **Standard library:** `random`
- **Python concepts:** functions, loops, conditionals, strings, lists, tuples, sets, and input validation

## Project Structure

```text
CodeAlpha_HangmanGame/
├── main.py          # Main game logic
├── wordslist.py     # Predefined word collection
└── README.md        # Project documentation
```

## Getting Started

### Requirements

- Python 3.x
- No third-party packages are required.

### Run the game

1. Clone this repository:

   ```bash
   git clone https://github.com/mohammedshiyadh/CodeAlpha_HangmanGame.git
   ```

2. Open the project directory:

   ```bash
   cd CodeAlpha_HangmanGame
   ```

3. Start the game:

   ```bash
   python main.py
   ```

   On some systems, use `python3 main.py` instead.

## How to Play

1. Start the game.
2. The program selects a word at random.
3. Enter one letter per turn.
4. Correct guesses reveal matching letters in the word.
5. Incorrect guesses add a part to the Hangman drawing.
6. Guess the complete word before reaching six incorrect guesses to win.

## Learning Outcomes

This project provides practice with:

- Selecting random items from a collection
- Managing game state with variables and loops
- Using sets to track previously guessed letters
- Validating user input
- Breaking a program into reusable functions

## Internship

**CodeAlpha – Python Programming Internship**

## Author

**Mohammed Shiyadh S**

B.Tech – Artificial Intelligence and Data Science
