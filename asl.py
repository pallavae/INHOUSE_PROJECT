import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk

def application():
    root.destroy()
    import app

def contact():
    root.destroy()
    import contact

root=Tk()
root.title("Login")
root.geometry("1530x790")

img=Image.open(r"C:\Users\ASUS\LastHope\images\wallpaper.jpg")
img=img.resize((1530,790),Image.ANTIALIAS)
photoimg=ImageTk.PhotoImage(img)
lbl=Label(root,image=photoimg)
lbl.place(x=0,y=0)

newPage=Button(root,text='Try Me',font =("Helvetica", 20, "bold italic"),fg='black',bg='light pink'
                        ,cursor='hand2',bd=0,command=application)
newPage.place(x=1350,y=25)

ContactUs=Button(root,text='Contact Us',font =("Helvetica", 20, "bold italic"),fg='black',bg='light pink'
                        ,cursor='hand2',bd=0,command=contact)
ContactUs.place(x=1100,y=25)

root.mainloop()