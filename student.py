from tkinter import*
from tkinter import ttk
from tokenize import String
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import cv2.face





class Student:
    def __init__(self,root):
        self.root=root 
        self.root.title("Face Recognition System")
        self.root.geometry("1530x790+0+0")
        self.root.configure(bg="white")

        #variables
        
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_studentId=StringVar()
        self.var_studentName=StringVar()
        self.var_gender=StringVar()
        self.var_rollno=StringVar()
        

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

        title_lbl=Label(bg_img,text="STUDENT DETAILS",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1330,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=55,width=1255,height=445)

        #left label frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=600,height=420)


        img_left=Image.open(r"C:\Users\prami\Downloads\fece recognition\fece recognition\project images\bgfinal1.jpg")
        img_left=img_left.resize((600,200))         
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=6,y=0,width=585,height=50)

        
        #current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=6,y=50,width=585,height=120)
       
        #Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Department","ARTS","MEDICAL","ENGINEERING")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        dep_entry=ttk.Entry(current_course_frame,textvariable=self.var_dep,width=17,font=("times new roman",12,"bold"))
        dep_entry.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=17,state="readonly")
        course_combo["values"]=("Select Course","BCOM","BCA HONS","PHARMACY","EEE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="readonly")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #class student information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="class student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=6,y=180,width=585,height=210)

        #student id
        studentId_label=Label(class_student_frame,text="Student Id:",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_studentId,width=17,font=("times new roman",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        #student name
        studentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_studentName,width=17,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)

        #Gender
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=1,column=0,padx=7,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=15,state="readonly")
        gender_combo["values"]=("Select gender","Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=1,padx=7,pady=5,sticky=W)

        #Roll No
        rollno_label=Label(class_student_frame,text="Roll No:",font=("times new roman",12,"bold"),bg="white")
        rollno_label.grid(row=1,column=2,padx=7,pady=5,sticky=W)

        rollno_entry=ttk.Entry(class_student_frame,textvariable=self.var_rollno,width=17,font=("times new roman",12,"bold"))
        rollno_entry.grid(row=1,column=3,padx=7,pady=5,sticky=W)

        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=10,column=0)

        
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=10,column=1)

        #buttons frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=4,y=105,width=570,height=30)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=15,font=("times new roman",12,"bold"),bg="purple",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=15,font=("times new roman",12,"bold"),bg="purple",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=15,font=("times new roman",12,"bold"),bg="purple",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("times new roman",12,"bold"),bg="purple",fg="white")
        reset_btn.grid(row=0,column=3)

        #buttons frame
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=5,y=145,width=570,height=30)

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=31,font=("times new roman",12,"bold"),bg="purple",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=31,font=("times new roman",12,"bold"),bg="purple",fg="white")
        update_photo_btn.grid(row=0,column=1)
        
        #Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=620,y=10,width=610,height=420)

        img_right=Image.open(r"C:\Users\prami\Downloads\fece recognition\fece recognition\project images\bgfinal1.jpg")
        img_right=img_right.resize((600,200))         
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=6,y=0,width=593,height=50)

        #search system
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=7,y=50,width=593,height=63)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="purple")
        search_label.grid(row=0,column=0,padx=7,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),width=15,state="readonly")
        search_combo["values"]=("Select","Roll No","Student id ","Year")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=7,pady=5,sticky=W)

        search_entry=ttk.Entry(search_frame,width=17,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=8,pady=5,sticky=W)

        #rightframebuttons
        search_btn=Button(search_frame,text="Search",width=8,font=("times new roman",12,"bold"),bg="purple",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showall_btn=Button(search_frame,text="Show All",width=8,font=("times new roman",12,"bold"),bg="purple",fg="white")
        showall_btn.grid(row=0,column=4,padx=4)

        #table frame
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=7,y=130,width=593,height=255)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","studentId","studentName","gender","rollno","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("studentId",text="Student Id")
        self.student_table.heading("studentName",text="Student Name")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("rollno",text="Roll No")
        self.student_table.heading("photo",text="Photo Status")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width="100")
        self.student_table.column("course",width="100")
        self.student_table.column("year",width="100")
        self.student_table.column("studentId",width="100")
        self.student_table.column("studentName",width="100")
        self.student_table.column("gender",width="100")
        self.student_table.column("rollno",width="100")
        self.student_table.column("photo",width="100")
        

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()



        #function declaration
    def add_data(self):

        if self.var_dep.get()=="Select Department"or self.var_studentName.get()=="" or self.var_studentId.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="pramisha",database="facerecognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                    
                                                                        self.var_dep.get(),
                                                                        self.var_course.get(),
                                                                        self.var_year.get(),
                                                                        self.var_studentId.get(),
                                                                        self.var_studentName.get(),
                                                                        self.var_gender.get(),
                                                                        self.var_rollno.get(),
                                                                        self.var_radio1.get()

                                                                                    ))
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details Has Been Added Successfully",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)  

     #fetchdata
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="pramisha",database="facerecognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select*from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()    
        conn.close()  
    #get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_studentId.set(data[3]),
        self.var_studentName.set(data[4]),
        self.var_gender.set(data[5]),
        self.var_rollno.set(data[6]),
        self.var_radio1.set(data[7])

    #update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_studentName.get()=="" or self.var_studentId.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do You Want To Update This Student Details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="pramisha",database="facerecognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Student_name=%s,Gender=%s,Roll_no=%s,Photo_Sample=%s where Student_id=%s",(


                                                                                                                                            self.var_dep.get(),
                                                                                                                                            self.var_course.get(),
                                                                                                                                            self.var_year.get(),
                                                                                                                                            self.var_studentName.get(),
                                                                                                                                            self.var_gender.get(),
                                                                                                                                            self.var_rollno.get(),
                                                                                                                                            self.var_radio1.get(),
                                                                                                                                            self.var_studentId.get()



                                                                                                                                                                    ) )
                    
                else:
                    if  not Update:
                        return
                messagebox.showinfo("Success","Student Details Has Been Updated Successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


#delete function
    def delete_data(self):
        if self.var_studentId.get()=="":
            messagebox.showerror("Error","Student Id Must Be Required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do You Want To Delete This Student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="pramisha",database="facerecognition")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_studentId.get(),)
                    my_cursor.execute(sql,val)                                                                                                                             
                else:
                    if  not delete:
                        return
                messagebox.showinfo("Delete","Student Details Has Been Deleted Successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    # reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")                                                              
        self.var_year.set("Select Year")
        self.var_studentId.set("Select StudentId")
        self.var_studentName.set("Select StudentName")
        self.var_gender.set("Select Gender")
        self.var_rollno.set("Select RollNo")
        self.var_radio1.set("Select Radio1")

        #take photo sample
        
        #==========================generate data set or take photo sample==========================
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_studentName.get()=="" or self.var_studentId.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="pramisha",database="facerecognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Student_name=%s,Gender=%s,Roll_no=%s,Photo_Sample=%s where Student_id=%s",(


                                                                                                                                            self.var_dep.get(),
                                                                                                                                            self.var_course.get(),
                                                                                                                                            self.var_year.get(),
                                                                                                                                            self.var_studentName.get(),
                                                                                                                                            self.var_gender.get(),
                                                                                                                                            self.var_rollno.get(),
                                                                                                                                            self.var_radio1.get(),
                                                                                                                                            self.var_studentId.get()==id+1



                                                                                                                                                                    ) )
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #=============load predefine data on face frontals from opencv=====================================
                
                face_classifier = cv2.CascadeClassifier("fece recognition\haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #minimum neighbour=5
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped        
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="fece recognition\\data\\user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()

                messagebox.showinfo("Result","Generating Data Sets Completed!!!")

            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

            






if __name__ == "__main__":
    root=Tk()
    obj=Student(root)       
    root.mainloop()        