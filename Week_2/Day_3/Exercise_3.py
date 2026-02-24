
#=============================
# 🌟 Exercise 3: String module
#=============================
# Goal: Generate a random string of length 5 using the string module.
# Instructions:

# Use the string module to generate a random string of length 5, consisting of uppercase and lowercase letters only.

# Step 1: Import the string and random modules
# Import the string and random modules.

# Step 2: Create a string of all letters
# Read about the strings methods HERE to find the best methods for this step

# Step 3: Generate a random string
# Use a loop to select 5 random characters from the combined string.
# Concatenate the characters to form the random string.







import string

print("Lowercase:", string.ascii_lowercase)

print("Uppercase:", string.ascii_uppercase)

import random

pool = string.ascii_letters
random_string = ""

for _ in range(5):
    random_string += random.choice(pool)
    print(f"Random string: {random_string}")