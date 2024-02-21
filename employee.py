from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3

class employeeclass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Utility store management system")
        self.root.config(bg="white")
        self.root.focus_force()
    
    #-----------------------------------------
    #--------------All variable------------

        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.var_emp_id=StringVar() 
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_email=StringVar()
        self.var_password=StringVar()
        self.var_utype=StringVar()
        self.var_address=StringVar()
        self.var_salary=StringVar()
    


     #------search frame------
        SearchFrame=LabelFrame(self.root , text="Search Employee" , font =("groudy old style" , 12 , "bold") , bd=2 , relief=RIDGE , bg="white")
        SearchFrame.place(x=250 , y= 20 , width= 600 , height=70)   
    
    #------option-------------
        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby ,  value=("Select", "Emp ID", "Name", "Contact"), state="readonly", font=("goudy old style", 15, "bold"))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame ,textvariable=self.var_searchtxt , font=("goudy old style" , 20 , "bold")) . place (x=200 , y=10)

        btn_search=Button(SearchFrame , text="Search" , command=self.search ,font=("goudy old style" , 20 , "bold"), bg="#4caf20" , fg="white" , cursor="hand2") . place (x=410 , y=10 , width=150 , height=30)

    #-------Title--------------
        lbl_title=Label( self.root , text="Employee Details" , font= ("goudy old style" , 20 , "bold" ), bg="#0f4d7d" , fg= "white") . place (x=50 , y=100 , width=1000)
   

     #-------Content------------
     #------- Row 1--------
        lbl_empid=Label( self.root , text="Emp Id" , font= ("goudy old style" , 20 , "bold" ), bg="white" ) . place (x=50 , y=150 )
        
        lbl_contact=Label( self.root , text="Contact" , font= ("goudy old style" , 20 , "bold" ), bg="white" ) . place (x=750 , y=150 )

        txt_empid = Entry(self.root, textvariable=self.var_emp_id, font=("goudy old style", 20, "bold"), bg="lightyellow")
        txt_empid.place(x=150, y=150, width=180)

        label_gender = Label(self.root, text="Gender", font=("goudy old style", 20, "bold"))
        label_gender.place(x=350, y=150)

        cmb_gender = ttk.Combobox(self.root, textvariable=self.var_gender, value=("Select", "Male", "Female"), state="readonly", font=("goudy old style", 15, "bold"))
        cmb_gender.place(x=500, y=150, width=180)
        cmb_gender.current(0)

        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 20, "bold"), bg="lightyellow")
        txt_contact.place(x=850, y=150, width=180) 

        #-------Row 2---------
        label_name = Label(self.root, text="Name", font=("goudy old style", 20, "bold"), bg='white')
        label_name.place(x=50, y=190)

        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 20, "bold"), bg="lightyellow")
        txt_name.place(x=150, y=190, width=180)

        label_dob = Label(self.root, text="D.O.B", font=("goudy old style", 20, "bold") , bg="white")
        label_dob.place(x=350, y=190)

        txt_dob = Entry(self.root, textvariable=self.var_dob, font=("goudy old style", 20, "bold"), bg="lightyellow")
        txt_dob.place(x=500, y=190, width=180)

        label_doj = Label(self.root, text="D.O.J", font=("goudy old style", 20, "bold"),bg="white")
        label_doj.place(x=750, y=190)

        txt_doj = Entry(self.root, textvariable=self.var_doj, font=("goudy old style", 20, "bold"), bg="lightyellow")
        txt_doj.place(x=850, y=190, width=180)

        #-------Row 3------------
        label_email = Label(self.root, text="Email", font=("goudy old style", 20, "bold"), bg='white')
        label_email.place(x=50, y=230)

        txt_name = Entry(self.root, textvariable=self.var_email, font=("goudy old style", 20, "bold"), bg="lightyellow")
        txt_name.place(x=150, y=230, width=180)

        label_password = Label(self.root, text="Password", font=("goudy old style", 20, "bold") , bg="white")
        label_password.place(x=350, y=230)

        txt_password = Entry(self.root, textvariable=self.var_password, font=("goudy old style", 20, "bold"), bg="lightyellow")
        txt_password.place(x=500, y=230, width=180)

        label_utype = Label(self.root, text="Usertype", font=("goudy old style", 20, "bold"),bg="white")
        label_utype.place(x=750, y=230)

        cmb_utype = ttk.Combobox(self.root, textvariable=self.var_utype, value=("Select", "Admin", "employee"), state="readonly", font=("goudy old style", 15, "bold"))
        cmb_utype.place(x=850, y=230, width=180)
        cmb_utype.current(0)

        #--------Row 4----------------
        label_address = Label(self.root, text="Address", font=("goudy old style", 20, "bold"), bg='white')
        label_address.place(x=50, y=270)

        txt_address = Entry(self.root, font=("goudy old style", 20, "bold"), bg="lightyellow")
        txt_address.place(x=150, y=270 , width=300 , height=60 )

        label_salary = Label(self.root, text="Salary", font=("goudy old style", 20, "bold"), bg='white')
        label_salary.place(x=500, y=270)

        txt_salary = Entry(self.root, textvariable=self.var_salary, font=("goudy old style", 20, "bold"), bg="lightyellow")
        txt_salary.place(x=600, y=270, width=180)

        #------buttons--------
        button_add=Button(self.root , text="Save" ,command=self.add , font=("goudy old style" , 20 , "bold") , bg="#2196f3" , fg="white" , cursor="hand2" )
        button_add.place(x=500 , y=315 , width=110 , height=28)

        button_update=Button(self.root , text="Update" , command=self.update , font=("goudy old style" , 20 , "bold") , bg="#4caf50" , fg="white" , cursor="hand2" )
        button_update.place(x=620 , y=315 , width=110 , height=28)
 
        button_delete=Button(self.root , text="Delete" , command=self.delete ,font=("goudy old style" , 20 , "bold") , bg="#f44336" , fg="white" , cursor="hand2" )
        button_delete.place(x=740 , y=315 , width=110 , height=28)

        button_clear=Button(self.root , text="Clear" , command=self.clear , font=("goudy old style" , 20 , "bold") , bg="#607d8b" , fg="white", cursor="hand2" )
        button_clear.place(x=860 , y=315 , width=110 , height=28)
        
        #-------Employee Details------
        emp_frame=Frame(self.root , bd=3 , relief="ridge")
        emp_frame.place(x=0 , y=350 , relwidth=1 , height=150)

        Scrolly=Scrollbar(emp_frame , orient="vertical")
        Scrollx=Scrollbar(emp_frame , orient="horizontal")

        self.EmployeeTable=ttk.Treeview(emp_frame , columns=("eid ","name", "email" , "gender","contact","dob","doj" , "pass", "utype","address", "salary") ,yscrollcommand=Scrolly.set  , xscrollcommand=Scrollx.set)
        Scrollx.pack(side="bottom",fill="x")
        Scrolly.pack(side="right",fill="y")
        Scrollx.config(command=self.EmployeeTable.xview)
        Scrolly.config(command=self.EmployeeTable.yview)
        
        self.EmployeeTable.heading("eid ",text="Emp Id")
        self.EmployeeTable.heading("name",text="Name")
        self.EmployeeTable.heading("email" ,text="Email")
        self.EmployeeTable.heading("gender",text="Gender")
        self.EmployeeTable.heading("contact",text="Contact")
        self.EmployeeTable.heading("dob",text="D.O.B")
        self.EmployeeTable.heading("doj",text="D.O.J")
        self.EmployeeTable.heading("pass",text="Password")
        self.EmployeeTable.heading("utype",text="Usertype")
        self.EmployeeTable.heading("address",text="Address")
        self.EmployeeTable.heading("salary",text="Salary")
        
        self.EmployeeTable["show"]= "headings"

        #---setting the columns size

        self.EmployeeTable.column("eid ",width=90)
        self.EmployeeTable.column("name",width=100)
        self.EmployeeTable.column("email" ,width=100)
        self.EmployeeTable.column("gender",width=100)
        self.EmployeeTable.column("contact",width=100)
        self.EmployeeTable.column("dob",width=100)
        self.EmployeeTable.column("doj",width=100)
        self.EmployeeTable.column("pass",width=100)
        self.EmployeeTable.column("utype",width=100)
        self.EmployeeTable.column("address", width=100)
        self.EmployeeTable.column("salary",width=100)
        self.EmployeeTable.pack(fill=BOTH , expand=1) 
        self.EmployeeTable.bind("<ButtonRelease-1>", self.get_data)
        
  
        self.show()
   
