#=============================
#  Daily Challenge Tanslator
#=============================

from googletrans import Translator

# 1. Given list of French words from the Instructions:
french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]

# 2. Initialize the Translator object:
translator = Translator()

# 3. Initialize an empty dictionary for the results:
translated_dict = {}

# 4. Loop through each French word and translate:
for word in french_words:
    # Translate from French ('fr') to English ('en')
    translation = translator.translate(word, src='fr', dest='en')
    
    # Store in dictionary: Key = French word, Value = English translation
    translated_dict[word] = translation.text

# 5. Result: 
print("=== TRANSLATED DICTIONARY ===")
print(translated_dict)