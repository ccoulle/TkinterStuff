#!/usr/bin/python

import os, sys
import Tkinter as tk

def quit():
  sys.exit()

if __name__ == '__main__':
  root = tk.Tk()
  root.title("A Button")
  root.bind('<Escape>', (lambda event: quit())) 

  frame = tk.Frame(root)
  frame.pack(side=tk.TOP)

  label1 = tk.Label(frame, text='Hello', bg='#00ff00')
  label1.pack(side=tk.LEFT, padx=5, pady=5)
  label1.config(width=20, height=3, relief=tk.RAISED, bd=5)

  label2 = tk.Label(frame, text='World', bg='#0000ff')
  label2.pack(side=tk.RIGHT, padx=5, pady=5)
  label2.config(width=20, height=3, relief=tk.RAISED, bd=5)

  button = tk.Button(root, text='Push me', command=quit)
  button.config(width=20, height=3, bg='#ff0000', relief=tk.SUNKEN, bd=5)
  button.pack(side=tk.BOTTOM, padx=5, pady=5)
  root.mainloop()
