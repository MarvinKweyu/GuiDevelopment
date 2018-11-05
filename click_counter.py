#!/bin/python3
#count number o ftimes button is clicked

from tkinter import *

class Application(Frame):
    """docstring for Application."""
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.bttn_clicks = 0 #no. of buttons clicked
        self.create_widget()

    def create_widget(self):
        'Create a button showing no of clicks'
        self.bttn = Button(self)
        self.bttn["text"] = "Total Clicks: 0"
        self.bttn["command"] = self.update_count
        self.bttn.grid()

    def update_count(self):
        'increase click count and display new Total'
        self.bttn_clicks += 1
        self.bttn["text"] = "Total clicks: "+str(self.bttn_clicks)

# mainloop
root = Tk()
root.title()
root.geometry("200x50")

app = Application(root)
root.mainloop()
