#!/usr/bin/python
# -*- coding : utf-8 -*-

from Tkinter import *
import tkMessageBox

class HelloFrame(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        # self.helloLabel = Label(self,text='Hello GUI............')
        # self.helloLabel.pack()
        self.nameEntry = Entry(self)
        self.nameEntry.pack()
        self.quiteButton = Button(self,text='Quit',command=self.printName)
        self.quiteButton.pack()

    def printName(self):
        name = self.nameEntry.get() or 'Xiaoyang'
        tkMessageBox.showinfo('Message','name is %s !' % name)

hello = HelloFrame()
hello.master.title('Hello GUI!')
hello.mainloop()