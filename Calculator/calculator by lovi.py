import tkinter
from tkinter import *
import math

class calculator():

    def __init__(self,root=Tk()):
        root.geometry("330x300")
        root.minsize("330","300")
        root.maxsize("500","500")

        root.wm_attributes('-alpha', 0.8) 
        root.configure(borderwidth=20)

        root.title("LVY's Calculator")
        root.iconbitmap(r"E:\\New folder (2)\\Python practice\\Calculator\\calculator_icon.ico")
        root.configure(background="black",relief=SUNKEN)
        root.config(highlightbackground="white")

        self.decimal_point_open = False

        self.scvalue = StringVar()
        self.scvalue.set("")
        self.screen = Entry(root,textvar = self.scvalue, font="lucia 25  ",width=15)
        # Entry.config(self,width=10)
        self.screen.pack(ipadx=8, pady=5,padx=5)

        frame1 = Frame(root)

        frame1.pack()
        frame1.configure(background="black")

        #number buttons
        bt9 = Button(frame1, text="9",font="lucia 13  ",bg="black",fg="white" ,padx=20,command = lambda: self.clickk("9"))
        bt9.grid(row=4, column=0, sticky="ewns", padx=2, pady=2)

        bt8 = Button(frame1, text="8",font="lucia 13  ",bg="black",fg="white",padx=20,command =lambda: self.clickk("8"))
        bt8.grid(row=4, column=1, sticky="ewns", padx=2, pady=2)

        bt7 = Button(frame1, text="7",font="lucia 13  ",bg="black",fg="white" ,padx=20,command =lambda: self.clickk("7"))
        bt7.grid(row=4, column=2, sticky="ewns", padx=2, pady=2)

        bt6 = Button(frame1, text="6",font="lucia 13  ",bg="black",fg="white" ,padx=20,command =lambda: self.clickk("6"))
        bt6.grid(row=5, column=0, sticky="ewns", padx=2, pady=2)

        bt5 = Button(frame1, text="5",font="lucia 13  ",bg="black",fg="white" ,padx=20,command =lambda: self.clickk("5"))
        bt5.grid(row=5, column=1, sticky="ewns", padx=2, pady=2)

        bt4 = Button(frame1, text="4",font="lucia 13  ",bg="black",fg="white" ,padx=20,command =lambda: self.clickk("4"))
        bt4.grid(row=5, column=2, sticky="ewns", padx=2, pady=2)

        bt3 = Button(frame1, text="3",font="lucia 13  ",bg="black",fg="white" ,padx=20,command =lambda: self.clickk("3"))
        bt3.grid(row=6, column=0, sticky="ewns", padx=2, pady=2)

        bt2 = Button(frame1, text="2",font="lucia 13  ",bg="black",fg="white" ,padx=20,command =lambda: self.clickk("2"))
        bt2.grid(row=6, column=1, sticky="ewns", padx=2, pady=2)

        bt1 = Button(frame1, text="1",font="lucia 13  ",bg="black",fg="white" ,padx=20,command =lambda: self.clickk("1"))
        bt1.grid(row=6, column=2, sticky="ewns", padx=2, pady=2)

        bt0 = Button(frame1, text="0",font="lucia 13  ",bg="black",fg="white" ,padx=20,command =lambda: self.clickk("0"))
        bt0.grid(row=7, column=0, sticky="ewns", padx=2, pady=2)

        bt_decimal = Button(frame1, text=".",font="lucia 13  ",bg="black",fg="white" ,padx=20,command =lambda: self.clickk("."))
        bt_decimal.grid(row=8, column=2, sticky="ewns", padx=2, pady=2)

        #operation buttons
        btplus = Button(frame1, text="+",font="lucia 13 bold",bg="black",fg="white" ,padx=20,command =lambda: self.clickk("+"))
        btplus.grid(row=4, column=3, sticky="ewns", padx=2, pady=2)

        btminus = Button(frame1, text="-",font="lucia 13 bold",bg="black",fg="white" ,padx=20,command =lambda: self.clickk("-"))
        btminus.grid(row=5, column=3, sticky="ewns", padx=2, pady=2)

        btmultiply = Button(frame1, text="×",font="lucia 13 ",bg="black",fg="white" ,padx=20,command =lambda: self.clickk("*"))
        btmultiply.grid(row=6, column=3, sticky="ewns", padx=2, pady=2)

        btdivide = Button(frame1, text="÷",font="lucia 13 bold",bg="black",fg="white" ,padx=20,command =lambda: self.clickk("/"))
        btdivide.grid(row=7, column=3, sticky="ewns", padx=2, pady=2)

        btequal = Button(frame1, text="=",font="lucia 13 bold",bg="black",fg="white" ,padx=20,command =lambda: self.clickk("="))
        btequal.grid(row=8, column=3, sticky="ewns", padx=2, pady=2)

        # bt_square = Button(frame1, text="x\u00b2",font="lucia 13 bold",bg="black",fg="white" ,padx=20,command =lambda: self.clickk("x\u00b2"))
        # bt_square.grid(row=8, column=1, sticky="ewns", padx=2, pady=2)

        #extra functions of calculator
        btclear = Button(frame1,text="C", font="lucia 13 bold",bg="black",fg="white" ,padx=20,command =self.clear)
        btclear.grid(row=8, column=0, sticky="ewns", padx=2, pady=2)

        bt_delete = Button(frame1,text="Del", font="lucia 13 bold",bg="black",fg="white" ,padx=20,command =self.popopop)
        bt_delete.grid(row=8, column=1, sticky="ewns", padx=2, pady=2)

        root.mainloop()

    def clickk(self,bt):
            text = self.scvalue.get()
            char_num = len(text)

    #define valid characters for the beginning of the expression
            if(char_num==0):
                valid_chars_for_init = ".0123456789-"
                if(bt in valid_chars_for_init):
                    text+=bt
                    self.scvalue.set(text)
            
            else:
    # decimal point usage control
                last_char = text[char_num - 1]
                if(bt=='.' and not last_char in "+-*/"):
                    if(self.decimal_point_open):
                        text+= bt
                    else:
                        text += bt
                        self.scvalue.set(text)
                        self.decimal_point_open = True
                else:
                    if(last_char in ".0123456789" and bt in ".0123456789"):
                        text+=bt
                        self.scvalue.set(text)
                    elif(last_char in "0123456789" and not self.decimal_point_open and bt in "+-*/"):
                        text += bt
                        self.scvalue.set(text)
                    elif(self.decimal_point_open and not last_char=='.' and bt in "+-*/"):
                        text += bt
                        self.scvalue.set(text)
                        self.decimal_point_open = False
    # operator control
                    elif(last_char in "+-*/" and bt in ".0123456789"):
                        text += bt
                        self.scvalue.set(text)

    # button = pressed, get result
                    elif(bt=='=' and last_char in "0123456789"):
                        try:
                            if self.scvalue.get().isdigit():
                                value = float(scvalue.get())
                            else:
                                value = eval(self.scvalue.get())
                                self.scvalue.set(value)
                                self.screen.update()
                        except Exception as e:
                            print(e)
                            self.scvalue.set("Error")
                            self.screen.update()

    def clear(self):
        self.decimal_point_open = False
        self.scvalue.set("")
        self.screen.update()
    
    def popopop(self):
        self.scvalue.set(self.scvalue.get()[:-1])
        self.decimal_point_open = False
        self.screen.update()


if (__name__ == "__main__"):
    calc = calculator()
