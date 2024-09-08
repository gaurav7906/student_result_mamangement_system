from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import os
import subprocess
import sqlite3
class loginClass:
    def __init__(self, root):
       self.root=root
       self.root.title("Login Window")
       self.root.geometry("1350x700+0+0")
       self.root.config(bg="white")

       #===image===
       self.bg=ImageTk.PhotoImage(file="immage/b2.jpg")
       bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)

       self.left=ImageTk.PhotoImage(file="immage/side.png")
       left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)

       frame1=Frame(self.root,bg="white")
       frame1.place(x=480,y=100,width=700,height=500)


       title=Label(frame1,text="LOGIN HERE",font=("times new roman",30,"bold"),bg="white",fg="green").place(x=100,y=30)
       fname=Label(frame1,text="ENTER NAME",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=100,y=100)
       self.txt_fname=Entry(frame1,font=("goudy old style",20, "bold"),bg="lightyellow")
       self.txt_fname.place(x=100,y=130,width=350)

       password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=100,y=180)
       self.txt_password=Entry(frame1,font=("goudy old style",22, "bold"),bg="lightyellow")
       self.txt_password.place(x=100,y=210,width=350)
       btn_login=Button(frame1,text="LOGIN",font=("times new roman",20,"bold"),fg="white",bg="red",command=self.login).place(x=100,y=300,width=180,height=40)

    def login(self):
        if self.txt_fname.get() == "" or self.txt_password.get() == "":
            messagebox.showerror("Error", "Fields cannot be empty", parent=self.root)
        else:
            try:
                con = sqlite3.connect(database="PROJECTZ.db")
                cur = con.cursor()
                cur.execute("select * from employee where fname=? and password=?", (self.txt_fname.get(), self.txt_password.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid username or password", parent=self.root)
                else:
                    messagebox.showinfo("Success", "Welcome", parent=self.root)
                    self.root.destroy()
                    script_path = r"C:\Users\gaurav\OneDrive\Desktop\PROJECTZ\dashboard.py"
                    result= subprocess.run(["python", script_path], capture_output=True, text=True)
                    if result.runcode==0:
                        print("output",result.stdout)
                    else:
                        print("error:",result.stderr)
            except Exception as  ex:
                messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)






if __name__ == "__main__":
    root = Tk()
    obj = loginClass(root)
    root.mainloop()
