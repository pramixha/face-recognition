from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self,root):
        self.root=root 
        self.root.title("Face Recognition System")
        self.root.geometry("1530x790+0+0")


        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1330,height=45)
        #Image
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

        #=========================button=======================
        b1_1=Button(self.root,text="Face Detector",cursor="hand2",command=self.face_recog,font=("times new roman",25,"bold"),bg="purple",fg="white")
        b1_1.place(x=0,y=200,width=1280,height=60)

        img4=Image.open(r"C:\Users\prami\Downloads\fece recognition\fece recognition\project images\tra.jpg")
        img4=img4.resize((1300,410))         
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=260,width=1290,height=410)
        #=====================attendance========================
    def mark_attendance(self,i,r,n,d):
        with open("fece recognition\suja.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((",")) 
                name_list.append(entry[0])
            if((i not in name_list)) and ((r not in name_list)) and ((n not in name_list)) and ((d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")




        #=================face Recognition==========================

    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)   #3
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="pramisha",database="facerecognition")
                my_cursor=conn.cursor()


                #my_cursor.execute("select Student_name from student where Student_id="+str(id))
                #n=my_cursor.fetchone()
                #n="+".join(n)
                my_cursor.execute("select Student_name from student where Student_id=" + str(id))
                n = my_cursor.fetchone()
                n = "+".join(n) if n else ''


                my_cursor.execute("select Roll_no from student where Student_id=" +str(id))
                r=str(my_cursor.fetchone()[0])
                r="".join(r) if r else ''

                #my_cursor.execute("select Department from student where Student_id="+str(id))
                #d=my_cursor.fetchone()
                #d="+".join(d)
                my_cursor.execute("select Department from student where Student_id=" + str(id))
                d = my_cursor.fetchone()
                d = "+".join(d) if d else ''
                #my_cursor.execute("select Student_id from student where Student_id="+str(id))
                #i=my_cursor.fetchone()
                #i="+".join(i)
                my_cursor.execute("select Student_id from student where Student_id=" + str(id))
                i = my_cursor.fetchone()
                i = "+".join(i) if i else ''

                if confidence>77:
                    cv2.putText(img,f"Student_id:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3) #3
                    cv2.putText(img,f"Roll_no:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3) #3
                    cv2.putText(img,f"Student_name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3) #3
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3) #3
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3) #3
                    cv2.putText(img,f"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3) #3
                coord=[x,y,w,h]

            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img    #hashtagged now by suja
            
        faceCascade=cv2.CascadeClassifier("fece recognition\haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
                ret,img=video_cap.read()
                #if not ret:
                    #break
                img=recognize(img,clf,faceCascade)
                cv2.imshow("Welcome To face Recognition",img)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)       
    root.mainloop()  