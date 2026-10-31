# 🎮 Hangman Game – Python

A simple, interactive, console-based Hangman word guessing game developed using Python as part of the **CodeAlpha Python Programming Internship**.

The game randomly selects a word from a predefined collection of words. Players must guess the hidden word one letter at a time before running out of attempts.

## ✨ Features

* 🎲 Random word selection from a large word collection.
* 🔤 Hidden word display with underscores.
* 💀 ASCII-based Hangman visual representation.
* ❤️ Maximum of 6 incorrect guesses.
* 🔍 Real-time letter guessing.
* ✅ Input validation to prevent invalid entries.
* 🔄 Repeated guess detection.
* 🏆 Win and lose conditions.
* 📢 Displays the correct answer when the game ends.

## 🛠️ Technologies Used

* **Language:** Python
* **Module:** Random
* **Concepts:**

  * Variables and Data Types
  * Lists and Tuples
  * Sets
  * Functions
  * Loops
  * Conditional Statements
  * String Manipulation
  * User Input Validation

## 📁 Project Structure

```text
CodeAlpha_HangmanGame/
│
├── main.py       # Main game logic
├── wordslist.py     # Collection of predefined words
└── README.md        # Project documentation
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/CodeAlpha_HangmanGame.git
```

### 2. Navigate to the project directory

```bash
cd CodeAlpha_HangmanGame
```

### 3. Run the game

```bash
python hangman.py
```

**Requirements:** Python 3.x

No external libraries are required.

## 🎯 How to Play

1. Run the Python program.
2. The computer randomly selects a secret word.
3. The word is displayed as underscores.
4. Enter one letter at a time to guess the word.
5. Correct guesses reveal the corresponding letters.
6. Incorrect guesses reduce your remaining attempts.
7. You have a maximum of 6 incorrect guesses.
8. Guess the complete word to win!

## 🖥️ Example Gameplay

```text
      HANGMAN

      o
     /|\
     /

_ _ _ _ _ _

Guess a letter: p

Wrong guess! You have 5 guesses left.

Guess a letter: y

_ y _ _ _ _

Congratulations! You guessed the word.
```

*Example output for illustration.*

## 📚 Learning Outcomes

Through this project, I practised:

* Implementing random word selection.
* Working with Python collections.
* Managing game states using loops and conditions.
* Creating reusable functions.
* Validating user inputs.
* Implementing basic game logic.

## 👨‍💻 Author

**Mohammed Shiyadh S**

B.Tech – Artificial Intelligence and Data Science

## 📌 Internship

Developed as part of the **CodeAlpha Python Programming Internship**.

---

⭐ If you find this project interesting, feel free to explore the repository!
