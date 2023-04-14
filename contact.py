import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import subprocess

def Back():
    contactwindow.destroy()
    subprocess.call(["python","asl.py"])

contactwindow=Tk()
contactwindow.title("Be My Voice")
contactwindow.geometry("1530x790")

img=Image.open(r"C:\Users\ASUS\LastHope\images\contact.jpg")
img=img.resize((1530,790),Image.ANTIALIAS)
photoimg=ImageTk.PhotoImage(img)
lbl=Label(contactwindow,image=photoimg)
lbl.place(x=0,y=0)

Back=Button(contactwindow,text='Back',font =("Helvetica", 20, "bold italic"),fg='black',bg='white'
                        ,cursor='hand2',bd=0,command=Back)
Back.place(x=1400,y=720)

contactwindow.mainloop()