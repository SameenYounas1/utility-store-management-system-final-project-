from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3

class categoryclass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Utility Store Management System| Category Section")
        self.root.config(bg="white")
        self.root.focus_force()
        #======Variables===
        self.var_cat_id=StringVar()
        self.var_name=StringVar()
        
         #-------TITLE----
        label_title=Label(self.root , text="Manage Product Category" , font=("goudy old style ", 30), bg="#184a45", fg="white", bd=2 , relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)

        label_name=Label(self.root , text="Select Category Name" , font=("goudy old style ", 30), bg="white").place(x=50,y=100)
        Text_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style ", 18), bg="lightyellow").place(
            x=50, y=170, width=300)
        
        btn_add=Button(self.root , text="ADD" , command=self.add ,font=("goudy old style ", 10 , "bold"), bg="#4caf50",fg="white",cursor="hand2").place(x=360,y=170,width=150, height=30)
        btn_delete=Button(self.root , text="DELETE" ,command=self.delete , font=("goudy old style ", 10 , "bold"), bg="Red",fg="white",cursor="hand2").place(x=520,y=170,width=150, height=30)
         
        #----------Category Details----
        frame_cat = Frame(self.root, bd=3, relief=RIDGE)
        frame_cat.place(x=700, y=120, width=380, height=350)

        scrollx = Scrollbar(frame_cat, orient=HORIZONTAL)
        scrolly = Scrollbar(frame_cat, orient=VERTICAL)

        self.categorytable = ttk.Treeview(frame_cat, columns=("cid", "Category Name"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command=self.categorytable.xview)
        scrolly.config(command=self.categorytable.yview)

        self.categorytable.heading("cid", text="Category Id")
        self.categorytable.heading("Category Name", text="Category Name")
        self.categorytable["show"] = "headings"
        self.categorytable.column("cid", width=90)
        self.categorytable.column("Category Name", width=100)
        self.categorytable.pack(fill=BOTH , expand=1) 
        self.categorytable.bind("<ButtonRelease-1>", self.get_data)


        #---Image---
        self.im1 = Image.open("image/cat.jpg")
        self.im1=self.im1.resize((490,240),Image.Resampling.LANCZOS)
        self.im1=ImageTk.PhotoImage(self.im1)

        self.lbl_im1 = Label(self.root, image=self.im1, bd=1,relief=RAISED, bg="white")
        self.lbl_im1.place(x=50, y=220)
        self.show()
        ######################Function############################
      
    def add(self):
        con=sqlite3.connect(database=r'ums.db')
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error", "Category name should be required", parent=self.root)
            else:
                cur.execute("Select * from category where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Category already present, try different", parent=self.root)
                else:
                    cur.execute("Insert into category(name) values(?)", (self.var_name.get(),))
                    con.commit()
                    messagebox.showinfo("Success", "Category Added Successfully", parent=self.root)
                    self.show()
                    self.var_name.set("")
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def show(self):
        con=sqlite3.connect(database=r'ums.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from category")
            rows=cur.fetchall()
            self.categorytable.delete(*self.categorytable.get_children())
            for row in rows:
                self.categorytable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def get_data(self, ev):
        f=self.categorytable.focus()
        content=(self.categorytable.item(f))
        row=content['values']

        self.var_cat_id.set(row[0])
        self.var_name.set(row[1])

    def delete(self):
        con=sqlite3.connect(database=r'ums.db')
        cur=con.cursor()
        try:
            if self.var_cat_id.get()=="":
                messagebox.showerror("Error", "Please select category from the list", parent=self.root)
            else:
                cur.execute("Select * from category where cid=?",(self.var_cat_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Error, Please try again", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?", parent=self.root)
                    if op==True:
                        cur.execute("delete from category where cid=?",(self.var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Category Deleted Successfully", parent=self.root)
                        self.show()
                        self.var_cat_id.set("")
                        self.var_name.set("")

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


        
        

if __name__ == '__main__':
     root = Tk()
     obj = categoryclass(root)
     root.mainloop()
