from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk

class Login:
    def __init__(self,root):
        self.root=root 
        self.root.title("Face Recognition System")
        self.root.geometry("1530x790+0+0")
        self.root.configure(bg="white")
        img=Image.open(r"C:\Users\prami\Downloads\fece recognition\fece recognition\project images\bgfinal3.jpg")
        img=img.resize((500,300))         
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=250)

        img2=Image.open(r"C:\Users\prami\Downloads\fece recognition\fece recognition\project images\bgfinal3.jpg")
        img2=img2.resize((500,300))         
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=500,height=250)

        img3=Image.open(r"C:\Users\prami\Downloads\fece recognition\fece recognition\project images\bgfinal3.jpg")
        img3=img3.resize((500,300))         
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1000,y=0,width=500,height=250)

        # bg image
        img4=Image.open(r"C:\Users\prami\Downloads\fece recognition\fece recognition\project images\bgfinal1.jpg")
        img4=img4.resize((1430,510))         
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=230,width=1430,height=510)

        frame=Frame(self.root,bg="black")
        frame.place(x=495,y=115,width=340,height=450)


        img6=Image.open(r"C:\Users\prami\Downloads\fece recognition\fece recognition\project images\std.jpg")
        img6=img6.resize((120,120))         
        self.photoimg6=ImageTk.PhotoImage(img6)

        f_lbl=Label(self.root,image=self.photoimg6)
        f_lbl.place(x=630,y=115,width=80,height=80)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=105,y=110)



       






if __name__ == "__main__":
    root=Tk()
    obj=Login(root)       
    root.mainloop() 