from tkinter import *
from PIL import Image, ImageTk

root= Tk()
root.title('My Image app')
root.iconbitmap('love.ico')


my_image= ImageTk.PhotoImage(Image.open('img/6.jpg'))
my_image1= ImageTk.PhotoImage(Image.open('img/6.jpg'))
my_image2= ImageTk.PhotoImage(Image.open('img/6.jpg'))
my_image3= ImageTk.PhotoImage(Image.open('img/6.jpg'))
my_image4= ImageTk.PhotoImage(Image.open('img/6.jpg'))
my_image5= ImageTk.PhotoImage(Image.open('img/6.jpg'))
label= Label(image=my_image)
label.grid(row=0, column=0,columnspan=3)
 

backward= Button(root, text='<<',padx=40, command= root.quit, bg='blue', fg='white').grid(row=1, column=0)
quitter= Button(root, text='Exit',padx=40, command= root.quit, bg='green', fg='white').grid(row=1, column=1)
forward= Button(root, text='>>',padx=40, command= root.quit, bg='orange', fg='white').grid(row=1, column=2)
root.mainloop() 