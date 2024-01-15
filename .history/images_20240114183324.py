from tkinter import *
from PIL import Image, ImageTk

root= Tk()
root.title('My Image app')
root.iconbitmap('heart_20.png')

quitter= Button(root, text='Exit',padx=40, command= root.quit, bg='green', fg='white')
quitter.pack()
root.mainloop()