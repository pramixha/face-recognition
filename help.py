from tkinter import*
from tkinter import ttk
from tokenize import String
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import cv2.face
import os
import numpy as np

class Help:
    def __init__(self,root):
        self.root=root 
        self.root.title("Face Recognition System")
        self.root.geometry("1530x790+0+0")
        self.root.configure(bg="white")

        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1330,height=55)

        img=Image.open(r"C:\Users\prami\Downloads\fece recognition\fece recognition\project images\hhd.jpg")
        img=img.resize((1300,600))         
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=52,width=1290,height=600)

        dev_label=Label(f_lbl,text="Email:sujajubiya15@gmail.com",font=("times new roman",20,"bold"),bg="purple")
        dev_label.place(x=5,y=10)
        dev_label=Label(f_lbl,text="Email:pramishawcm123@gmail.com",font=("times new roman",20,"bold"),bg="purple")
        dev_label.place(x=825,y=10)




if __name__ == "__main__":
    root=Tk()
    obj=Help(root)       
    root.mainloop()  