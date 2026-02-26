from anagram_checker import AnagramChecker


def main():
    
    checker = AnagramChecker()

    while True:
        print("\n--- MENU ---")
        print("1. Find anagrams for a word")
        print("2. Exit")
        
        choice = input("Select an option: ").strip()

        if choice == "2":
            print("Goodbye!")
            break
        
        elif choice == "1":
            user_word = input("Enter your word: ").strip()

          
            if " " in user_word:
                print("ERROR: Only a single word is allowed.")
                continue 
            
            
            if not user_word.isalpha():
                print("ERROR: Only letters are allowed (no numbers or symbols).")
                continue

            
            if checker.is_valid_word(user_word):
                results = checker.get_anagrams(user_word)
                
                print(f'\nYOUR WORD: "{user_word.upper()}"')
                print("This is a valid English word.")
                
                if results:
                    
                    print(f"Anagrams for your word: {', '.join(results)}.")
                else:
                    print("No anagrams were found for this word.")
            else:
                print(f"\n'{user_word}' is not a valid word in our dictionary.")

        else:
            print("Invalid choice. Please pick 1 or 2.")

if __name__ == "__main__":
    main()


# my_list = ['mate', 'tame', 'team']
# print(my_list)