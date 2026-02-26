


class AnagramChecker: 
    def __init__(self):
        with open("sowpods.txt", "r") as f:
         self.words = {line.strip().lower() for line in f}

           
    def is_valid_word(self, word):
        return word.lower() in self.words


    def is_anagram(self, word1, word2):
        w1 = word1.lower()
        w2 = word2.lower()
    
        return sorted(w1) == sorted(w2) and w1 != w2
        


    def get_anagrams(self, word):
      word = word.lower()
      store_anagrams = []

      for dict_word in self.words:
         if self.is_anagram(word, dict_word):
            store_anagrams.append(dict_word)
      return store_anagrams



    
    
         
# Temporary test at the bottom of anagram_checker.py
if __name__ == "__main__":
    checker = AnagramChecker()
    print(f"Is 'meat' valid? {checker.is_valid_word('meat')}")
    print(f"Anagrams of 'meat': {checker.get_anagrams('meat')}")