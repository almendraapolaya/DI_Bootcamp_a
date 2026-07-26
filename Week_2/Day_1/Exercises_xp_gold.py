##=============================
# Exercises XP Gold
##=============================

#==============================
# Exercise 1 : Geometry
#==============================
# Instructions
# Write a class called Circle that receives a radius as an argument (default is 1.0).
# Write two instance methods to compute perimeter and area.
# Write a method that prints the geometrical definition of a circle.


import math

class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    # Method to calculate perimeter (Circumference = 2 * pi * r)
    def perimeter(self):
        return 2 * math.pi * self.radius

    # Method to calculate area (Area = pi * r^2)
    def area(self):
        return math.pi * (self.radius ** 2)

    # Method to print the geometrical definition
    def definition(self):
        print("A circle is a 2D shape formed by all points in a plane that are at a fixed distance (the radius) from a given point (the center).")


# --- Testing the Class ---
if __name__ == "__main__":
    # Test with default radius (1.0)
    c1 = Circle()
    print("=== Default Circle ===")
    print(f"Radius: {c1.radius}")
    print(f"Perimeter: {c1.perimeter():.2f}")
    print(f"Area: {c1.area():.2f}")
    c1.definition()

    print("\n" + "-" * 30 + "\n")

    # Test with a custom radius (5.0)
    c2 = Circle(5.0)
    print("=== Custom Circle (radius = 5.0) ===")
    print(f"Radius: {c2.radius}")
    print(f"Perimeter: {c2.perimeter():.2f}")
    print(f"Area: {c2.area():.2f}")

#===============================
# Exercise 2 : Custom List Class
#===============================
# Instructions
# Create a class called MyList, the class should receive a list of letters.
# Add a method that returns the reversed list.
# Add a method that returns the sorted list.
# Bonus : Create a method that generates a second list with the same length as mylist. The list should be constructed with random numbers. (use list comprehension).

import random

class MyList:
    def __init__(self, letters):
        self.letters = letters

    # Method to return the reversed list without modifying the original
    def get_reversed(self):
        return list(reversed(self.letters))

    # Method to return the sorted list without modifying the original
    def get_sorted(self):
        return sorted(self.letters)

    # Bonus: Generate a random list of integers with the same length as mylist
    def generate_random_list(self, start=1, end=100):
        return [random.randint(start, end) for _ in range(len(self.letters))]


# --- Testing Exercise 2 ---
if __name__ == "__main__":
    sample_letters = ['d', 'a', 'c', 'b', 'e']
    my_custom_list = MyList(sample_letters)

    print("=== Custom List Class Analysis ===")
    print(f"Original List:  {my_custom_list.letters}")
    print(f"Reversed List:  {my_custom_list.get_reversed()}")
    print(f"Sorted List:    {my_custom_list.get_sorted()}")
    
    # Bonus method output
    random_nums = my_custom_list.generate_random_list()
    print(f"Random List:    {random_nums} (Length: {len(random_nums)})")


#==================================
# Exercise 3 : Restaurant Menu Manager
#==================================
# Instructions
# The purpose of this exercise is to create a restaurant menu. 
# The code will allow a manager to add and delete dishes.

class MenuManager:
    def __init__(self):
        # Initial menu data structured as a list of dictionaries
        self.menu = [
            {"name": "Soup", "price": 10, "spice": "B", "gluten": False},
            {"name": "Hamburger", "price": 15, "spice": "A", "gluten": True},
            {"name": "Salad", "price": 18, "spice": "A", "gluten": False},
            {"name": "French Fries", "price": 5, "spice": "C", "gluten": False},
            {"name": "Beef bourguignon", "price": 25, "spice": "B", "gluten": True}
        ]

    # Method to add a new dish to the menu
    def add_item(self, name, price, spice, gluten):
        new_dish = {
            "name": name,
            "price": price,
            "spice": spice,
            "gluten": gluten
        }
        self.menu.append(new_dish)
        print(f" Success: '{name}' has been added to the menu.")

    # Method to update an existing dish
    def update_item(self, name, price, spice, gluten):
        for dish in self.menu:
            if dish["name"].lower() == name.lower():
                dish["price"] = price
                dish["spice"] = spice
                dish["gluten"] = gluten
                print(f" Success: '{name}' has been updated.")
                return
        
        # If loop finishes without returning, dish wasn't found
        print(f" Warning: '{name}' is not in the menu.")

    # Method to remove a dish from the menu
    def remove_item(self, name):
        for dish in self.menu:
            if dish["name"].lower() == name.lower():
                self.menu.remove(dish)
                print(f" Success: '{name}' has been removed from the menu.")
                print("\n--- Updated Menu ---")
                for item in self.menu:
                    print(item)
                return
        
        # If loop finishes without returning, dish wasn't found
        print(f" Warning: '{name}' is not in the menu.")


# === Testing the MenuManager Class ===
if __name__ == "__main__":
    manager = MenuManager()

    print("=== INITIAL MENU ===")
    for item in manager.menu:
        print(item)

    print("\n1. Adding a new item...")
    manager.add_item("Tacos", 12, "C", True)

    print("\n2. Updating an existing item...")
    manager.update_item("Soup", 12, "B", False)

    print("\n3. Trying to update a non-existent item...")
    manager.update_item("Pizza", 20, "A", True)

    print("\n4. Removing an item...")
    manager.remove_item("French Fries")

    print("\n5. Trying to remove a non-existent item...")
    manager.remove_item("Sushi")