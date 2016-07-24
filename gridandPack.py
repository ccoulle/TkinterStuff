import Tkinter as tk

names = ['Frodo', 'Sam', 'Gandalf', 'Boromir', 'Galadriel',
         'Gimli', 'Legoloas', 'Elrond', 'Merry', 'Pippin']

def printVal(event):
  widget = event.widget
  print widget.get()

root = tk.Tk()
root.bind('<Escape>', lambda event: root.quit())
root.title('Grids and toolbars')

quitFrame = tk.Frame(root)
quitFrame.pack(side=tk.BOTTOM)
quit = tk.Button(quitFrame, text='Exit', command=root.quit)
quit.pack(side=tk.LEFT)

gridFrame = tk.Frame(root)
gridFrame.pack()
count = 0
for n in names:
  l = tk.Label(gridFrame, text=n)
  l.grid(row=count, column=0)
  e = tk.Entry(gridFrame)
  e.insert(tk.END, str(count*10))
  e.bind('<Return>', printVal)
  e.grid(row=count, column=1)
  count += 1

root.mainloop()
