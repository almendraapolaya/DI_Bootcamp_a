
import random
from game import Game  

def get_user_menu_choice():
    """Displays menu and validates user input."""
    while True:
        print("\n--- MENU ---")
        print("(g) Play a new game")
        print("(x) Show scores and exit")
        
        choice = input("Select an option: ").strip().lower()
        
        if choice in ['g', 'x']:
            return choice
        print("Invalid choice. Please select 'g' or 'x'.")

def print_results(results):
    """Prints the final score summary."""
    print("\n--- GAME RESULTS ---")
    print(f"Wins:   {results['win']}")
    print(f"Losses: {results['loss']}")
    print(f"Draws:  {results['draw']}")
    print("\nThank you for playing!")

def main():
    
    results = {"win": 0, "loss": 0, "draw": 0}
    
    while True:
        choice = get_user_menu_choice()
        
        if choice == 'g':
            # Create a new Game object and play
            new_game = Game()
            outcome = new_game.play() # play() returns "win", "loss", or "draw"
            
            # Update the dictionary score
            results[outcome] += 1
            
        elif choice == 'x':
            # Show scores and break the loop to exit
            print_results(results)
            break

if __name__ == "__main__":
    main()
