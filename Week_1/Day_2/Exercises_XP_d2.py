#Exercises XP
#-----------------
#=========================================================================
#Exercise 1: Favorite Numbers
#=========================================================================

# Key Python Topics:
# Sets
# Adding/removing items in a set
# Set concatenation (using union)

# Instructions:
#--------------------------------------------------------------------------
# Create a set called my_fav_numbers and populate it with your favorite numbers.
# Add two new numbers to the set.
# Remove the last number you added to the set.
# Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
# Note: Sets are unordered collections, so ensure no duplicate numbers are added.

my_fav_numbers = {2, 15, 13, 24, 31}
my_fav_numbers.add(14)
my_fav_numbers.add(50)

my_fav_numbers.discard(50)
print(my_fav_numbers)

friend_fav_numbers = {1, 3, 4, 5}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print(our_fav_numbers)

#============================================================================
#  Exercise 2: Tuple
#============================================================================

# Key Python Topics:
# Tuples (immutability)

# Instructions:
# Given a tuple of integers, try to add more integers to the tuple.
# Hint: Tuples are immutable, meaning they cannot be changed after creation. Think about why you can’t add more integers to a tuple.

my_tuple = (1, 2, 3)
#You cannot add more items to a tuple once is created even using append() or add()
#my_tuple.append(4)

#print(my_tuple) # You get an AttributeError

#============================================================================
#  Exercise 3: List Manipulation
#============================================================================
# Key Python Topics:
# Lists
# List methods: append, remove, insert, count, clear

# Instructions:

# You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# Remove "Banana" from the list.
# Remove "Blueberries" from the list.
# Add "Kiwi" to the end of the list.
# Add "Apples" to the beginning of the list.
# Count how many times "Apples" appear in the list.
# Empty the list.
# Print the final state of the list.

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
apples_count = basket.count("Apples")

print(apples_count)
basket.clear()

print(basket)

#=============================================================================
# Exercise 4: Floats
#=============================================================================
# Key Python Topics:

# Lists
# Floats and integers
# Range generation

# Instructions:

# Recap: What is a float? What’s the difference between a float and an integer?
# A float is number with decimals and Integer whole numbers

# Create a list containing the following sequence of mixed types: floats and integers:
# 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5
# Avoid hard-coding each number manually.
# Think: Can you generate this sequence using a loop or another method?

num_list = []
base = 1.5

while base <= 5:
    num_list.append(base)
    base = base + 0.5

print(num_list)

#==============================================================================
#Exercise 5: For Loop
#==============================================================================
# Key Python Topics:

# Loops (for)
# Range and indexing


# Instructions:

# Write a for loop to print all numbers from 1 to 20, inclusive.
# Write another for loop that prints every number from 1 to 20 where the index is even.

for n in range(1, 21):
    print(n)

for n in range(1, 21, 2):
    print(n)

#===============================================================================
# Exercise 6: While Loop
#===============================================================================
# Key Python Topics:

# Loops (while)
# Conditionals

# Instructions:

# Use an input to ask the user to enter their name.
# Using a while True loop, check if the user gave a proper name (not digits and at least 3 letters long)
# hint: check for the method isdigit()
# if the input is incorrect, keep asking for the correct input until it is correct
# if the input is correct print “thank you” and break the loop

user_name = input("Enter your name: ")

while True:
    if not user_name.isdigit() and len(user_name) >= 3:
        print("Thank you!")
        break
    else:
        user_name = input("Give the correct name: ")
    
#=============================================================================
#  Exercise 7: Favorite Fruits
#=============================================================================
# Key Python Topics:

# Input/output
# Strings and lists
# Conditionals


# Instructions:

# Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
# Store these fruits in a list.
# Ask the user to input the name of any fruit.
# If the fruit is in their list of favorite fruits, print:
# "You chose one of your favorite fruits! Enjoy!"
# If not, print:
# "You chose a new fruit. I hope you enjoy it!"  

user_fruits = input("Type your favorite fruits(separated by spaces): ")

user_fruits = user_fruits.lower().split()

choice = input("Enter the name of any fruit: ").lower()

if choice in user_fruits:
    print("You choose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit.I hope you enjoy it!")

#=============================================================================
# Exercise 8: Pizza Toppings
#=============================================================================
# Key Python Topics:

# Loops
# Lists
# String formatting


# Instructions:

# Write a loop that asks the user to enter pizza toppings one by one.
# Stop the loop when the user types 'quit'.
# For each topping entered, print:
# "Adding [topping] to your pizza."
# After exiting the loop, print all the toppings and the total cost of the pizza.
# The base price is $10, and each topping adds $2.50.

toppings = []
base_price = 10
topping_price = 2.50

while True:
    topping = input("Please enter a topping (or 'quit' to finish): ").lower()

    if topping == 'quit':
        break
    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")

total_cost = base_price + (len(toppings) * topping_price)

print(f"Your toppings: {', '.join(toppings)}")
print(f"Total price: ${total_cost:.2f}")

#=================================================================================
# Exercise 9: Cinemax Tickets
#=================================================================================
# Key Python Topics:

# Conditionals
# Lists
# Loops


# Instructions:

# Ask for the age of each person in a family who wants to buy a movie ticket.
# Calculate the total cost based on the following rules:
# Free for people under 3.
# $10 for people aged 3 to 12.
# $15 for anyone over 12.
# Print the total ticket cost.

total_cost = 0

print("Hi! Please enter the ages of your family members one by one. Type 'done' when finished.")

while True:
    age_client = input("Enter age: ").lower()
    
    if age_client == 'done':
        break
    
    age = int(age_client)
    
    if age < 3:
        price = 0
        print("The ticket is free!")
    elif 3 <= age <= 12:
        price = 10
        print("The ticket is $10.")
    else:
        price = 15
        print("The ticket is $15.")
        
    total_cost += price

print(f"\nThe total cost for your family is: ${total_cost}")

#=================================================================================
# Bonus:
#=================================================================================
# Imagine a group of teenagers wants to see a restricted movie (only for ages 16–21).
# Write a program to:
# Ask for each person’s age.
# Remove anyone who isn’t allowed to watch.
# Print the final list of attendees.

input_clients = input("Please enter the ages separated by dashes (e.g 15-20-22) to know if you are allow to see the movie: ")

age_strings = input_clients.split("-")
allowed_attendees = []

for age_str in age_strings:
    
    age = int(age_str)
    
    if 16 <= age <= 21:
        allowed_attendees.append(age)
        print(f"Age {age} is allowed.")
    else:
        print(f"Age {age} is restricted and removed.")

print(f"\nFinal list of attendees: {allowed_attendees}")

