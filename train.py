from tkinter import*
from tkinter import ttk
from tokenize import String
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import cv2.face
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root 
        self.root.title("Face Recognition System")
        self.root.geometry("1530x790+0+0")
        self.root.configure(bg="white")

        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1330,height=45)

        img=Image.open(r"C:\Users\prami\Downloads\fece recognition\fece recognition\project images\bgfinal3.jpg")
        img=img.resize((500,200))         
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=50,width=500,height=150)

        img2=Image.open(r"C:\Users\prami\Downloads\fece recognition\fece recognition\project images\bgfinal3.jpg")
        img2=img2.resize((1000,200))         
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=50,width=500,height=150)

        img3=Image.open(r"C:\Users\prami\Downloads\fece recognition\fece recognition\project images\bgfinal3.jpg")
        img3=img3.resize((500,200))         
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1000,y=50,width=500,height=150)

        #============================button=======================
        b1_1=Button(self.root,text="Train Data",cursor="hand2",command=self.train_classifier,font=("times new roman",25,"bold"),bg="purple",fg="white")
        b1_1.place(x=0,y=200,width=1280,height=60)

        img4=Image.open(r"C:\Users\prami\Downloads\fece recognition\fece recognition\project images\bgfinal2.jpg")
        img4=img4.resize((1300,410))         
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=260,width=1290,height=410)

    def train_classifier(self):
        data_dir=("fece recognition\data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')  #GRAY SCALE IMAGE
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #===========================train the classifier and save===========
        
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training data sets completed!!",parent=self.root)



            



        








if __name__ == "__main__":
    root=Tk()
    obj=Train(root)       
    root.mainloop()  



        