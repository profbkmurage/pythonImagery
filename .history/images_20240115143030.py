from tkinter import *
from PIL import Image, ImageTk

root= Tk()
root.title('My Image app')
root.iconbitmap('love.ico')


my_image= ImageTk.PhotoImage(Image.open('img/1.jpg'))
my_image1= ImageTk.PhotoImage(Image.open('img/2.jpg'))
my_image2= ImageTk.PhotoImage(Image.open('img/3.jpg'))
my_image3= ImageTk.PhotoImage(Image.open('img/4.jpg'))
my_image4= ImageTk.PhotoImage(Image.open('img/5.jpg'))
my_image5= ImageTk.PhotoImage(Image.open('img/6.jpg'))

my_image6= Image.open('img/7.jpg')
resized = my_image6.thumbnail((300,300))
print(resized.__sizeof__)


image_list=[my_image,my_image1,my_image2,my_image3,my_image4,my_image5,resized]
label= Label(image=my_image)
label.grid(row=0, column=0,columnspan=3)

status_bar = Label(root, text='image 1 of '+ str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)


def forward(image_number):
    global label
    global button_forward
    global button_backward
    if image_number<len(image_list):
        label.grid_forget()
        label= Label(image= image_list[image_number-1])
        button_forward= Button(root, text='>>',padx=40, command= lambda:forward(image_number +1), bg='orange', fg='white').grid(row=1, column=2)
        button_backward= Button(root, text='<<',padx=40, command=lambda:backward(image_number-1), bg='blue', fg='white').grid(row=1, column=0)

    else: 
        button_forward= Button(root,text='Reached the End', state=DISABLED).grid(row=1, column=2) 
        button_backward= Button(root, text='<<',padx=40, command=lambda:backward(image_number-1), bg='blue', fg='white').grid(row=1, column=0)

    status_bar = Label(root, text=f'image {image_number} of '+ str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status_bar.grid(row=2, column=0, columnspan=3, sticky=W + E)
    label.grid(row=0, column=0,columnspan=3)


def backward(image_number):
    global label
    global button_forward
    global button_backward
    if image_number==1:
        button_backward= Button(root, text='nothing more',padx=40, bg='blue', fg='white',state=DISABLED).grid(row=1, column=0)
    else:
        label.grid_forget()
        label= Label(image= image_list[image_number-1])
        button_forward= Button(root, text='>>',padx=40, command= lambda:forward(image_number +1), bg='orange', fg='white').grid(row=1, column=2)
        button_backward= Button(root, text='<<',padx=40, command=lambda:backward(image_number-1), bg='blue', fg='white').grid(row=1, column=0)
        
    status_bar = Label(root, text=f'image {image_number} of '+ str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status_bar.grid(row=2, column=0, columnspan=3, sticky=W+ E)
     

    label.grid(row=0, column=0,columnspan=3)

button_backward= Button(root, text='<<',padx=40, command=backward, bg='blue', fg='white',state=DISABLED).grid(row=1, column=0)
quitter= Button(root, text='Exit',padx=40, command= root.quit, bg='green', fg='white').grid(row=1, column=1)
button_forward= Button(root, text='>>',padx=40, command= lambda:forward(2), bg='orange', fg='white',pady=10).grid(row=1, column=2)

status_bar.grid(row=2, column=0, columnspan=3, sticky=W+ E)
root.mainloop() 