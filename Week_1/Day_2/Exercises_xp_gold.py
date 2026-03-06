#================================
# Exercises XP Gold
#================================
#--------------------------------
# Exercise 1: Concatenate lists
#--------------------------------
# Instructions
# Write code that concatenates two lists together without using the + sign.

list_1 = ['apple', 'orange', 'banana']
list_2 = ['kiwi', 'grape']

list_1.extend(list_2)

print(list_1)

#--------------------------------
# Exercise 2: Range of numbers
#--------------------------------
# Instructions
# Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.

multiples_of_5 = []
multiples_of_7 = []

for num in range(1500, 2501):

    if num % 5 == 0:
        multiples_of_5.append(num)

    if num % 7 == 0:
        multiples_of_7.append(num)

print(f"Multiples of 5 between 1500 to 2500: {multiples_of_5}")
print(f"Multiples of 7 between 1500 to 2500: {multiples_of_7}")


#---------------------------------
# Exercise 3: Check the index
#---------------------------------
# Instructions
# Using this variable
# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
# Ask a user for their name, if their name is in the names list print out the index of the first occurence of the name.
# Example: if input is 'Cortana' we should be printing the index 1


names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

user_input = input("Please type your name: ").capitalize()

for index, item in enumerate(names):
    if user_input == item:
        print(f"Index: {index}")
        break
    else:
        print("The name you enter is not in the list")
        break

#---------------------------------
#Exercise 4: Greatest Number
#---------------------------------
#Instructions
#Ask the user for 3 numbers and print the greatest number.
#Test Data
#Input the 1st number: 25
#Input the 2nd number: 78
#Input the 3rd number: 87
#The greatest number is: 87

numbers = [
int(input("Please type your first number: ")),
int(input("Please type your second number: ")),
int(input("Please type your third number: "))
]
    
print(f"The greatest number is: {max(numbers)}")

#---------------------------------
#Exercise 5: The Alphabet
#---------------------------------
#  Instructions
# Create a string of all the letters in the alphabet
#  Loop over each letter and print a message that contains the letter and whether its a vowel or a consonant.

alphabet = "abcdefghijklmnopqrstuvwxyz"

vowels = "aeiou"

for letter in alphabet:
    if letter in vowels:
        print(f"{letter} is a vowel")
    else:
        print(f"{letter} is a consonant")
        
# ---------------------------------
# Exercise 6: Words and letters
# ---------------------------------
# Instructions
# Ask a user for 7 words, store them in a list named words.
# Ask the user for a single character, store it in a variable called letter.
# Loop through the words list and print the index of the first appearence of the letter variable in each word of the list.
# If the letter doesn’t exist in one of the words, print a friendly message with the word and the letter.

user_input = input("Type 7 words separated by commas): ")

raw_word = user_input.split(",")

words = []
for w in raw_word:
    words.append(w.strip())

letter = input("Enter a single character to search for: ")

for word in words:
    index = word.find(letter)
    if index != -1:
        print(f"In the word '{word}', '{letter}' is at index {index}")
    else:
        print(f"The letter '{letter}' is not in '{word}'.")

#---------------------------------
# Exercise 7: Min, Max, Sum
#---------------------------------
# Instructions
# Create a list of numbers from one to one million and then use min() and max() to make sure your list actually starts at one and ends at one million. Use the sum() function to see how quickly Python can add a million numbers.


numbers = list(range(1, 1000001))

print(f"Minimum: {min(numbers)}")
print(f"Maximum: {max(numbers)}")

total_sum = sum(numbers)
print(f"Sum: {total_sum}")

#---------------------------------
#Exercise 8 : List and Tuple
#---------------------------------
# Instructions
# Write a program which accepts a sequence of comma-separated numbers. Generate a list and a tuple which contain every number.
# Suppose the following input is supplied to the program: 34,67,55,33,12,98


user_input = input("Enter a sequence of comma-separated numbers: ")

numbers_list = user_input.split(",")

numbers_tuple = tuple(numbers_list)

print(numbers_list)
print(numbers_tuple)

#---------------------------------
#Exercise 9 : Random number
#---------------------------------
# Instructions
# Ask the user to input a number from 1 to 9 (including).
# Get a random number between 1 and 9. Hint: random module.
# If the user guesses the correct number print a message that says Winner.
# If the user guesses the wrong number print a message that says better luck next time.
# Bonus: use a loop that allows the user to keep guessing until they want to quit.
# Bonus 2: on exiting the loop tally up and display total games won and lost.

import random

wins = 0
losses = 0

print("--- Welcome to the Guessing Game! ---")
print("Enter a number between 1 and 9, or type 'quit' to exit.")

while True:
    user_input = input("\nYour guess: ").lower()

    if user_input == 'quit':
        break

    if not user_input.isdigit():
        print("Please enter a valid number or 'quit'.")
        continue

    guess = int(user_input)

    if guess < 1 or guess > 9:
        print("Remember, the number is between 1 and 9!")
        continue

    secret_number = random.randint(1, 9)
    print(f"The secret number was: {secret_number}")

    if guess == secret_number:
        print("Winner!")
        wins += 1
    else:
        print("Better luck next time.")
        losses += 1

print("\n" + "="*20)
print("GAME OVER")
print(f"Total Wins: {wins}")
print(f"Total Losses: {losses}")
print("="*20)