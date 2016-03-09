#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *
import tkMessageBox
import tkFileDialog
import xlrd
import os

class MainPanel(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack(expand = 1, fill='both',padx = 5, pady = 5)
        self.createWidgets()

    def createWidgets(self):
        padxPx = 10
        padyPx = 10
        self.dirLabel = Label(self, text=u'工程目录',font = 18)
        self.dirLabel.grid(row = 0)
        self.nameEntry = Entry(self,font = 18,bd = 2, fg = 'red')
        self.nameEntry.grid(row = 0 , column = 1,columnspan=2)
        self.quiteButton = Button(self, text='Quit', command=self.selectExcel, relief=GROOVE)
        self.quiteButton.grid(row = 0 , column = 3)

    def selectExcel(self):
        rootDirPath =  os.path.expanduser('~')
        fileTyps = [('xlx / xlsx files', '.xl*'),('all files', '.*')]
        file = tkFileDialog.askopenfilename(initialdir = rootDirPath , filetypes = fileTyps)
        # file = u'/home/wangxiaoyang/share/FineOS应用支持的语言表_QL613.xlsx'
        print file
        if(len(file) > 0) :
            data = xlrd.open_workbook(file)
            sheets = data.sheets();
            nTable = len( sheets )
            for index in range(nTable) :
                table = data.sheet_by_index(index)
                nRows = table.nrows
                nCols = table.ncols
                for row in range(nRows) :
                    for col in range(nCols) :
                        print "row_%d col_%d : %s" % ( row , col, table.cell(row,col).value )


rt = Tk()
# update window ,must do
rt.update()
# get screen width and height
scnWidth,scnHeight = rt.maxsize()
# get current width
rWidth = 0.5 * scnWidth
# get current height
rHeight = 0.5 * scnHeight
# now generate configuration information
tmpcnf = '%dx%d+%d+%d' % (rWidth, rHeight, (scnWidth - rWidth) / 2, (scnHeight - rHeight) / 2)
rt.geometry(tmpcnf)
rt.title('Hello GUI')
mainPanel = MainPanel(rt)
rt.mainloop()