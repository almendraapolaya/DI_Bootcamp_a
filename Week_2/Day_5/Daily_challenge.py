# ---------------------------------
# Daily Challenge
# ---------------------------------
# =================================
# Exercise 1: Quizz
# =================================
# Answer the following questions:

# What is a class?
# ---------------------------------
# Is a blueorint or template for creating objetcs.
# It defines the attibutes(data) and methods(behaviors) they will have.

# What is an instance?
# ---------------------------------
# An instance is a specific object created from a class.
# If "Car" is the class, "Your red Toyota" is an instance.
#
# What is encapsulation?
# ---------------------------------
# Bundling data and methods together and restricting direct access to some components.

# What is abstraction?
# ---------------------------------
# Hiding complex implementation details and showing only the necessary features.
# You know how to drive a car using the steering wheel without knowing how the engine combustion works.

# What is inheritance?
# ---------------------------------
# A way for one class to derive attributes and methods from another
# (e.g., a Dog class inheriting from an Animal class).

# What is multiple inheritance?
# ---------------------------------
# When a class inherits features from more than one parent class.

# What is polymorphism?
# ---------------------------------
# The ability for different classes to be treated as instances of the same general class through the same interface
#  (e.g., both Circle and Square have a method .draw(), but they do it differently).

# What is method resolution order or MRO?
# ---------------------------------
# The order in which Python looks for a method in a hierarchy of classes,
#  especially important in multiple inheritance.

# =================================
# Exercise 2: Create a deck of cards class
# =================================
# The Deck of cards class should NOT inherit from a Card class.

# The requirements are as follows:
# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# The Deck class :
# should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.


import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6",
                  "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(s, v) for s in suits for v in values]

    def shuffle(self):
        if len(self.cards) == 52:
            random.shuffle(self.cards)
            print("Deck shuffled successfully.")
        else:
            print("Cannot shuffle: The deck is not complete!")

    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return "No more cards!"


#Test

# Initialize the deck
my_deck = Deck()
print(f"1. New deck created. Total cards: {len(my_deck.cards)}")

# Test Shuffle 
my_deck.shuffle() 

# Test Deal 
dealt_card = my_deck.deal()
print(f"2. I dealt a card: {dealt_card}")
print(f"3. Cards remaining in deck: {len(my_deck.cards)}")

# Test the Shuffle Requirement 
print("4. Trying to shuffle again (should fail because deck is at 51)...")
my_deck.shuffle()

# Deal until empty 
print("5. Dealing the rest of the cards...")
for _ in range(51):
    my_deck.deal()

last_try = my_deck.deal()
print(f"6. Final deal attempt: {last_try}")
