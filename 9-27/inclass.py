# Nashid Chowdhury
# Morning Session 9:30


# Question A
# def main():
#
#     score = int((input('input exam score'))
#
#
#     if input(score) > 50:
#         print("you passed")
#     else:
#         print ("you failed")
#
#
#     main()


# Question B

# def temp():
#     temperature = input('input a temperature type ')
#
#     if temperature == 'K':
#         print ('The absolute zero temperature for Kelvin is 0 K')
#     elif temperature == 'C':
#         print ('The absolute zero temperature for Celsius is -273.15 C')
#     elif temperature == 'F':
#         print ('The absolute zero temperature for Celsius is -459.67 F')
#     else:
#         print('The absolute zero temperature for Rankine is 0 R')
#
# temp()


# Question C
#
# def exam ():
#
#     exam_1 = input('please enter first exam score: ')
#     exam_1 = int(exam_1)
#
#     exam_2 = input('please enter second exam score: ')
#     exam_2 = int(exam_2)
#
#     avg = (exam_1+exam_2)/2
#
#     if 100 <= avg >= 97:
#         print ("your grade is an A+")
#
#     elif 96 <= avg >= 93:
#         print ("your grade is an A")
#
#     elif 92 <= avg >= 90:
#         print ("your grade is an A-")
#
#     elif 89 <= avg >= 87:
#         print ("your grade is a B+")
#
#     elif 86 <= avg >= 83:
#         print ("your grade is a B")
#
#     elif 82 <= avg >= 80:
#         print ("your grade is a B-")
#
#     elif 79 <= avg >= 77:
#         print ("your grade is a C+")
#
#     elif 76 <= avg >= 73:
#         print ("your grade is a C")
#
#     elif 72 <= avg >= 70:
#         print ("your grade is a C-")
#
#     elif 69 <= avg >= 67:
#         print ("your grade is a D+")
#
#     elif 65 <= avg >= 66:
#         print ("your grade is a D")
#
#     else:
#         print ("your grade is an d")
#
# exam()


# Question D

# def main():
#
#     num = int(input('please enter a number: '))
#
#     if num == 1:
#         print ("Sunday")
#     elif num == 2:
#         print ("Monday")
#     elif num == 3:
#         print ("Tuesday")
#     elif num == 4:
#         print ("Wednesday")
#     elif num == 5:
#         print ("Thursday")
#     elif num == 6:
#         print ("Friday")
#     elif num == 7:
#         print ("Saturday")
#
#     else:
#         print ("That is an invalid number, try again")
#
# main()


# Question E
#
# def main():
#     input_1 = int(input("please enter a number"))
#     input_2 = int(input("please enter another number"))
#
#     input_3 = (input("do you want to add or subtract?"))
#
#     if input_3 == 'add':
#         print ("your total is %d" % (input_1 + input_2))
#
#     else:
#         print ("your total is %d" % (input_1 - input_2))
#
# main()

# Question F

def main():
    side_a = int(input("please enter a side: "))
    side_8a = side_a*8
    side_9a = side_a*9

    rec = (side_a*side_8a*side_9a)

    cube = (side_a**3)

    print ("cube can fit into rectangle %d times" % (cube % rec))

main()
