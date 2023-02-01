vowels = "aeiou"
suffix = "ay"


def convert(word):
    first_vowel_index = -1
    for index, char in enumerate(word):
        if char in vowels:
            first_vowel_index = index
            break
    
    if first_vowel_index == -1:
        print("no vowel in: " + word)
    
    if first_vowel_index == 0:
        print(word + suffix)

    if first_vowel_index > 0: 
        cons_before_vowel = word[:first_vowel_index:]
        new_word = word[first_vowel_index::]
        print(new_word + cons_before_vowel + suffix)


test_cases = ("apple", "bbbl", "monkey","sleep","string", "Bandicoot", "pla!ypus", "do1phin")
for test_wrd in test_cases:
    convert(test_wrd)


# save file
# git status - checks which files have changed
# git add <filename> - track the relevant files
# git commit -m "this commit will...."
# git push - pushes changes to github

