#!/bin/python3

#using classes
from tkinter import *

class Application(Frame):
    """docstring for Application.A GUI with three buttons"""
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        '''Create three buttons whose master is self
        this implies that Application is their master
        '''

        bttn1 = Button(self,text = "I do nothing!")
        bttn1.grid()
        bttn2 = Button(self,text = "Me too")
        bttn2.grid()
        bttn3 = Button(self,text = "Same here")
        bttn3.grid()

#mainloop
root = Tk()
root.title("Lazy buttons 2")
root.geometry("200x85")

app = Application(root)
root.mainloop()
