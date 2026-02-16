#
#==================================================
# Exercise: Outputs
#==================================================
# Instructions
# Predict the output of the following code snippets:

3 <= 3 < 9                           # True
3 == 3 == 3                          # True
bool(0)                              # False
bool(5 == "5")                       # False
bool(4 == 4) == bool("4" == "4")     # True
bool(bool(None))                     # False

x = (1 == True)                      # True (1 == 1)
y = (1 == False)                     # False (1 == 0)
a = True + 4                         # 1 + 4 = 5
b = False + 10                       # 0 + 10 = 10

print("x is", x)                     #True
print("y is", y)                     #False
print("a:", a)                       # 5
print("b:", b)                       # 10

#==================================================
# Exercise: How many characters in a sentence ?
#==================================================
# Instructions
# Use python to find out how many characters are in the following text, use a single line of code (beyond the establishment of your my_text variable).

my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

print(len(my_text)) #445

#===================================================
# Exercise: Longest word without a specific character
#===================================================
# Instructions
# Keep asking the user to input the longest sentence they can without the character “A”.
# Each time a user successfully sets a new longest sentence, print a congratulations message.

longest_len_sentence = 0

while True:
    sentence = input("Enter a the longest sentence you can without the character 'a' ")
    
    if "a" in sentence.lower():
        print("I am sorry, your sentence contains an 'a'")
    elif sentence.lower() == "exit":
        break
    else:
        len_sentence = len(sentence)
        if len_sentence > longest_len_sentence:
            longest_len_sentence = len_sentence
            print(f"Congratulations! Your new record is: {longest_len_sentence} characters!")
       
