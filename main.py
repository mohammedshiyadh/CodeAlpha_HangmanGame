# Hangman in Python

import random
from wordslist import words

# dictionary of key: ()
hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/  "),
               6: (" o ",
                   "/|\\",
                   "/ \\")}


def display_hangman(wrong_guesses):
    """Display the hangman art based on the number of wrong guesses."""
    for line in hangman_art[wrong_guesses]:
        print(line)


def display_hint(hint):
    """Display the current state of the guessed word."""
    print(" ".join(hint))


def display_answer(answer):
    """Display the correct answer."""
    print("The correct answer was: " + answer)


def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True
    while is_running:
        display_hangman(wrong_guesses)
        display_hint(hint)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print(f"You already guessed that letter {guess}.")
            continue

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1
            print(f"Wrong guess! You have {6 - wrong_guesses} guesses left.")
        if "_" not in hint:
            print("Congratulations! You guessed the word.")
            print(wrong_guesses)
            display_answer(answer)
            is_running = False
        elif wrong_guesses >= 6:
            print("Sorry, you lost!")
            display_hangman(wrong_guesses)
            display_answer(answer)
            is_running = False


if __name__ == "__main__":
    main()
