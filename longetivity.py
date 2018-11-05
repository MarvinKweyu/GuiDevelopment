#!/bin/python3

#secret to long life
from tkinter import *

class Application(Frame):
    """docstring for Application."""

    def __init__(self, master):
        'initialize Frame'
        super(Application, self).__init__(master)
        self.grid() #make sure it is visible
        self.create_widgets()

    def create_widgets(self):
        '''create button,text and entry widget  '''
        #create instruction label
        self.inst_lbl = Label(self,text = "Enter password for the secret of longetivity: ")
        self.inst_lbl.grid(row=0,column=0,columnspan=2,sticky=W)#aligns text to West i.e left
        #label for password
        self.pw_lbl = Label(self,text="Password: ")
        self.pw_lbl.grid(row=1,column=0,sticky=W)
        #entry widget to accept password
        self.pw_ent = Entry(self)
        self.pw_ent.grid(row=1,column=1,sticky=W)
        #submit button for password
        self.submit_button = Button(self,text="submit",command=self.reveal)#note that command calls reveal method
        self.submit_button.grid(row=2,column=0,sticky=W)
        #widget to display text
        self.secret_txt = Text(self,width=35,height=5,wrap=WORD)
        self.secret_txt.grid(row=3,column=0,columnspan=2,sticky=W)

    def reveal(self):
        'display message based on password'
        contents = self.pw_ent.get()
        if contents =='secret':
            message= "Here's the secret to living to 100:live to 99 "\
            "and then be VERY careful."
        else:
            message = "That's not the correct password,so I can't share the "\
            "secret with you"
        #delete any message in the Text widget first
        self.secret_txt.delete(0.0,END)
        self.secret_txt.insert(0.0,message)

#mainloop
root = Tk()
root.title("Longetivity of life")
root.geometry("300x150")

app = Application(root)
root.mainloop()
