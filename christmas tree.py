import turtle
from turtle import TurtleScreen
import random
from turtle import Screen
import winsound
import time
import tkinter as tk
from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk

root = tk.Tk()

root.geometry('600x620')
root.maxsize(620,600)
root.minsize(620,600)
root.title('X-Christmas Tree')

statusbar=Label(root, text='Merry Christams From Lvyy',bd=3, relief = SUNKEN,anchor=S,fg="light green",bg="white" ,font=('Comic Sans MS', 19, 'italic'))
statusbar.pack(side = BOTTOM ,fil=X)

canvas = tk.Canvas(master=root, height=500,width=500,bg = 'blue',bd=3,relief=SUNKEN)
canvas.configure(bg='black')

canvas.pack()

colors = ["red","yellow","pink","blue","white","orange","magenta","cyan","grey","light green","light blue"]


"""defining lines"""
rectangle = turtle.RawTurtle(canvas)
triangle3 = turtle.RawTurtle(canvas)
triangle2 = turtle.RawTurtle(canvas)
triangle1 = turtle.RawTurtle(canvas)
circle_up = turtle.RawTurtle(canvas)
inner_circle = turtle.RawTurtle(canvas)

"""speed"""
rectangle.speed(11)
triangle3.speed(11)
triangle2.speed(11)
triangle1.speed(11)
circle_up.speed(11)
inner_circle.speed(11)

"""Turtle visibility"""
rectangle.hideturtle()
triangle3.hideturtle()
triangle2.hideturtle()
triangle1.hideturtle()
circle_up.hideturtle()
inner_circle.hideturtle()

"""widths"""
rectangle.width(5)
triangle3.width(5)
triangle2.width(5)
triangle1.width(5)
circle_up.width(5)
inner_circle.width(5)

global stopp 
stopp = False

global i
i = 0

def nothing():
    pass

def Merry_Christmas():
    global i
    global stopp
    i+=1

    if i>1:
        stopp = True
        nothing()
    else:
        pass

    if stopp == True:
        pass
    else:
        """Basic wood"""
        rectangle.penup()
        rectangle.goto(-25,-220)
        rectangle.color('brown','brown')
        rectangle.pendown()

        rectangle.begin_fill()
        rectangle.forward(50)
        rectangle.left(90)
        rectangle.forward(110)
        rectangle.left(90)
        rectangle.forward(50)
        rectangle.left(90)
        rectangle.forward(110)
        rectangle.end_fill()

        """last triangle"""
        triangle3.penup()
        triangle3.goto(-115,-120)
        triangle3.color(random.choice(colors),'green')
        triangle3.pendown()

        triangle3.begin_fill()
        triangle3.forward(230)
        triangle3.left(120)
        triangle3.forward(230)
        triangle3.left(120)
        triangle3.forward(230)
        triangle3.left(120)
        triangle3.end_fill()

        """2nd last triangle"""
        triangle2.penup()
        triangle2.goto(-100,-10)
        triangle2.color(random.choice(colors),'green')
        triangle2.pendown()

        triangle2.begin_fill()
        triangle2.forward(200)
        triangle2.left(120)
        triangle2.forward(200)
        triangle2.left(120)
        triangle2.forward(200)
        triangle2.left(120)
        triangle2.end_fill()


        """3rd last triangle"""
        triangle1.penup()
        triangle1.goto(-75,90)
        triangle1.color(random.choice(colors),'green')
        triangle1.pendown()

        triangle1.begin_fill()
        triangle1.forward(150)
        triangle1.left(120)
        triangle1.forward(150)
        triangle1.left(120)
        triangle1.forward(150)
        triangle1.left(120)
        triangle1.end_fill()

        while True:
            if stopp == True:
                break
            else:
            # """circle_up"""    
                circle_up.penup()
                circle_up.goto(0,170)
                circle_up.color(random.choice(colors))
                circle_up.pendown()

                circle_up.begin_fill()
                circle_up.circle(36)
                circle_up.end_fill()


                inner_circle.penup()
                inner_circle.goto(0,190)
                inner_circle.color(random.choice(colors))
                inner_circle.pendown()

                inner_circle.begin_fill()
                inner_circle.circle(15)
                inner_circle.end_fill()

                statusbar['fg'] = random.choice(colors)
                startButton.configure(text="Stop")


startButton = Button(root,text='Start',font=('Comic Sans MS', 15, 'italic'),relief=RAISED,command = Merry_Christmas)
# startButton.config()
startButton.pack(side = BOTTOM)


root.mainloop()
