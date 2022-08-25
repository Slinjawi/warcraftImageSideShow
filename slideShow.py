import tkinter as tk
from tkinter import *
from PIL import Image
from PIL import ImageTk

csa = tk.Tk()
csa.geometry("700x800")

#Maybe should add function to add all files automatically
img = ImageTk.PhotoImage(Image.open("p.jpg"))
img2 = ImageTk.PhotoImage(Image.open("p1.jpg"))
img3 = ImageTk.PhotoImage(Image.open("p2.jpg"))
img4 = ImageTk.PhotoImage(Image.open("p3.jpg"))
img5 = ImageTk.PhotoImage(Image.open("p4.jpg"))
img6 = ImageTk.PhotoImage(Image.open("p5.jpg"))
img7 = ImageTk.PhotoImage(Image.open("p6.jpg"))
img8 = ImageTk.PhotoImage(Image.open("p7.jpg"))
img9 = ImageTk.PhotoImage(Image.open("p8.jpg"))
img10 = ImageTk.PhotoImage(Image.open("p9.jpg"))
img11 = ImageTk.PhotoImage(Image.open("p10.jpg"))
img12 = ImageTk.PhotoImage(Image.open("p11.jpg"))
img13 = ImageTk.PhotoImage(Image.open("p12.jpg"))

l = Label()
l.pack()


x = 1


def move_pic():
    global x
    if x == 13:
        x = 1
    if x == 1:
        l.config(image=img)
    elif x == 2:
        l.config(image=img2)
    elif x == 3:
        l.config(image=img3)
    elif x == 4:
        l.config(image=img4)
    elif x == 5:
        l.config(image=img5)
    elif x == 6:
        l.config(image=img6)
    elif x == 7:
        l.config(image=img7)
    elif x == 8:
        l.config(image=img8)
    elif x == 9:
        l.config(image=img9)
    elif x == 10:
        l.config(image=img10)
    elif x == 11:
        l.config(image=img11)
    elif x == 12:
        l.config(image=img12)
    elif x == 13:
        l.config(image=img13)
    x += 1
    csa.after(2000, move_pic)


move_pic()
csa.mainloop()