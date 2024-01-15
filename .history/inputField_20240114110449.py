from tkinter import *

root = Tk()


# create an entry widget
entry = Entry(root, width=100)
entry.pack()
entry.insert(0,'enter your name') #this give the entry field a placeholder


root.mainloop()