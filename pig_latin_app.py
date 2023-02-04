import re
vowels = "aeiou"
suffix = "ay"
pl_words = []
special_characters = "!@#$%^&*()-+?_=,<>/ "
# convert takes a word and returns the word in pig-latin
def convert(word:str) -> str:
    # check for numbers
    if bool(re.search(r'\d', word))==True:        
        print("invalid word: " + word)
        return "" 

    if any(c in special_characters for c in word):
        print("invalid word: " + word)
        return "" 

    # find the index of the first vowel
    first_vowel_index = -1
    for index, char in enumerate(word):
        if char in vowels:
            first_vowel_index = index
            break

    lc_word = word.lower()
    if first_vowel_index >= 0:
        # takes a substring from the start of the word to first vowel
        cons_before_vowel = lc_word[:first_vowel_index:] 
        # takes a substring from first vowel to the end of the word
        new_word = lc_word[first_vowel_index::]
        return new_word + cons_before_vowel + suffix

    print("error: no vowel in: " + word)
    return "" 
    
with open('words-in.txt') as f:
    for word in f:
        piglatin = convert(word.strip())
        pl_words.append(piglatin)
    f.close()
        
with open('words-out.txt', 'w') as f:
    for word in pl_words:
        f.write(f"{word}\n")
    f.close()
        






# tests
# test_cases = ("apple", "bbbl", "monkey","sleep","string", "Bandicoot", "pla!ypus", "do1phin")
# for test_wrd in test_cases:
#         
#     else:
#         piglatin = convert(test_wrd)
#         print(piglatin)

# save file
# git status - checks which files have changed
# git add <filename> - track the relevant files
# git commit -m "this commit will...."
# git push - pushes changes to github

