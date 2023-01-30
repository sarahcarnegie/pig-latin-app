vowels = "aeiou"
word = "apple"
suffix = "ay"
# case_two = "monkey"
# case_three = "skip"
# case_four = "string"
# case_five = "sleep"

first_vowel_index = -1 # check this for good practice in python
wordaslist = enumerate(word)
for index, char in wordaslist:
    if char in vowels:
        first_vowel_index = index
        break
    
if first_vowel_index == -1:
    print("no vowel in: " + word)
   
if first_vowel_index == 0:
    print(word + suffix)
   
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
