from tkinter import *

root = Tk()

my_label = Label(root, text='This is prof BKMurage creating a GUI App on Python')
my_label1 = Label(root, text='Hello fellas and welcome to GUI class 1')

# packing just [laces the stuff in the center of the window]
# my_label.pack()

# grid takes in a parameter of row and column
my_label.grid(row= 0, column= 0)
my_label1.grid(row= 1, column= 0)

# a button is a widget
my_button = Button(root, text='submit Button')
my_button.grid(row= 2, column= 0)


root.mainloop()