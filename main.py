# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here

    
    if len(word) != len(anagram):
        return False
 
    word = sorted(word)
    anagram = sorted(anagram)
 
    return word == anagram

word = "hello"
anagram = "check"
print(find_anagram(word, anagram))

    

