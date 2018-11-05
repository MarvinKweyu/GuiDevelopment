#!/bin/python3

#simple GUI
#demonstrates creating a window

from tkinter import *

#create root window
root = Tk()

#modify window
root.title("Simple GUI")
root.geometry("200x100") #notice use of x and not *

#kick off loop
root.mainloop()
