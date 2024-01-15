from tkinter import *
from PIL import Image, ImageTk

root= Tk()
root.title('My Image app')
root.iconbitmap('love.ico')


my_image= ImageTk.PhotoImage(Image.open('love.jpg'))
label= Label(image=my_image)
label.grid(row=1, column=2, columnspan=10)


quitter= Button(root, text='Exit',padx=40, command= root.quit, bg='green', fg='white')
quitter.pack()
root.mainloop()