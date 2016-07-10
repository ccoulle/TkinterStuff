#!/usr/bin/python

import os, sys
import Tkinter as tk

def quit():
  sys.exit()

if __name__ == '__main__':
  root = tk.Tk()
  root.title("A Label")
  root.bind('<Escape>', (lambda event: quit())) 
  label = tk.Label(root, text='Too Wide')
  label.pack()
  label.config(width=100, height=4, font=('symbol',20))
  root.mainloop()
