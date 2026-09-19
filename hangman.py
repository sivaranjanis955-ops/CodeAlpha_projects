
import random

words = ["python", "java", "computer", "programming", "developer"]

word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("=== Hangman Game ===")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.")

while wrong_guesses < max_wrong_guesses:
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter only.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess! Incorrect guesses:",
              wrong_guesses, "/", max_wrong_guesses)

else:
    print("\nGame Over!")
    print("The word was:", word)