from tkinter import *
from PIL import Image, ImageTk

root= Tk()
root.title('My Image app')
root.iconbitmap('love.ico')

quitter= Button(root, text='Exit',padx=40, command= root.quit, bg='green', fg='white')
quitter.pack()
root.mainloop()