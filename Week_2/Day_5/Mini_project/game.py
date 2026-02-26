
import random

class Game:
    def __init__(self):
        self.options = ["rock", "paper", "scissors"]

    def get_user_item(self):
        
        while True:
            user_input = input("Select rock, paper, or scissors: ").strip().lower()
            if user_input in self.options:
                return user_input
            print("Invalid choice. Please try again.")

    def get_computer_item(self):
        return random.choice(self.options)

    def get_game_result(self, user_item, computer_item):
        
        if user_item == computer_item:
            return "draw"

        if (user_item == "rock" and computer_item == "scissors") or \
           (user_item == "scissors" and computer_item == "paper") or \
           (user_item == "paper" and computer_item == "rock"):
            return "win"
        
        else:
            return "loss"

    def play(self):
       
        user_choice = self.get_user_item()
        computer_choice = self.get_computer_item()
        result = self.get_game_result(user_choice, computer_choice)

       
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        print(f"Result: {result.upper()}!")
        
       
        return result




        




