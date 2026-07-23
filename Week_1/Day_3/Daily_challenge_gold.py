#======================
# Daily challenge GOLD: Caesar Cypher
#======================

print("=== CAESAR CIPHER PROGRAM ===")

# 1. Ask user whether they want to encrypt or decrypt
user_action = input("Type 'e' to ENCRYPT or 'd' to DECRYPT: ").strip().lower()

# 2. Get the message and shift value
text_input = input("Enter your message: ")
shift_amount = int(input("Enter shift number (e.g., 3): "))

# Initialize result string
cipher_result = ""

# 3. Perform encryption or decryption
for char in text_input:
    # Handle uppercase letters
    if char.isupper():
        if user_action == 'e':
            # Shift forward within 'A'-'Z' bounds (ASCII 65 to 90)
            new_char = chr((ord(char) - 65 + shift_amount) % 26 + 65)
        else:
            # Shift backward within 'A'-'Z' bounds
            new_char = chr((ord(char) - 65 - shift_amount) % 26 + 65)
        cipher_result += new_char

    # Handle lowercase letters
    elif char.islower():
        if user_action == 'e':
            # Shift forward within 'a'-'z' bounds (ASCII 97 to 122)
            new_char = chr((ord(char) - 97 + shift_amount) % 26 + 97)
        else:
            # Shift backward within 'a'-'z' bounds
            new_char = chr((ord(char) - 97 - shift_amount) % 26 + 97)
        cipher_result += new_char

    # Non-alphabetic characters (spaces, punctuation) stay unchanged
    else:
        cipher_result += char

# 4. Display output
action_label = "Encrypted" if user_action == 'e' else "Decrypted"
print(f"\n {action_label} Message: {cipher_result}")