#!/bin/python3
#demonstrates how to use labels

from tkinter import *

root = Tk()

root.title("Labler")
root.geometry("200x50")

#create a frame to hold other widgets
app = Frame(root)

app.grid()

# create label in frame
lbl = Label(app,text="I am a label")
lbl.grid()#make the label always visible #grid inside a grid

#main mainloop
root.mainloop()
