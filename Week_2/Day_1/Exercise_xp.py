# 
# Exercises XP
#-----------------------------
#=============================
# Exercise 1: Cats
#=============================
# Instructions:

# Use the provided Cat class to create three cat objects. Then, create a function to find the oldest cat and print its details.

# Step 1: Create Cat Objects
# Use the Cat class to create three cat objects with different names and ages.

# Step 2: Create a Function to Find the Oldest Cat
# Create a function that takes the three cat objects as input.
# Inside the function, compare the ages of the cats to find the oldest one.
# Return the oldest cat object.

# Step 3: Print the Oldest Cat’s Details
# Call the function to get the oldest cat.
# Print a formatted string: “The oldest cat is <cat_name>, and is <cat_age> years old.”
# Replace <cat_name> and <cat_age> with the oldest cat’s name and age.


class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age  = cat_age

cat1 = Cat(cat_name='Fluffy', cat_age=3)
cat2 = Cat('Whiskers', 7)
cat3 = Cat('Mittens', 1)

def find_oldest_cat(cat1: Cat, cat2: Cat, cat3: Cat):
    if cat1.age >= cat2.age and cat1.age >= cat3.age:
      return cat1
    elif cat2.age >= cat1.age and cat2.age >= cat3.age:
      return cat2
    else:
      return cat3

oldest = find_oldest_cat(cat1, cat2, cat3)
print(oldest.name, oldest.age)

#==============================
#Exercise 2 : Dogs
#==============================
# Goal: Create a Dog class, instantiate objects, call methods, and compare dog sizes.

# Instructions:
# Create a Dog class with methods for barking and jumping. Instantiate dog objects, call their methods, and compare their sizes.

# Step 1: Create the Dog Class
# Create a class called Dog.
# In the __init__ method, take name and height as parameters and create corresponding attributes.
# Create a bark() method that prints “<dog_name> goes woof!”.
# Create a jump() method that prints “<dog_name> jumps <x> cm high!”, where x is height * 2.

# Step 2: Create Dog Objects
# Create davids_dog and sarahs_dog objects with their respective names and heights.

# Step 3: Print Dog Details and Call Methods
# Print the name and height of each dog.
# Call the bark() and jump() methods for each dog.

# Step 4: Compare Dog Sizes

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high")

davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Bella", 35)

print(f"David's dog: {davids_dog.name}, {davids_dog.height} cm")
print(f"Sarah's dog: {sarahs_dog.name}, {sarahs_dog.height} cm")
print()

davids_dog.bark()
davids_dog.jump()

sarahs_dog.bark()
sarahs_dog.jump()

print()

if davids_dog.height > sarahs_dog.height:
  print(f"{davids_dog.name} is bigger than {sarahs_dog.name}")
elif sarahs_dog.height > davids_dog.height:
  print(f"{sarahs_dog.name} is bigger than {davids_dog.name}")
else:
  print(f"They are the same size!")

#=====================
#Exercise 3 : Who’s the song producer?
#=====================
# Goal: Create a Song class to represent song lyrics and print them.

# Instructions:

# Create a Song class with a method to print song lyrics line by line.

# Step 1: Create the Song Class
# Create a class called Song.
# In the __init__ method, take lyrics (a list) as a parameter and create a corresponding attribute.
# Create a sing_me_a_song() method that prints each element of the lyrics list on a new line.


class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
          print(line)

stairway = Song([
    "There's a lady who's sure",
    "all that glitters is gold",
    "and she's buying a stairway to heaven"
])

stairway.sing_me_a_song()



# 
#===============================
# 🌟 Exercise 4 : Afternoon at the Zoo
#===============================
# Instructions
# Step 1: Define the Zoo Class
# 1. Create a class called Zoo.

# 2. Implement the __init__() method:
# It takes a string parameter zoo_name, representing the name of the zoo.
# Initialize an empty list called animals to keep track of animal names.

# 3. Add a method add_animal(new_animal):
# This method adds a new animal to the animals list.
# Do not add the animal if it is already in the list.

# 4. Add a method get_animals():
# This method prints all animals currently in the zoo.

# 5. Add a method sell_animal(animal_sold):
# This method checks if a specified animal exists on the animals list and if so, remove from it.

# 6. Add a method sort_animals():
# This method sorts the animals alphabetically.
# It also groups them by the first letter of their name.
# The result should be a dictionary where:
# Each key is a letter.
# Each value is a list of animals that start with that letter.

# 7. Add a method get_groups():
# This method prints the grouped animals as created by sort_animals().

class Zoo:
  def __init__(self, zoo_name):
    self.name = zoo_name
    self.animals = [] 

  def add_animal(self, new_animal):
    if new_animal not in self.animals: 
      self.animals.append(new_animal)

  def get_animals(self):
    print(self.animals)

  def sell_animal(self, animal_sold):
    if animal_sold in self.animals:
      self.animals.remove(animal_sold)

  def sort_animals(self):
    groups = {}

    for animal in sorted(self.animals):
      letter = animal[0]

      if letter not in groups:
        groups[letter] = [] 

      groups[letter].append(animal)

    return groups

  def get_groups(self):
      groups = self.sort_animals()
      for letter, animals in groups.items(): 
        print(f"{letter}: {animals}")


brooklyn_safari = Zoo("Brooklyn Safari")
brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Baboon")
brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.add_animal("Lion")
brooklyn_safari.add_animal("Zebra")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Cat")
brooklyn_safari.add_animal("Cougar")
brooklyn_safari.get_animals()
brooklyn_safari.get_groups()

