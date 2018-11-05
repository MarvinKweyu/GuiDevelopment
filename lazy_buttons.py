#!/bin/python3
#make buttons that do nothing

from tkinter import *

root = Tk()
root.title("Lazy Buttons")
root.geometry("300x300")

#create frame in window to hold widgets
app = Frame(root)
app.grid()

#create buttons in Frame
bttn1 = Button(app,text="I do nothing!")
bttn1.grid()

#alternatively
bttn2 = Button(app)
bttn2.grid()
bttn2.configure(text = "Me too!")

#alternatively 2
bttn3 = Button(app)
bttn3.grid()
bttn3["text"] = 'Same here'

#mainloop
root.mainloop()
