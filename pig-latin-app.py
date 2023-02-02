import re
vowels = "aeiou"
suffix = "ay"

# first_vowel_index takes a word and returns the index of the first vowel
# if no vowel is found it returns -1
def first_vowel_index(word:str) -> int:
    for index, char in enumerate(word):
        if char in vowels:
            return index
    return -1

# covert take a word and the index of the first vowel(>=0) and return the word in pig-latin
def convert(word:str, first_vowel_index:int) -> str: 
    lc_word = word.lower()
    if first_vowel_index < 0:
        print("error: index must be 0 or greater") 
    elif first_vowel_index > 0: 
        cons_before_vowel = lc_word[:first_vowel_index:]
        new_word = lc_word[first_vowel_index::]
        return new_word + cons_before_vowel + suffix

    return word + suffix

test_cases = ("apple", "bbbl", "monkey","sleep","string", "Bandicoot", "pla!ypus", "do1phin")
for test_wrd in test_cases:
    if bool(re.search(r'\d',test_wrd))==True:        
        print("invalid word: " + test_wrd)
    else:
        index = first_vowel_index(test_wrd)
        if index < 0:
            print("no vowel in: " + test_wrd)
        else:
            piglatin = convert(test_wrd, index)
            print(piglatin)

# save file
# git status - checks which files have changed
# git add <filename> - track the relevant files
# git commit -m "this commit will...."
# git push - pushes changes to github

