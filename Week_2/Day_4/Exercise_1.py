#
#=====================================
#Exercise 1: Random Sentence Generator
#=====================================
#Instructions:

# Download the provided word list and save it in your development directory.
# Create a function to read the words from the file.
# Create a function to generate a random sentence of a given length.
# Create a main function to handle user input and program flow.




import random

def get_words_from_file(content):
  with open("words.txt", "r") as f:
    content = f.read()
  return content.split()


def get_random_sentence(length):
  words = get_words_from_file("words.txt")

  chosen = []

  for _ in range(length):
    chosen.append(random.choice(words))

  return " ".join(chosen).lower()

def main():
   length = 0
   try:
     length = int(input("Enter sentence lenght (2-20): "))
   except ValueError:
     print("Invalid Input! Please enter a number.")
     return
   if not (2 < length < 20):
     print("Please enter a number between 2 and 20: ")
     return
   
   sentence = get_random_sentence(length)
   print(f"Generated sentence: {sentence}.")
    


main()