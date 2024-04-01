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
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root 
        self.root.title("ATTENDANCE")
        self.root.geometry("1530x790+0+0")

        #===================variable===================
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        


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

        title_lbl=Label(bg_img,text="ATTENDANCE",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1330,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=55,width=1255,height=445)

    #left label frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=600,height=420)


        img_left=Image.open(r"C:\Users\prami\Downloads\fece recognition\fece recognition\project images\bgfinal1.jpg")
        img_left=img_left.resize((600,200))         
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=6,y=0,width=585,height=50)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=5,y=55,width=588,height=320)

        #Label and enrty
        #attendance id
        attendanceIdLabel=Label(left_inside_frame,text="AttendanceId:",font=("comicsans","11","bold"),bg="white")
        attendanceIdLabel.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        attendanceId_entry=ttk.Entry(left_inside_frame,width=17,textvariable=self.var_atten_id,font=("times new roman",12,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)
        #atten_attendanceId=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_attendanceId,font="comicsans 11 bold")
        #atten_attendanceId.grid(row=0,column=3,pady=5)
 
        #roll
        rollLabel=Label(left_inside_frame,text="Roll",bg="white",font="comicsans 11 bold")
        rollLabel.grid(row=0,column=2,padx=4,pady=5)

        atten_roll=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_roll,font="comicsans 11 bold")
        atten_roll.grid(row=0,column=3,pady=5)


        #name
        nameLabel=Label(left_inside_frame,text="Name",bg="white",font="comicsans 11 bold")
        nameLabel.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        atten_name=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_name,font="comicsans 11 bold")
        atten_name.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        #dep
        depLabel=Label(left_inside_frame,text="Department",bg="white",font="comicsans 11 bold")
        depLabel.grid(row=1,column=2,padx=4,pady=5)

        atten_dep=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_dep,font="comicsans 11 bold")
        atten_dep.grid(row=1,column=3,pady=5)

        #time
        timeLabel=Label(left_inside_frame,text="Time",bg="white",font="comicsans 11 bold")
        timeLabel.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        atten_time=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_time,font="comicsans 11 bold")
        atten_time.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        #date
        dateLabel=Label(left_inside_frame,text="Date",bg="white",font="comicsans 11 bold")
        dateLabel.grid(row=2,column=2,padx=4,pady=5)

        atten_date=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_date,font="comicsans 11 bold")
        atten_date.grid(row=2,column=3,pady=5)

        #attendance
        attendanceLabel=Label(left_inside_frame,text="Attendance Status",bg="white",font="comicsansns 11 bold")
        attendanceLabel.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)
        
        #buttons frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=4,y=250,width=570,height=30)

        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=15,font=("times new roman",12,"bold"),bg="purple",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=15,font=("times new roman",12,"bold"),bg="purple",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",width=15,font=("times new roman",12,"bold"),bg="purple",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("times new roman",12,"bold"),bg="purple",fg="white")
        reset_btn.grid(row=0,column=3)




    #right lable
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=620,y=10,width=610,height=420)

        img_right=Image.open(r"C:\Users\prami\Downloads\fece recognition\fece recognition\project images\bgfinal1.jpg")
        img_right=img_right.resize((600,200))         
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=6,y=0,width=593,height=50)
    #right frame
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=55,width=588,height=320)
    #=======================scroll===========================
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll no")
        self.AttendanceReportTable.heading("name",text="Student name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


    #=========================fetch data=====================================

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    #importcsv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
    #exportcsv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.write(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"sucessfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_dep.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_id.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
        







        





if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)       
    root.mainloop()