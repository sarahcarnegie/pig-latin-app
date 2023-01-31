vowels = "aeiou"
suffix = "ay"
first_vowel_index = -1 # check this for good practice in python

def convert(word):
    for index, char in enumerate(word):
        if char in vowels:
            global first_vowel_index
            first_vowel_index = index
            break
    
if first_vowel_index == -1:
    print("no vowel in: " + word)
   
if first_vowel_index == 0:
    print(word + suffix)

convert("apple")
convert("eat")
convert("octopus")
convert("igloo")
convert("unicorn") 
convert("bbbl")
convert("sleep")
convert("skip")
convert("string")
convert("monkey")

# loop thru letters in the word and check each letter to see if it's a vowel
# assign to the variable



# step 2 Take all letters before the first vowel and place them at word end
# consider variable = (first vowel index) is always the first vowel 
# first case = if first vowel index = 0, add ay to the end of the word end
# else if first vowel index is -1 print error, end
# else extract the letters from 0 to first vowel index - 1 at word end and add ay
# save file
# git status - checks which files have changed
# git add <filename> - track the relevant files
# git commit -m "this commit will...."
# git push - pushes changes to github

# I debugged my code using print