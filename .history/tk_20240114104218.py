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
my_button = Button(root, text='submit Button') #the button can be disabled by adding a state=DISABLED after the text. padx=50 and pady=50 changes the size pf the button
my_button.grid(row= 2, column= 0)

# create a button that calls a function. to add color to text you us the fg='color and the bg='color commands
def text_display():
    myLabel = Label(root, text='this is the text display function',bg='greeb').grid(row=4,column=3)

another_button = Button(root, text='call the func', command=text_display).grid(row=3, column=2)


root.mainloop()