#---------------------------------------------------------------
# Exercises XP
#---------------------------------------------------------------
#===============================================================
# Exercise 1: Converting Lists into Dictionaries
#===============================================================
# Key Python Topics:

# Creating dictionaries
# Zip function or dictionary comprehension


# Instructions
# You are given two lists. Convert them into a dictionary where the first list contains the keys and the second list contains the corresponding values.

# Lists:
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# # Expected Output:
# # {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

new_dict = dict(zip(keys, values))

print(new_dict)

# #============================================================
# # Exercise 2: Cinemax #2
# #============================================================

# # Key Python Topics:

# # Looping through dictionaries
# # Conditionals
# # Calculations

# # Instructions
# # Write a program that calculates the total cost of movie tickets for a family based on their ages.

# # Family members’ ages are stored in a dictionary.
# # The ticket pricing rules are as follows:
# # Under 3 years old: Free
# # 3 to 12 years old: $10
# # Over 12 years old: $15

# # Family Data:
# # family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# # Loop through the family dictionary to calculate the total cost.
# # Print the ticket price for each family member.
# # Print the total cost at the end.



family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_cost = 0

for name, age in family.items():
    if age < 3:
        price = 0
        print(f"{name} the price for you is: {price}")
    elif 3 <= age <= 12:
        price = 10
        print(f"{name} the price for you is: {price}")
    else:
        price = 15
        print(f"{name} the price for you is: {price}")
        
    total_cost += price

print(f"\nTotal cost for the tickets: ${total_cost}")

#---------------------------------------------------------------
# # Bonus:
# # Allow the user to input family members’ names and ages, then calculate the total ticket cost.
#---------------------------------------------------------------

total_price = 0

while True:
    family_input = input("For a ticket, please enter you name.Type 'done' when finished: ").lower()

    if family_input == 'done':
        break
     
    age_client_input = input(f"Hi {family_input.capitalize()}, Please type your age: ")
    age = int(age_client_input)

    if age < 3:
        prices = 0
    elif 3 <= age <= 12:
        prices = 10
    else:
        prices = 15
    
    print(f"{family_input.capitalize()}, the price for you is: $ ")
    total_price += prices

print(f"\nTotal cost for the tickets: ${total_price}")

#==============================================================
#  Exercise 3: Zara
#==============================================================
# Key Python Topics:

# Creating dictionaries
# Accessing and modifying dictionary elements
# Dictionary methods like .pop() and .update()


# Instructions
# Create and manipulate a dictionary that contains information about the Zara brand.

# Brand Information:

# name: Zara
# creation_date: 1975
# creator_name: Amancio Ortega Gaona
# type_of_clothes: men, women, children, home
# international_competitors: Gap, H&M, Benetton
# number_stores: 7000
# major_color: 
#     France: blue, 
#     Spain: red, 
#     US: pink, green


# Create a dictionary called brand with the provided data.
# Modify and access the dictionary as follows:
#  1 -Change the value of number_stores to 2.
#  2 -Print a sentence describing Zara’s clients using the type_of_clothes key.
#  3 -Add a new key country_creation with the value Spain.
#  4 -Check if international_competitors exists and, if so, add “Desigual” to the list.
#  5 -Delete the creation_date key.
#  6 -Print the last item in international_competitors.
#  7 -Print the major colors in the US.
#  8 -Print the number of keys in the dictionary.
#  9 -Print all keys of the dictionary.


brand = {
    'name': 'Zara',
    'creation_date': 1975,
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors':['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000,
    'major_color': {'France': 'blue', 'Spain': 'red', 'US': ['pink', 'green']}
    }

original_brand = brand.copy()

brand['number_stores'] = 2                                      # 1

clothes = ", ".join(brand['type_of_clothes'])
print(f"Zara have clothes for: {clothes}")                      # 2 

brand['country_creation'] = 'Spain'                             # 3  

brand['international_competitors'].append('Uniqlo')             # 4 

del brand['creation_date']                                      # 5

print(brand['international_competitors'][-1])                   # 6 

print(brand.get('major_color'))                                 # 7 

print(len(brand.keys()))                                        # 8 

print(brand.keys())                                             # 8 

#-------------------
# Bonus:
#-------------------
# Create another dictionary called more_on_zara with creation_date and number_stores. Merge this dictionary with the original brand dictionary and print the result.

more_on_zara = {'creation_date': 1975, 'number_stores': 7000}
merge_zara ={**original_brand, **more_on_zara}
print(merge_zara)                                         

#==============================================================
#Exercise 4: Disney Characters
#==============================================================
# Key Python Topics:

# Looping with indexes
# Dictionary creation
# Sorting

# Instructions
# You are given a list of Disney characters. Create three dictionaries based on different patterns as shown below:

# Character List:

# users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# Expected Results:
# 1. Create a dictionary that maps characters to their indices:
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

# 2. Create a dictionary that maps indices to characters:
# {0: "Mickey", 1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

# 3. Create a dictionary where characters are sorted alphabetically and mapped to their indices:
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
# 1
new_dict ={}

for index, item in enumerate(users):
    new_dict[item] = index

print(new_dict)
# 2
dict_char = {}


for index, item in enumerate(users):
    dict_char[index] = item

print(dict_char)

# 3

users.sort()
sorted_users ={}
for index, item in enumerate(users):
    sorted_users[item] = index

print(sorted_users)

