#================================
#     Mini-Project #2 - Hangman
#================================

# What you will create
# Use python to create a Hangman game.

# Instructions
# The computer choose a random word and mark stars for each letter of each word.
# Then the player will guess a letter.
# If that letter is in the word(s) then the computer fills the letter in all the correct positions of the word.
# If the letter isn’t in the word(s) then add a body part to the gallows (head, body, left arm, right arm, left leg, right leg).
# The player will continue guessing letters until they can either solve the word(s) (or phrase) or all six body parts are on the gallows.
# The player can’t guess the same letter twice.

import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist) 

guessed_letters = []
wrong_guesses = 0
max_attempts = 6

display_word = []
for letter in word:
    if letter == " ":
        display_word.append(" ")
    else:
        display_word.append("*")

print("Welcome to Hangman!")

while wrong_guesses < max_attempts and "*" in display_word:
    print(f"\nWord: {''.join(display_word)}")
    print(f"Attempts left: {max_attempts - wrong_guesses}")
    print(f"Guessed so far: {', '.join(guessed_letters)}")
    
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print(">> Please enter a single valid letter.")
        continue
    
    if guess in guessed_letters:
        print(f">> You already guessed '{guess}'. Try again!")
        continue
    
    guessed_letters.append(guess)

    if guess in word:
        print(f"Good job! '{guess}' is in the word.")
        
        for index in range(len(word)):
            if word[index] == guess:
                display_word[index] = guess
    else:
        wrong_guesses += 1
        print(f"Sorry, '{guess}' is not there. A body part is added to the gallows!")

if "*" not in display_word:
    print(f"\nCongratulations! You saved the hangman! The word was: {word}")
else:
    print(f"\nGame Over! The hangman is complete. The word was: {word}")