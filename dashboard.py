from tkinter import *
from PIL import Image, ImageTk
from course import CourseClass
from student import StudentClass
from result import resultClass
from viewresult import reportClass
from tkinter import messagebox
import sqlite3
import os
import subprocess
class PROJECTZ:
    def __init__(self, root):
       self.root=root
       self.root.title("student result management system")
       self.root.geometry("1350x700+0+0")
       self.root.config(bg="white")
       #===title===
       title=Label(self.root,text="student result management system",font=("goudy old style",20,"bold"),bg="black",fg="white").place(x=0,y=0,relwidth=1,height=50)
       #===menu===#
       M_FRAME=LabelFrame(self.root,text="Menus",font=("times new roman",15,"bold"),bg="black")
       M_FRAME.place(x=10,y=70,width=1340,height=80)
       btn_course=Button(M_FRAME,text="course",font=("goudy old style",15,"bold"),cursor="hand2",bg="yellow",fg="black",command=self.add_course).place(x=0,y=5,width=200,height=40)
       btn_stdent=Button(M_FRAME,text="student",font=("goudy old style",15,"bold"),cursor="hand2",bg="yellow",fg="black",command=self.add_student).place(x=220,y=5,width=200,height=40)
       btn_result=Button(M_FRAME,text="result",font=("goudy old style",15,"bold"),cursor="hand2",bg="yellow",fg="black",command=self.add_result).place(x=440,y=5,width=200,height=40)
       btn_view=Button(M_FRAME,text="view result",font=("goudy old style",15,"bold"),cursor="hand2",bg="yellow",fg="black",command=self.add_report).place(x=660,y=5,width=200,height=40)
       btn_logout=Button(M_FRAME,text="log-out",font=("goudy old style",15,"bold"),cursor="hand2",bg="yellow",fg="black",command=self.logout).place(x=880,y=5,width=200,height=40)
       btn_exit=Button(M_FRAME,text="Exit",font=("goudy old style",15,"bold"),cursor="hand2",bg="yellow",fg="black",command=self.exitt).place(x=1100,y=5,width=200,height=40)
       #===content===

       self.bg_img = Image.open("immage/bg.png")
       self.bg_img = self.bg_img.resize((920, 350), Image.BICUBIC)
       self.bg_img = ImageTk.PhotoImage(self.bg_img)
       self.bg_img_label = Label(self.root, image=self.bg_img)
       self.bg_img_label.place(x=400, y=180, width=920, height=350)
       self.side_img = Image.open("immage/mome.png")
       self.side_img = self.side_img.resize((400, 500), Image.BICUBIC)
       self.side_img = ImageTk.PhotoImage(self.side_img)
       self.side_img_label = Label(self.root, image=self.side_img)
       self.side_img_label.place(x=30, y=180, width=350, height=350)
       #===update===#
       self.lbl_course=Label(self.root,text="TOTAL COURSES\n[0]",font=("goudy old stlyle",15),bd=10,relief=RIDGE,bg="#808080",fg="white")
       self.lbl_course.place(x=400,y=530,width=240,height=80)
       self.lbl_student=Label(self.root,text="TOTAL STUDENTS\n[0]",font=("goudy old stlyle",15),bd=10,relief=RIDGE,bg="#038074",fg="white")
       self.lbl_student.place(x=710,y=530,width=240,height=80)
       self.lbl_result=Label(self.root,text="TOTAL RESULT\n[0]",font=("goudy old stlyle",15),bd=10,relief=RIDGE,bg="#0676ad",fg="white")
       self.lbl_result.place(x=1020,y=530,width=240,height=80)
       #===footer===
       footer=Label(self.root,text=" S.R.M.S :student result management system    contact us for any technical issues +91 7906970111\t or send mail :geusupport23@gmail.com",font=("goudy old style",12),bg="black",fg="white").pack(side=BOTTOM,fill=X)
       self.update_details()
    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)
    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=StudentClass(self.new_win)
    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=resultClass(self.new_win)
    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=reportClass(self.new_win)
    def logout(self):
        op=messagebox.askyesno("confirm","do you realy want to logout",parent=self.root)
        if op==True:
            self.root.destroy()
            script_path=r"C:\Users\gaurav\OneDrive\Desktop\PROJECTZ\login.py"
            subprocess.run(["python", script_path], capture_output=True, text=True)
    def exitt(self):
        op=messagebox.askyesno("confirm","do you realy want to exit",parent=self.root)
        if op==True:
            script_path=r"C:\Users\gaurav\OneDrive\Desktop\PROJECTZ\register.py"
            subprocess.run(["python", script_path], capture_output=True, text=True)

    def update_details(self):
        con=sqlite3.connect(database="PROJECTZ.db")
        cur=con.cursor()
        try:
            cur.execute("select *from course")
            cr=cur.fetchall()
            self.lbl_course.config(text=f"TOTAL COURSES[{str(len(cr))}]")
            self.lbl_course.after(200,self.update_details)

            cur.execute("select *from student")
            cr=cur.fetchall()
            self.lbl_student.config(text=f"TOTAL STUDENTS[{str(len(cr))}]")


            cur.execute("select *from result")
            cr=cur.fetchall()
            self.lbl_result.config(text=f"TOTAL RESULT[{str(len(cr))}]")

        except Exception as ex:
             messagebox.showerror("error",f"error due to{str(ex)}")
if __name__ == "__main__":
    root = Tk()
    obj = PROJECTZ(root)
    root.mainloop()
