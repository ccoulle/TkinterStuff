#!/usr/bin/python

import Tkinter as tk
import tkMessageBox
GEOMETRY='640x200'

'''Message boxes: showinfo, showwarning, showerror, askquestion,
   askokcancel, askyesno, askretrycancel'''

class App(object):
  def __init__(self):
    self.root = tk.Tk()
    self.root.geometry(GEOMETRY)
    self.root.title('Menus')
    self.root.config(bg='#FFFFCC')
    self.root.bind('<Escape>', lambda event: self.root.quit())
    self.toolFrame = tk.Frame(self.root)
    self.toolFrame.pack(side=tk.BOTTOM)
    self.makeLabel()
    self.makeToolbar()
    self.makeMenu()

  def makeLabel(self):
    label = tk.Label(self.root, width=50, height=5)
    label.config(text='This GUI has a menu', relief=tk.GROOVE)
    label.pack(padx=20, pady=20)

  def makeToolbar(self):
    quit = tk.Button(self.toolFrame, text='Exit', command=self.root.quit)
    quit.config(relief=tk.RAISED)
    quit.pack(padx=5, pady=5)

  def makeMenu(self):
    menubar = tk.Menu(self.root)
    menubar.config(bg='#ffad99')
    filemenu = tk.Menu(menubar, tearoff=1)
    filemenu.add_command(label='Load', command=self.notYet)
    filemenu.add_command(label='Save', command=self.notYet)
    filemenu.add_command(label='Exit', command=self.root.quit)
    menubar.add_cascade(menu=filemenu, label='File')
    editmenu = tk.Menu(menubar, tearoff=1)
    editmenu.add_command(label='Cut', command=self.notYet)
    editmenu.add_command(label='Copy', command=self.notYet)
    editmenu.add_command(label='paste', command=self.notYet)
    menubar.add_cascade(menu=editmenu, label='Edit')
    helpmenu = tk.Menu(menubar)
    helpmenu.add_command(label='Get Help', command=self.showWarning)
    menubar.add_cascade(menu=helpmenu, label='Help')
    self.root.config(menu=menubar)

  def mainloop(self):
    self.root.mainloop()

  def showWarning(self):
    tkMessageBox.showwarning('what', 'do you need help about?')

  def notYet(self):
    tkMessageBox.showinfo('Oops', 'Not implemented Yet!')

app = App()
app.mainloop()
