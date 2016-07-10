#!/usr/bin/python

import os, sys
import Tkinter as tk

def quit():
  sys.exit()

if __name__ == '__main__':
  root = tk.Tk()
  root.title("A Label")
  root.bind('<Escape>', (lambda event: quit())) 
  label = tk.Label(root, text='Too Small')
  label.config(width=20, height=5, font=('Symbol', 22))
  label.config(bg='#ff0000', relief=tk.SUNKEN, padx=5, pady=5)
  label.pack()
  root.mainloop()
