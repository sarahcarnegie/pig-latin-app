import re
vowels = "aeiou"
suffix = "ay"

# convert takes a word and returns the word in pig-latin
def convert(word:str) -> str: 
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
        print(piglatin)







# tests
# test_cases = ("apple", "bbbl", "monkey","sleep","string", "Bandicoot", "pla!ypus", "do1phin")
# for test_wrd in test_cases:
#     if bool(re.search(r'\d',test_wrd))==True:        
#         print("invalid word: " + test_wrd)     
#     else:
#         piglatin = convert(test_wrd)
#         print(piglatin)

# save file
# git status - checks which files have changed
# git add <filename> - track the relevant files
# git commit -m "this commit will...."
# git push - pushes changes to github

