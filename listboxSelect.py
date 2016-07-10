#!/usr/bin/python
import Tkinter as tk

class Application():
  def __init__(self):
    self.root = tk.Tk()
    self.root.title('Listbox')

    self.scrollbar = tk.Scrollbar(self.root)
    self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    self.listbox = tk.Listbox(self.root, selectmode=tk.MULTIPLE)
    self.listbox.pack(side="top", fill="both", expand=True)
    self.initialize()

    self.scrollbar.config(command=self.listbox.yview)
    self.listbox.config(yscrollcommand=self.scrollbar.set)

    # The selection is one off with Button-1; gotta use ListboxSelect
    self.listbox.bind("<Double-1>", self.onDoubleClick)
    self.root.bind('<Escape>', lambda event: self.root.quit())

  def mainloop(self):
    self.root.mainloop()

  def initialize(self):
    for i in range(50):
      self.listbox.insert(tk.END, i*5)

  def onDoubleClick(self, event):
    widget = event.widget
    selection=widget.curselection()
    print "SELECTION:", selection
    for x in selection:
      value = widget.get(x)
      print "Value is", value

if __name__ == "__main__":
  app = Application()
  app.mainloop()
