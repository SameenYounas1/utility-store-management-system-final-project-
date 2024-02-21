from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3
import os
class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Utility store management system | Log In")
        self.root.config(bg="#fafafa")
        #----images------
        self.phone_image=ImageTk.PhotoImage(file="image/phone.png")
        self.lbl_image=Label(self.root , image=self.phone_image).place(x=200,y=50)
        #------Frame-----
        self.employee_id=StringVar()
        self.password=StringVar()
        
        Frame_login=Frame(self.root , bd=20 , relief=RIDGE)
        Frame_login.place(x=650 , y=90 ,width=350, height=460)

        title=Label(root, text="Employee log in", font=("Arial Rounded MT Bold", 30, "bold")).place(x=0, y=30, relwidth=1)
        lbl_user = Label(Frame_login, text="Employee Id", font=("goudy old style", 25, "bold"))
        lbl_user.place(x=50, y=100)
       
        entry_user = Entry(Frame_login, font=("goudy old style", 15), bg="#BCECEC",textvariable=self.employee_id)
        entry_user.place(x=50, y=140 , width=250)

        lbl_password = Label(Frame_login, text="Password", font=("goudy old style", 25, "bold"))
        lbl_password.place(x=50, y=200)
        entry_password = Entry(Frame_login, font=("goudy old style", 15), bg="#BCECEC", textvariable=self.password)
        entry_password.place(x=50, y=240 , width=250)

        Btn_login = Button(Frame_login, text="Log in", font=("Arial Rounded MT Bold", 12),command=self.login, cursor="hand2" , bg="lightblue")
        Btn_login.place(x=50, y=300, width=250, height=35)
#-----------log in functions-------
    def login(self):
            con=sqlite3.connect(database= r"ums.db")
            cur=con.cursor()
            try:
                if self.employee_id.get()==""or self.password.get()=="":
                    messagebox.showerror("error","All fields are required",parent=self.root)
                else:    
                   cur.execute("select* from employee where eid=? AND pass=?",(self.employee_id.get(),self.password.get()))
                   user=cur.fetchone()
                   if user==None:
                        messagebox.showerror("error","Invalid username / password",parent=self.root)
                   else:
                        
                            self.root.destroy()
                            os.system("python dashboard.py") 
                           
            except Exception as ex:
                 messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)



if __name__ == '__main__':
     root = Tk()
     obj = Login_System(root)
     root.mainloop()  




