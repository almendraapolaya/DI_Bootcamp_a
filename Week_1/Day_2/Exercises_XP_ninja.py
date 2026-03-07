#
#=========================
# Exercises XP Ninja
#=========================
#-------------------------
# Exercise 1: Formula
#-------------------------
# Instructions
# Write a program that calculates and prints a value according to this given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50.
# H is 30.
# Ask the user for a comma-separated string of numbers, use each number from the user as D in the formula and return all the results

import math

C = 50
H = 30

user_input = input("Enter comma-separated values for D: ")
values = user_input.split(',')

results = []

for val in values:
    D = int(val)
    Q = math.sqrt((2 * C * D) / H)

    results.append(str(round(Q)))

print(", ".join(results))


#-------------------------
#Exercise 2 : List of integers
#-------------------------

class ListAnalyzer:
    def __init__(self, data):
        self.data = data

    def basic_stats(self):
        total = 0
        maximum = self.data[0]
        minimum = self.data[0]
        count = 0
        for x in self.data:
            total += x
            count += 1
            if x > maximum: maximum = x
            if x < minimum: minimum = x
        
        avg = total / count
        return total, avg, maximum, minimum

    def get_filtered(self):
        greater_50 = [x for x in self.data if x > 50]
        smaller_10 = [x for x in self.data if x < 10]
        return greater_50, smaller_10

    def get_transformed(self):
        squared = [x**2 for x in self.data]
        unique = list(set(self.data))
        return squared, unique

test_list = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]
analyzer = ListAnalyzer(test_list)
s, a, hi, lo = analyzer.basic_stats()

print(f"Sum: {s}, Avg: {a}, Max: {hi}, Min: {lo}")

#-------------------------
#Exercise 3: Working on a paragraph
#-------------------------
# Find an interesting paragraph of text online. (Please keep it appropriate to the social context of our class.)
# Paste it to your code, and store it in a variable.
# Let’s analyze the paragraph. Print out a nicely formatted message saying:
# How many characters it contains (this one is easy…).
# How many sentences it contains.
# How many words it contains.
# How many unique words it contains.
# Bonus: How many non-whitespace characters it contains.
# Bonus: The average amount of words per sentence in the paragraph.
# Bonus: the amount of non-unique words in the paragraph.

text = """Data analysis is the systematic process of applying statistical and logical techniques 
to describe and illustrate, condense and recap, and evaluate data. It is a crucial component 
of modern decision-making across all industries. By transforming raw numbers into meaningful 
insights, analysts can identify patterns, discover anomalies, and predict future trends."""

cleaned_text = text.replace('.', '').replace(',', '').lower()
words = cleaned_text.split()

char_count = len(text)
non_white_space = len([char for char in text if not char.isspace()]) # Bonus
sentence_count = text.count('.') + text.count('!') + text.count('?')
word_count = len(words)
unique_words = set(words)
unique_count = len(unique_words)

avg_words = word_count / sentence_count if sentence_count > 0 else 0

non_unique_words = [w for w in unique_words if words.count(w) > 1]

print(f"Characters: {char_count}")
print(f"Non-whitespace: {non_white_space}")
print(f"Sentences: {sentence_count}")
print(f"Words: {word_count}")
print(f"Unique words: {unique_count}")
print(f"Non-unique words count: {len(non_unique_words)}")
print(f"Average words per sentence: {avg_words:.2f}")

#-------------------------
#Exercise 4 : Frequency Of The Words
#-------------------------
#Instructions
#Write a program that prints the frequency of the words from the input.

#Suppose the following input is supplied to the program:
#New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.

#Then, the output should be:
#     2:2
#     3.:1
#     3?:1
#     New:1
#     Python:5
#     Read:1
#     and:1
#     between:1
#     choosing:1
#     or:2
#     to:1

user_input = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."

words = user_input.split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

sorted_keys = sorted(frequency.keys())

for key in sorted_keys:
    print(f"{key}:{frequency[key]}")