#==========================================================================
    def add(self):
     con=sqlite3.connect(database=r"ums.db")
     cur=con.cursor()

     try:
        if  self.var_emp_id.get()=="":
         messagebox.showerror('Error',"Please enter Emp ID" , parent=self.root)
        else:
           cur.execute("SELECT * from employee where eid=?" , (self.var_emp_id.get(),))
           row=cur.fetchone()
           if row!=None:
              messagebox.showerror("Error","this Employee is already assigned, Try different", parent=self.root)
           else:
               cur.execute("INSERT INTO employee(eid, name, email, gender, contact, dob, doj, pass, utype, address, salary) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (self.var_emp_id.get(), self.var_name.get(), self.var_email.get(), self.var_gender.get(),
             self.var_contact.get(), self.var_dob.get(), self.var_doj.get(), self.var_password.get(),
             self.var_utype.get(), self.var_address.get(), self.var_salary.get()))

        con.commit()
        messagebox.showinfo("Success","Employee added successfully",parent=self.root)
     except Exception as ex: 
        messagebox.showerror('Error',f"Error due to: {str(ex)}",parent=self.root) 
        self.show()
    def new_method(self, con):
        con.commit()  


    def show(self):     
     con=sqlite3.connect(database=r"ums.db")
     cur=con.cursor()
     
     try:
      cur.execute("select* from employee")
      rows=cur.fetchall()
      self.EmployeeTable.delete(*self.EmployeeTable.get_children())
      for row in rows:
         self.EmployeeTable.insert('',END,values=row)
                   
     except Exception as ex: 
        messagebox.showerror('Error',f"Error due to: {str(ex)}",parent=self.root)   
     
    def get_data(self, ev):
        f = self.EmployeeTable.focus()
        content = (self.EmployeeTable.item(f))
        row = content['values']
        self.var_emp_id.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])
        self.var_dob.set(row[5])
        self.var_doj.set(row[6])
        self.var_password.set(row[7])
        self.var_utype.set(row[8])
        self.var_address.set(row[9])
        self.var_salary.set(row[10])

    def update(self):
     con=sqlite3.connect(database=r"ums.db")
     cur=con.cursor()

     try:
        if  self.var_emp_id.get()=="":
         messagebox.showerror('Error',"Please enter Emp ID" , parent=self.root)
        else:
           cur.execute("SELECT * from employee where eid=?" , (self.var_emp_id.get(),))
           row=cur.fetchone()
           if row==None:
              messagebox.showerror("Error","Invalid Employee ID", parent=self.root)
           else:
               cur.execute("UPDATE  employee SET  name=?, email=?, gender=?, contact=?, dob=?, doj=?, pass=?, utype=?, address=?, salary=? WHERE eid=? ",
              (self.var_name.get(), self.var_email.get(), self.var_gender.get(),
             self.var_contact.get(), self.var_dob.get(), self.var_doj.get(), self.var_password.get(),
             self.var_utype.get(), self.var_address.get(), self.var_salary.get(),self.var_emp_id.get()))

        con.commit()
        messagebox.showinfo("Success","Employee UPDATED successfully",parent=self.root)
     except Exception as ex: 
        messagebox.showerror('Error',f"Error due to: {str(ex)}",parent=self.root) 
        self.show()
    def new_method(self, con):
        con.commit()  

   

    def delete(self):
      con = sqlite3.connect(database=r"ums.db")   
      cur = con.cursor()    
      
      try:
        if self.var_emp_id.get() == "":
            messagebox.showerror('Error', "Please enter Emp ID", parent=self.root)
        else:
            cur.execute("SELECT * from employee where eid=?", (self.var_emp_id.get(),))
            row = cur.fetchone()
            if row is None:
                messagebox.showerror("Error", "Invalid Employee ID", parent=self.root)
            else:
                op = messagebox.askyesno("Confirm", "You really want to delete", parent=self.root)
                if op==True:
                    cur.execute("DELETE FROM employee WHERE eid=?", (self.var_emp_id.get(),))

                    con.commit()
                    messagebox.showinfo("Delete", "Employee deleted successfully", parent=self.root)

        self.clear()

      except Exception as ex:
        messagebox.showerror('Error', f"Error due to: {str(ex)}", parent=self.root)

        self.show()
 




    def show(self):     
     con=sqlite3.connect(database=r"ums.db")
     cur=con.cursor()
     
     try:
      cur.execute("select* from employee")
      rows=cur.fetchall()
      self.EmployeeTable.delete(*self.EmployeeTable.get_children())
      for row in rows:
         self.EmployeeTable.insert('',END,values=row)
                   
     except Exception as ex: 
        messagebox.showerror('Error',f"Error due to: {str(ex)}",parent=self.root)

    def clear(self):       
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_password.set("")
        self.var_utype.set("admin")
        self.var_address.set("")
        self.var_salary.set("")
        self.show()

    

    def search(self):
        con = sqlite3.connect(database=r"ums.db")
        cur = con.cursor()

        try:
            if self.var_searchby.get():
             messagebox. showerror("Ennor", "Select Search By option" ,parent=self.root)
            elif self.var_searchtxt.get()=="":
             messagebox. showerror("Enror", "Search input should be required" ,parent=self.root)

            cur.execute("SELECT * FROM employee WHERE " + self.var_searchby.get() + " LIKE '%" + self.var_searchtxt.get() + "%'")


            rows = cur.fetchall()
            if len(rows)!=0:
             self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                  self.EmployeeTable.insert("" ,END, values=row)
            else:
                  messagebox. showerror ("ErroR", "No record found" ,parent=self.root)

        except Exception as ex:
            messagebox.showerror('Error', f"Error due to: {str(ex)}", parent=self.root)
    
    

         
if __name__ == '__main__':
     root = Tk()
     obj = employeeclass(root)
     root.mainloop()
