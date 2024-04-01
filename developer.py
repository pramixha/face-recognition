from tkinter import*
from tkinter import ttk
from tokenize import String
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import cv2.face
import os
import numpy as np

class Developer:
    def __init__(self,root):
        self.root=root 
        self.root.title("Face Recognition System")
        self.root.geometry("1530x790+0+0")
        self.root.configure(bg="white")

        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1330,height=55)

        img=Image.open(r"C:\Users\prami\Downloads\fece recognition\fece recognition\project images\devss1.jpg")
        img=img.resize((1300,600))         
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=52,width=1290,height=600)

        #frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=750,y=0,width=500,height=500)

        img1=Image.open(r"C:\Users\prami\Downloads\fece recognition\fece recognition\project images\de.jpg")
        img1=img1.resize((200,200))         
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(main_frame,image=self.photoimg1)
        f_lbl.place(x=275,y=20,width=200,height=200)

        #Developer info
        dev_label=Label(main_frame,text="Suja",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=3,y=40)
        dev_label=Label(main_frame,text="III Bca Honours",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=3,y=80)

        img2=Image.open(r"C:\Users\prami\Downloads\fece recognition\fece recognition\project images\de.jpg")
        img2=img2.resize((200,200))         
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(main_frame,image=self.photoimg2)
        f_lbl.place(x=275,y=260,width=200,height=200)

        #Developer info
        dev_label=Label(main_frame,text="Pramisha",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=3,y=300)
        dev_label=Label(main_frame,text="III Bca Honours",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=3,y=340)



        
        

if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)       
    root.mainloop()  