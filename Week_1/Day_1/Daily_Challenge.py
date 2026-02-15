
#===============================================
#   Daily Challenge: Build up a string
#===============================================
# Instructions:
# 1. Ask for User Input:

# The string must be exactly 10 characters long.
# 2. Check the Length of the String:
# If the string is less than 10 characters, print: "String not long enough."
# If the string is more than 10 characters, print: "String too long."
# If the string is exactly 10 characters, print: "Perfect string" and proceed to the next steps.

# 3. Print the First and Last Characters:
# Once the string is validated, print the first and last characters.

# 4. Build the String Character by Character:
# Using a for loop, construct and print the string character by character. Start with the first character, then the first two characters, and so on, until the entire string is printed.
# Hint: You can create a loop that goes through the string, adding one character at a time, and print it progressively.

# Example:

# Alt text

# 5. Bonus: Jumble the String (Optional)
# As a bonus, try shuffling the characters in the string and print the newly jumbled string.
# Hint: You can use the random.shuffle function to shuffle a list of characters.
#

import random
#  1
user_input = input("Hi! Please enter a string of exactly 10 characters: ")
#  2
if len(user_input) < 10:
    print("String not long enough.")
elif len(user_input) > 10:
    print("String too long.")
else:
    print("Perfect string")
    #  3
    print(f"First character: {user_input[0]}")
    print(f"Last character: {user_input[-1]}")
    #  4
    word_loop = ""

    for letter in user_input:
        word_loop += letter
        print(word_loop)
    #  5
    input_to_list = list(user_input)
    random.shuffle(input_to_list)
    new_jumbled_str = "".join(input_to_list)

    print(f"Jumbled string: {new_jumbled_str}")

