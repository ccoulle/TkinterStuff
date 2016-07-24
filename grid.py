import Tkinter as tk
GEOMETRY = '380x280'

names = ['Frodo', 'Sam', 'Gandalf', 'Boromir', 'Galadriel',
         'Gimli', 'Legoloas', 'Elrond', 'Merry', 'Pippin']

class App(object):
  def __init__(self):
    self.root = tk.Tk()
    self.root.bind("<Escape>", lambda event: self.root.quit())
    self.root.geometry(GEOMETRY)
    self.makeGrid()

  def makeGrid(self):
    r = 0
    for n in names:
      label = tk.Label(self.root, text=n, width=15, relief=tk.RIDGE)
      label.grid(row=r, column=0)
      entry = tk.Entry(self.root, width=25, relief=tk.SUNKEN,bg='#00FF00')
      entry.insert(0, str(r*100))
      entry.bind('<Double-1>', self.getGridEntry)
      entry.grid(row=r, column=1)
      r += 1

    label = tk.Label(self.root, text='New Row', width=15, relief=tk.RIDGE)
    label.grid(row=len(names), column=0)
    entry = tk.Entry(self.root, width=25, relief=tk.SUNKEN,bg='#00FF00')
    entry.insert(0, "Pokemon  Go")
    entry.bind('<Double-1>', self.getGridEntry)
    entry.grid(row=len(names), column=1)


  def getGridEntry(self, event):
    name = event.widget.get()
    print name

  def mainloop(self):
    self.root.mainloop()

if __name__ == "__main__":
  app = App()
  app.mainloop()
