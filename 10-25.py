import math
# def main ():
#     principal = eval(input("please enter the prinpal"))
#     air = eval(input("please enter the annual interest rate: "))
#
#     for i in range(10):
#         principal = principal*(1+air)
#
#         print ("total amount: ", princpal)
#
#
#

# def main():
#     n = eval(input("enter the number"))
#     fact = 1
#
#     for factor in range(n, 1, -1) :
#         fact = fact * factor
#
#         print('The factorial of '
#         n," "is" fact)
#

def main():
    n = int(input("how many num do you have: "))
    sum = 0.0

    for i in range(n):
        x = eval(input("enter the number:"))
        sum = sum + x

        print ("the average of", n, "numbers is", sum/n)

    main()