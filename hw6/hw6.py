# Python hw6: deadline is next week before class
# email or printed copy
# ayuskey@ccny.cuny.edu
#
# str1 =
# str2 =
#
# 1.the characters occurring in str 1 and not str2.
# 2.char occurring in str2 not in str 1
# 3. output only distinct characters.
#
# ex input
#
# str1 = abcdeeeggg
# str2 = iiibcduvz
#
# 1st output should be:
# a
# e
# e
# e
# g
#
# 2nd output should be:
# i
# i
# i
# u
# v
# z
#
# 3rd output:
# a
# e
# g
# i
# u
# v
# z


str1 = input("Enter first word: ")
str2 = input("Enter second word: ")

for i in str1:
    if i in str1 and i not in str2:
        output1 = " ".join(i)
for i in str2:
    if i in str2 and i not in str1:
            output2 = " ".join(i)

    output3 = " ".join(set(output1+output2))

print("Characters in the only first string: {}\nCharacters in only in the second\n string: {}\ncharacters in both: {}".format(output1, output2, output3))