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
        'Create widgets to get story information and display story'

        #create instrucion label
        Label(self,text="Enter information for story:").grid(row=0,column=0,columnspan=2,sticky=W)
        #create label and text entry for name of person
        Label(self,text="Person: ").grid(row=1,column=0,sticky=W)
        self.person_ent = Entry(self)
        self.person_ent.grid(row=1,column=1,sticky=W)

        #label and text entry for plural noun
        Label(self,text="Plural noun:").grid(row=2,column=0,sticky=W)
        self.noun_ent = Entry(self)
        self.noun_ent.grid(row=2,column=1,sticky=W)

        #label and entry for verb
        Label(self,text='Verb').grid(row=3,column=0,sticky=W)
        self.verb_ent = Entry(self)
        self.verb_ent.grid(row=3,column=1,sticky=W)

        # Label for adjectives Checkbutton
        Label(self,text='Adjectives').grid(row=4,column=0,sticky=W)

        #itchy Checkbutton
        self.is_itchy = BooleanVar()
        Checkbutton(self,text="itchy",variable=self.is_itchy).grid(row=4,column=1,sticky=W)

        #joyous electric
        self.is_joyous = BooleanVar()
        Checkbutton(self,text='Joyous',variable=self.is_joyous).grid(row=5,column=2,sticky=W)

        #electric Checkbutton
        self.is_electric = BooleanVar()
        Checkbutton(self,text='Electric',variable=self.is_electric).grid(row=6,column=3,sticky=W)

        #create variable for single body part
        self.body_part = StringVar()
        self.body_part.set(None)
        #create body part radio button
        body_parts = ['bellybutton','big toe','medulla oblongata']
        column=1
        for part in body_parts:
            Radiobutton(self,text=part,variable=self.body_part,value=part).grid(row=5,column=column,sticky=W)
            column+=1

        #create submit button
        Button(self,text='Click for story',command= self.tell_story).grid(row=6,column=0,sticky=W)
        self.story_txt = Text(self,width=75,height=10,wrap=WORD)
        self.story_txt.grid(row=7,column=0,columnspan=4)


    def tell_story(self):
        ''' Fill the text box with a new story based on information given '''
        #get values from GUI
        person=self.person_ent.get()
        noun = self.noun_ent.get()
        verb = self.verb_ent.get()
        adjectives = ''
        if self.is_itchy.get():
            adjectives+=" itchy"
            #joyous electric
        if self.is_joyous.get():
            adjectives+=' joyous'
        if self.is_electric.get():
            adjectives+= ' electric'
        body_part = self.body_part.get()

        #create story
        story = "The famous explorer "
        story+=person
        story += " had already given up a life-long quest to find The Lost City of "
        story+=noun.title()
        story+=" when one day,the "
        story+=noun
        story+= " found "
        story += person + '.'
        story+= "A strong, "
        story+= adjectives
        story+= 'peculiar feeling overwhelmed the explorer. '
        story+= 'After all this time,the quest was finally over.A tear came to '
        story+= person +"'s "
        story+=body_part+ '.'
        story += "And then, the "
        story += noun
        story += " promptly devoured "
        story += person + "."
        story += "The moral of the story? Be careful what you "
        story += verb
        story += " for."

        #display story
        self.story_txt.delete(0.0,END)
        self.story_txt.insert(0.0,story)

#main
root = Tk()
root.title('Mad Lib')
app = Application(root) #application instance
root.mainloop() #starts GIU
