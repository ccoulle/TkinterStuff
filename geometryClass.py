#!/usr/bin/python

import os, sys
import Tkinter as tkinter

TITLE = "Learning Tkinter: Label"
GEOMETRY = '640x480+200+100'
class Labels(object):
  def __init__(self):
    self.screen = tkinter.Tk()
    self.screen.geometry(GEOMETRY)
    self.screen.title(TITLE)
    self.screen.bind('<Escape>', (lambda event: self.quit())) 
    self.init()
    self.screen.mainloop()

  def init(self):
    labelFont = ('times', 20, 'bold')
    label = tkinter.Label(self.screen, text = "Hello World")
    label.config(bg='black', fg='yellow')
    label.config(font=labelFont, height=3, width=20)
    label.pack(expand=tkinter.YES, fill=tkinter.BOTH)

  def quit(self):
    sys.exit()


if __name__ == '__main__':
  template = Labels()
