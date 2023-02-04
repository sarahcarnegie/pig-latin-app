import re
pl_words = [] # holds list of converted words

# convert takes a word and returns the word in pig-latin
def convert(word:str) -> str:
    special_characters = "!@#$%^&*()-+?_=,<>/ "

    # check for numbers or special characters
    if bool(re.search(r'\d', word))==True or any(c in special_characters for c in word):        
        print("invalid word: " + word)
        return "" 

    # interate through letters
    for index, char in enumerate(word):
        if char in "aeiou": # if vowel found, convert to pig latin
            cons_before_vowel = word.lower()[:index:] # extracts word start to first vowel (lowercase)
            new_word = word.lower()[index::] # extracts first vowel to word end 
            return new_word + cons_before_vowel + "ay"

    print("error: no vowel in: " + word)
    return "" 

# reads original words from file 
with open('words-in.txt') as f:
    for word in f:
        piglatin = convert(word.strip())
        pl_words.append(piglatin)
    f.close()

# writes converted words to file 
with open('words-out.txt', 'w') as f:
    for word in pl_words:
        f.write(f"{word}\n")
    f.close()