from tkinter import *

root = Tk()
root.title('my calculator')  #this assigns the top titleto the gui

# create an entry field
entry =Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10,pady=10)

root.mainloop()