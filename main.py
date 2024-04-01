from tkinter import*
import tkinter as tk
import tkinter
from tkinter import messagebox
from PIL import Image, ImageTk
from time import strftime
from datetime import datetime
import os
from student import Student
from train import Train
from facerecognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root 
        self.root.title("Face Recognition System")
        self.root.geometry("1530x790+0+0")
        self.root.configure(bg="white")

        img=Image.open(r"C:\Users\prami\Downloads\fece recognition\fece recognition\project images\bgfinal3.jpg")
        img=img.resize((500,200))         
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        img2=Image.open(r"C:\Users\prami\Downloads\fece recognition\fece recognition\project images\bgfinal3.jpg")
        img2=img2.resize((500,200))         
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=500,height=130)

        img3=Image.open(r"C:\Users\prami\Downloads\fece recognition\fece recognition\project images\bgfinal3.jpg")
        img3=img3.resize((500,200))         
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1000,y=0,width=500,height=130)

        # bg image
        img4=Image.open(r"C:\Users\prami\Downloads\fece recognition\fece recognition\project images\bgfinal1.jpg")
        img4=img4.resize((1430,510))         
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1430,height=510)

        title_lbl=Label(bg_img,text="FACE RECOGNITION SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1330,height=45)

        #time=================
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000,time)

        lbl = Label(title_lbl, font=('times new roman',14,'bold'), background = 'white', foreground = 'blue')
        lbl.place(x=0,y=0,width=110,height=45)
        time()

        #student button
        img5=Image.open(r"C:\Users\prami\Downloads\fece recognition\fece recognition\project images\std.jpg")
        img5=img5.resize((220,220))         
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=100,width=150,height=150)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="purple",fg="white")
        b1_1.place(x=100,y=250,width=150,height=40)

        #detect button
        img6=Image.open(r"C:\Users\prami\Downloads\fece recognition\fece recognition\project images\fd.jpg")
        img6=img6.resize((220,220))         
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.face_recognition)
        b1.place(x=400,y=100,width=150,height=150)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_recognition,font=("times new roman",15,"bold"),bg="purple",fg="white")
        b1_1.place(x=400,y=250,width=150,height=40)

        #attendance button
        img7=Image.open(r"C:\Users\prami\Downloads\fece recognition\fece recognition\project images\at.jpg")
        img7=img7.resize((220,220))         
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.attendance_data)
        b1.place(x=700,y=100,width=150,height=150)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="purple",fg="white")
        b1_1.place(x=700,y=250,width=150,height=40)

        #Help Desk button
        img8=Image.open(r"C:\Users\prami\Downloads\fece recognition\fece recognition\project images\hd.jpg")
        img8=img8.resize((220,220))         
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.help_data)
        b1.place(x=1000,y=100,width=150,height=150)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="purple",fg="white")
        b1_1.place(x=1000,y=250,width=150,height=40)

        #traning button
        img9=Image.open(r"C:\Users\prami\Downloads\fece recognition\fece recognition\project images\tr.jpg")
        img9=img9.resize((220,220))         
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,command=self.train_data,cursor="hand2")
        b1.place(x=100,y=300,width=150,height=150)

        b1_1=Button(bg_img,text="Train data",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="purple",fg="white")
        b1_1.place(x=100,y=450,width=150,height=40)

        #Photos button
        img10=Image.open(r"C:\Users\prami\Downloads\fece recognition\fece recognition\project images\p.jpg")
        img10=img10.resize((220,220))         
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,command=self.open_img,cursor="hand2")
        b1.place(x=400,y=300,width=150,height=150)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="purple",fg="white")
        b1_1.place(x=400,y=450,width=150,height=40)

        #Developer button
        img11=Image.open(r"C:\Users\prami\Downloads\fece recognition\fece recognition\project images\de.jpg")
        img11=img11.resize((220,220))         
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.developer_data,)
        b1.place(x=700,y=300,width=150,height=150)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="purple",fg="white")
        b1_1.place(x=700,y=450,width=150,height=40)

        #Quit button
        img12=Image.open(r"C:\Users\prami\Downloads\fece recognition\fece recognition\project images\q.jpg")
        img12=img12.resize((220,220))         
        self.photoimg12=ImageTk.PhotoImage(img12)

        b1=Button(bg_img,image=self.photoimg12,cursor="hand2",command=self.iExit)
        b1.place(x=1000,y=300,width=150,height=150)

        b1_1=Button(bg_img,text="Quit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="purple",fg="white")
        b1_1.place(x=1000,y=450,width=150,height=40)

    def open_img(self):
        os.startfile("fece recognition\data")

    def iExit(self):
        response = messagebox.askyesno("Face Recognition", "Are you sure you want to exit this project?")
        if response:
            self.root.destroy()
        else:
            return
        





        #=====================function button====================================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    def face_recognition(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    

    
    
    












if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)       
    root.mainloop()