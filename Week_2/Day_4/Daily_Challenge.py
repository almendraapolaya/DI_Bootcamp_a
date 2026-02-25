
import string
import re

class Text:
    def __init__(self, text):
        self.text = text

    def word_frequency(self,word):
        words = self.text.split()
        count = words.count(word)

        if count > 0:
            return count
        else: 
            return f"The word {word} was not found."
    
    def most_common_word(self):
        words = self.text.split()
        if not words:
            return None
            
        frequencies = {}
        for w in words:
            frequencies[w] = frequencies.get(w, 0) + 1
        
        most_common = max(frequencies, key=frequencies.get)
        return most_common

    def unique_words(self):
        words = self.text.split()
        unique_set = set(words)
        return list(unique_set)

    @classmethod
    def from_file(cls, path):
        with open(path) as f:
            return cls(f.read().strip())




class TextModification(Text):

    def remove_punctuation(self):
        self.text = re.sub(r'[^\w\s]', '', self.text)
        return self.text

    def remove_stop_words(self):
        stop_words = ["a", "the", "is", "in", "it", "of", "and", "to", "for", "with"]
        words = self.text.split()
        filtered = [w for w in words if w.lower() not in stop_words]
        self.text = " ".join(filtered)
        return self.text

    def remove_special_characters(self):
        self.text = re.sub(r'[^a-zA-Z0-9\s]', '', self.text)
        self.words = self.text.split()
        return self


#test:

test_string = "Hello world! This is a test. Hello again, world."
cleaner = TextModification(test_string)

print("--- Step 1: Raw Analysis ---")
print(f"Unique Words: {cleaner.unique_words()}") 

print("\n--- Step 2: Cleaning ---")
cleaner.remove_punctuation()
cleaner.remove_stop_words()
print(f"Cleaned Text: {cleaner.text}")

print("\n--- Step 3: Clean Analysis ---")

print(f"Unique Words: {cleaner.unique_words()}")
print(f"Most Common: {cleaner.most_common_word()}")