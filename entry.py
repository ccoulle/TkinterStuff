#!/usr/bin/python

'''
  Brian Malloy
  An example of an Entry widget, getting, and displaying the info.
'''

import os, sys
import Tkinter as tk

def quit():
  sys.exit()

class EntryWidget(object):
  def __init__(self, root):
    labelFont = ('Symbol', 12)
    label = tk.Label(root, text = "Type text and press enter")
    label.config(font=labelFont, bd=5, relief=tk.SUNKEN)
    label.config(height=2)
    label.pack()

    self.entry = tk.Entry(root)
    #self.entry.insert(0, "Type text:")
    self.entry.bind('<Return>', lambda event: self.displayEntryInfo())
    self.entry.config(width=25, font=labelFont)
    self.entry.pack(side=tk.TOP)
    self.entry.focus()

  def displayEntryInfo(self):
    print self.entry.get()

if __name__ == '__main__':
  root = tk.Tk()
  root.title("Buttons")
  root.bind('<Escape>', (lambda event: quit())) 
  entryWidget = EntryWidget(root)
  root.mainloop()
