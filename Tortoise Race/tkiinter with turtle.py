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

root.geometry('600x580')
root.maxsize(580,600)
root.minsize(580,600)
root.title('Turtle game')

statusbar=Label(root, text='Click Start To start the game!',bd=3, relief = SUNKEN,anchor=S,fg="light green",font=('Comic Sans MS', 19, 'italic'))
statusbar.pack(side=BOTTOM,fil=X)

root.wm_attributes('-alpha',0.9)

canvas = tk.Canvas(master=root, height=500,width=500,bg = 'blue',bd=3,relief=SUNKEN)
# canvas.configure(bg='black')

canvas.pack()



colors = ["red","orange","pink","yellow","green","blue","black","violet","white"]



"""Defining Turtles and lines"""
turt1 = turtle.RawTurtle(canvas)
turt2 = turtle.RawTurtle(canvas)
turt3 = turtle.RawTurtle(canvas)
turt4 = turtle.RawTurtle(canvas)
turt5 = turtle.RawTurtle(canvas)
line = turtle.RawTurtle(canvas)


turt1.shape("turtle")
turt2.shape("turtle")
turt3.shape("turtle")
turt4.shape("turtle")
turt5.shape("turtle")
"""speed"""
line.speed(10)
turt1.speed(3)
turt2.speed(3)
turt3.speed(3)
turt4.speed(3)
turt5.speed(3)

"""pensize/width"""
turt1.width(5)
turt2.width(5)
turt3.width(5)
turt4.width(5)
turt5.width(5)

line.penup()
line.goto(400,150)
line.color("black")
line.pendown()
line.backward(800)

turt1.penup()
turt1.left(90)
turt1.goto(-150,-210)
turt1.color("green")
turt1.pendown()

turt2.penup()
turt2.left(90)
turt2.goto(-75,-210)
turt2.color("red")
turt2.pendown()

turt3.penup()
turt3.left(90)
turt3.goto(0,-210)
turt3.color("yellow")
turt3.pendown()

turt4.penup()
turt4.left(90)
turt4.goto(75,-210)
turt4.color("purple")
turt4.pendown()

turt5.penup()
turt5.left(90)
turt5.goto(150,-210)
turt5.color("blue")
turt5.pendown()

def winner(e,d,c,b,a):
    print('ok')
    dict = {e:'blue',d:'purple',c:'yellow',b:'red',a:'green'}
    max = 3 #max is defined random
    for i in dict:
        if i > max:
            max = i
    # print(dict[max])
    statusbar['text'] = f'{dict[max]} is the winner'

"""Start Function"""
def startt():
    i=0
    b=1
    time.sleep(1)
    statusbar['text']='Running For Lettuce'
    while b ==1:
        if (turt5.position()[1]>=150) or (turt4.position()[1]>=150) or (turt3.position()[1]>=150) or (turt2.position()[1]>=150) or (turt1.position()[1]>=150):
            # winsound.Beep(100,2000)
            winsound.PlaySound("Ta Da-SoundBible.com-1884170640.wav",winsound.SND_FILENAME|winsound.SND_NOWAIT)
            winner(turt5.position()[1],turt4.position()[1],turt3.position()[1],turt2.position()[1],turt1.position()[1])
            b=2
            break

        else:
            turt1.forward(random.randrange(15,20))
            turt2.forward(random.randrange(15,20))
            turt3.forward(random.randrange(15,20))
            turt4.forward(random.randrange(15,20))
            turt5.forward(random.randrange(15,20))
            i+=1
            print(i,"th round")
            print(turt5.position()[1]>=150,"     ",turt5.position())
            print(turt4.position()[1]>=150,"     ",turt4.position())
            print(turt3.position()[1]>=150,"     ",turt3.position())
            print(turt2.position()[1]>=150,"     ",turt2.position())
            print(turt1.position()[1]>=150,"     ",turt1.position(),"\n")


        


startButton = Button(root,text='Start',font=('Comic Sans MS', 15, 'italic'),relief=RAISED, command = startt)
# startButton.config()
startButton.pack()


root.mainloop()
