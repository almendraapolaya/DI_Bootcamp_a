
#🌟 Exercise 2: Dogs
# Goal: Create a Dog class with methods for barking, running speed, and fighting.

# Instructions:
# Step 1: Create the Dog Class
# Create a class called Dog with name, age, and weight attributes.
# Implement a bark() method that returns “<dog_name> is barking”.
# Implement a run_speed() method that returns weight / age * 10.
# Implement a fight(other_dog) method that returns a string indicating which dog won the fight, based on run_speed * weight.

# Step 2: Create Dog Instances
# Create three instances of the Dog class with different names, ages, and weights.

# Step 3: Test Dog Methods
# Call the bark(), run_speed(), and fight() methods on the dog instances to test their functionality.

# 🌟 Exercise 2: Dogs
# Your code here

class Dog:
  def __init__(self, name: str, age: int, weight: float):
    self.name = name
    self.age = age
    self.weight = weight

  def bark(self):
     return f"{self.name} is barking"

  def run_speed(self) -> float:
    return (self.weight / self.age) * 10

  def fight(self, other_dog: "Dog"):
    my_speed = self.run_speed()
    their_speed = other_dog.run_speed()
    my_weitght = self.weight
    their_weight = other_dog.weight

    if (my_speed * my_weitght) > (their_speed * their_weight):
      return(f"{self.name} wins!")
    elif (my_speed * my_weitght) < (their_speed * their_weight):
      return(f"{other_dog.name} wins!")
    else:
      return("It's a draw!")


dog1 = Dog("Rex", 4, 20.0)
dog2 = Dog("Bella", 2, 12.0)
dog3 = Dog("Max", 6, 30.0)

print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog2))

