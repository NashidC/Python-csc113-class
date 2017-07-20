# coding=utf-8
# Nashid Chowdhury
# Morning session 9:30am
import math


# A. Write a function to convert minutes to milliseconds.

# def main():
#     minutes = input("Enter time in minutes")
#     minutes = int(minutes)
#
#     milli = (minutes*60000)
#     milli = int(milli)
#
#     print ("%d minutes = %d milliseconds" % (minutes, milli))
#
# main()


# B. Write a function to calculate the volume of square based pyramid.

# def main():
#     # type: () -> object
#     base = input("base edge = ")
#     base = int(base)
#
#     height = input("height of the pyramid = ")
#     height = int(height)
#
#     area = ((base * base) * (height / 3))
#     print ("%d is the volume of your pyramid" % area)
#
# main()

# C. Define a function to find the average of two exam scores
#
# def main ():
#     exam_1 = input("exam 1 score = ")
#     exam_1 = int(exam_1)
#
#     exam_2 = input("exam 2 score = ")
#     exam_2 = int(exam_2)
#
#     avg = (exam_1+exam_2)/2
#
#     print ("average exam score is %d" % avg)
#
# main ()

# D. Use math module import to use square root and compute the root of a quadratic equation.


# def main():
#     a = (input("a = "))
#
#     if a == 0:
#         print("'a' cannot be 0")
#         a = (input("a = "))
#     else:
#         a = int(a)
#
#     b = (input("b = "))
#     b = int(b)
#
#     c = (input("c = "))
#     c = int(c)
#
#     delta = (b**2 - 4*a*c)
#     x = ((-b+math.sqrt(delta))/2*a)
#     y = ((-b-math.sqrt(delta))/2*a)
#
#     if x or y < 0:
#         print("try again")
#
#     else:
#         print ("root is equal to %d or %d" % (x, y))
#
#
# main()

#
# E.	Miguel drives his car with the speed of 40 km/h for 2 hours and 60 km/h for 3 hours to
#  reach city A to city B. What’s Miguel’s average speed in this trip in the terms of m/s?
# Use variable assignment if necessary.
#
# def main():
#     km_1 = 40
#     km_2 = 60
#
#     m_1 = km_1 * 10000
#     m_2 = km_2 * 10000
#
#     # conversion between hours to seconds
#     sec = 1
#     min = sec * 60
#     hour = min * 60
#
#     avg = ((m_1 + m_2) / 2)
#     m_sec = (avg * hour)
#     km_hr = (((km_2+km_1)/2))
#
#     print ("Miguel's average speed is %d km/h or %d m/s" % (km_hr,m_sec))
#
# main()

# F.	Define a function to convert Kelvin to Reaumur, then Reaumur to Celsius. Use different functions and call
# one inside the other, if necessary.
#def main():
#    kelvin = (kelvin - 273.15) * (4.0/5)
#    ream = ream* (5.0/4)
#
#
#    r = kelvin
#    print (r)
#
#
#main()



# G.	Suppose you have a rectangular prism R with sides a, 8a, 9a, and a cube C with side 2a. How many of solid
#   C can fit in R?
#def main():
#    a
#    rect = a*(8*a)*(9*a)
#    cube = (2*a)**3.0
#    print (rect / cub)
#
#print(cube%rect)
#
#main()

# H.	Say you have a cube with side n. And you have some amount of marbles (round, sphere) with radius n/4.

def main():
    n
    cube = n**3
    sphere= (4.0/3)*3.14159*(n/4)**3
    print (cube / sphere)

main()

#  How many marbles can you fit in the cube? Obtain the solution with the functios.
