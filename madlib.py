#!/bin/python3
#create a story based on user input

from tkinter import *

class Application(Frame):
    """docstring for Application."""
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        ''
