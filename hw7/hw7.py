#Description hw 7:
# input = a word
# output: {} has {} vowels and {} consonants —>number of vowels and consonants
# ( using .format(word, vowels, consonants)
# -define a class
#
#
#
# #handle everything inside this class
# #maybe define pre-list for vowels and consonants
#
#
# class …..
# 	ask for the word
# 	check if vowel or consonant
# 	print the result
# 		—due next tuesday





def check():
    for char in word:
        if char in vowel:
            countvow+= 1
        elif char in con:
            countcon += 1

            print ('number of vow: {}'.format(countvow))
            print ('number of con:{}'.format(countcon))

class WordCheck:
    def __init__(self):
        pass

    word = str(input("Enter a word: "))
    vowel = list("aeiouAEIOU")
    con = list("BCDFGHJKLMNPQRSTVXYZbcdfghjklmnpqrstvxyz")
    countvow = 0
    countcon = 0
