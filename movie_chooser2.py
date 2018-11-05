#!/bin/python3

#using radio buttons

from tkinter import *

class Applications(Frame):
    """docstring for Applications."""
    def __init__(self,master):
        super(Applications, self).__init__(master)
        self.grid()#make contents visible
        self.create_widgets()

    def create_widgets(self):
        'create widgets to uses'
        #create description label
        Label(self,text = "Choose your favourite movie types").grid(row=0,column=0,sticky=W)
        #create instruction label
        Label(self,text="Select one").grid(row=1,column=0,sticky=W)
        #create radio button
        self.favourite = StringVar()
        self.favourite.set(None)
        #create comedy radio button
        Radiobutton(self,text="Comedy",variable=self.favourite,value="comedy.",command=self.update_text).grid(row=2,column=0,sticky=W)
        #create romance radio button
        Radiobutton(self,text="Romance",variable=self.favourite,value="romance.",command=self.update_text).grid(row=3,column=0,sticky=W)
        #create drama radio button
        Radiobutton(self,text="Drama",variable=self.favourite,value="drama.",command=self.update_text).grid(row=4,column=0,sticky=W)
        #text field for results
        self.results_txt = Text(self,width=40,height=5,wrap=WORD)
        self.results_txt.grid(row=5,column=0,columnspan=3)

    def update_text(self):
        '''update text area and display fav movie type '''
        message = "Your favourite movie is "
        message+=self.favourite.get()
        #delete current text
        self.results_txt.delete(0.0,END)
        self.results_txt.insert(0.0,message)

#mainloop
root = Tk()
root.title("Movie Chooser 2")
app = Applications(root)
root.mainloop()
