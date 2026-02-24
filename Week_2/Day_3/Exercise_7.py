#


# Instructions:

# Install the faker module and use it to create a list of dictionaries, where each dictionary represents a user with fake data.

# Step 1: Install the faker module

# Step 2: Import the faker module

# Step 3: Create an empty list of users

# Step 4: Create a function to add users

# Create a function that takes the number of users to generate as an argument.
# Inside the function, use a loop to generate the specified number of users.
# For each user, create a dictionary with the keys name, address, and language_code.
# Use the faker instance to generate fake data for each key:
# name: faker.name()
# address: faker.address()
# language_code: faker.language_code()
# Append the user dictionary to the users list.
# Step 5: Call the function and print the users list



from faker import Faker

users = []

fake = Faker()

def generate_fake_users(count):
    for _ in range(count):
        
        user_data = {
            "name": fake.name(),
            "address": fake.address(),
            "language_code": fake.language_code()
        }
        
        users.append(user_data)


generate_fake_users(5)

for user in users:
    print(user)