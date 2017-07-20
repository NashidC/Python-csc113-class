#Morning Section
#Authors: Nashid Chowdhury & Kevin Alfonso



import turtle
from Tkinter import *
import random
from string import ascii_letters

root = Tk()  # new window
root.title("Most Frequent")
root.resizable(height=FALSE, width=FALSE)

entry = Entry(root, bd=5)
entry.pack(side=RIGHT)

label = Label(root, text="Please enter number", bg="blue", fg="white")  # creates the label
label.pack(side=TOP)  # pack places it in the window and displays it in the screen


def draw_button():
    n = entry.get()
    root.quit()

    if n > 1:
        draw()


Button(root, text="Draw", command=draw_button()).grid(row=3, column=0, sticky=W, pady=4)

# Button(root, text="Draw", command=for_draw).grid(row=3, column=1, sticky=W, pady=4)

chars = ascii_letters
wordsCont = {}

file = open("Words.txt")


#
# def for_draw():
#     turtle.reset()
#     draw()
#     pass


def probability():
    global freq
    global letter
    # goes through each line
    for line in file:
        for word in line.split():
            if chars in word:
                # goes through each character
                wordsCont[chars] = wordsCont.get(chars, 0) + 1
                return wordsCont

    # sorts in decending order by frequency
    freq = []
    for key, value in wordsCont.items():
        freq.append((value, key))
        freq.sort()
        freq.reverse()
        return freq

    # calculates the total probability
    prob = []
    rest_of_letters = 0
    total = 0

    for freq, letter in prob[0:25]:
        total += freq

    for freq, letter in prob[0:entry]:
        prob_percent = float(freq) / total
        prob.append((prob_percent, letter))

    for freq, letter in prob[0:26]:
        rest_of_letters += + freq

    prob_percent = float(rest_of_letters) / total
    prob.append((prob_percent, "Others"))

    return prob


def draw():
    turtle.reset()
    red = random.randrange(0, 257, 10)
    green = random.randrange(0, 257, 10)
    blue = random.randrange(0, 257, 10)

    radius = 300
    angle = freq * 360
    string = letter + " = " + str(freq * 100)[:5] + "%"

    colormode(255)
    color(red, green, blue)
    pendown()
    forward(radius)
    left(90)
    begin_fill()
    circle(radius, angle)
    left(90)
    forward(radius)
    end_fill()
    penup()
    left(180)

    color('black')
    penup()
    forward(radius)
    left(90)
    circle(radius, angle / 2)
    write(string, align="center", font=12)
    circle(radius, angle / 2)
    left(90)
    forward(radius)
    left(180)

pass

root.mainloop()
