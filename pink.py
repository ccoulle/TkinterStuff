#!/usr/bin/python

import os, sys
import Tkinter as tkinter

TITLE = "Learning Tkinter: Label"
class Labels(object):
  def __init__(self):
    self.screen = tkinter.Tk()
    self.screen.title(TITLE)
    self.screen.bind('<Escape>', (lambda event: self.quit())) 
    self.init()
    self.screen.mainloop()

  def init(self):
    labelFontTuple = ('times', 20, 'bold')
    label = tkinter.Label(self.screen, text = "Hello World")
    # fg sets the foreground, which in this case is the font:
    label.config(bg='pink', fg='blue')
    # height is in lines, width is in characters;
    # this config is optional but we want the widget to be larger,
    # than what the geometry manager would make it:
    label.config(font=labelFontTuple, height=7, width=20)
    label.pack(expand=tkinter.YES, fill=tkinter.BOTH)

  def quit(self):
    sys.exit()


if __name__ == '__main__':
  template = Labels()
