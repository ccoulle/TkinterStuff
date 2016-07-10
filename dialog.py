#!/usr/bin/python
import sys
import Tkinter as tk
import tkMessageBox

ErrorMsg = "Sorry, no spam allowed?"
def callback():
  if tkMessageBox.askyesno('Verify', 'Do you really want to quit?'):
    #tkMessageBox.showwarning('Yes' 'Quit not implemented')
    sys.exit()
  else:
    tkMessageBox.showinfo('No', 'Quit has been canceled')

tk.Button(text="Quit", command=callback).pack()
button = tk.Button(text="Spam",
         command=(lambda: tkMessageBox.showerror('Spam', ErrorMsg)))
button.pack()
tk.mainloop()
