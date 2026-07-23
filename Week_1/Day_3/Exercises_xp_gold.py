#####################
# Exercises XP Gold
####################

#===========================
# Exercise 1: Birthday Look-up
#===========================
# 1. Create a dictionary with 5 birthdays
birthdays = {
    "Almendra": "1993/10/02",
    "Itay": "1990/03/31",
    "Lancelot": "2019/10/15",
    "Julia": "2011/12/05",
    "Ester": "2003/05/21"
}

# 2. Print welcome message and instructions
print("Welcome to the Birthday Look-up App!")
print("You can look up the birthdays of the people in the list!\n")

# Display available names so the user knows who to ask about
print("Available names:", ", ".join(birthdays.keys()))

# 3. Ask the user for a name and store it
user_choice = input("Whose birthday do you want to look up? ").strip()

#  Get the birthday and print it formatted
if user_choice in birthdays:
    birthday = birthdays[user_choice]
    print(f"\n Great! {user_choice}'s birthday is on {birthday}.")
else:
    print(f"\n Sorry, we don't have birthday information for '{user_choice}'.")
print("\n")
print("\n")

#============================
# Exercise 2: Birthdays Advanced
#============================

# Initial birthdays dictionary
birthdays_ex2 = {
    "Alice": "1995/04/12",
    "Bob": "1990/11/23",
    "Charlie": "1988/07/04",
    "Dana": "2001/01/15",
    "Eli": "1998/09/30"
}

# 1. Print welcome message
print("=== Welcome to the Birthday Look-up App Version 2 ===")
print("You can look up the birthdays of the people in the list!\n")

# 2. Print out ALL names in the dictionary before asking for input
print("Here are all the people in our system:")
for name in birthdays_ex2.keys():
    print(f"- {name}")

print("-" * 35)

# 3. Prompt user for input
search_name = input("Enter a person's name to look up their birthday: ").strip()

# 4. Check if the name exists and print output or error message
if search_name in birthdays_ex2:
    print(f"\n Success: {search_name}'s birthday is {birthdays_ex2[search_name]}.")
else:
    print(f"\n Sorry, we don't have the birthday information for {search_name}.")

print("\n")
print("\n")
#======================
# Exercise 3: Add Your Own Birthday
#======================

birthdays_ex3 = {
    "Fiona": "1993/03/14",
    "George": "1985/10/28",
    "Hannah": "1997/06/05",
    "Ian": "2002/12/19",
    "Julio": "1991/08/22"
}

print("=== Welcome to Exercise 3: Add Your Own Birthday ===")

# 1 & 2. Add your own birthday
print("First, let's add a new birthday to our record!")
new_name_ex3 = input("Enter the person's name: ").strip()
new_birthday_ex3 = input("Enter their birthday (YYYY/MM/DD): ").strip()

# 3. Add new entry into birthdays_ex3
birthdays_ex3[new_name_ex3] = new_birthday_ex3
print(f" Saved! {new_name_ex3} has been added.\n")

# Display updated list of names
print("Here are all available people in Exercise 3:")
for name in birthdays_ex3.keys():
    print(f"- {name}")

print("-" * 35)

# 4. Look up a birthday
search_name_ex3 = input("Whose birthday do you want to look up? ").strip()

if search_name_ex3 in birthdays_ex3:
    print(f"\n Success: {search_name_ex3}'s birthday is {birthdays_ex3[search_name_ex3]}.")
else:
    print(f"\n Sorry, we don't have the birthday information for {search_name_ex3}.")
print("\n")