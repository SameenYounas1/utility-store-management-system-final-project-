from tkinter import *
from PIL import Image, ImageTk
from employee import employeeclass
from category import categoryclass
from product  import ProductPage
import os
from report import reportclass

class UMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Utility store management system")
        self.root.config(bg="white")

        # ---title-----
        self.icon_title = PhotoImage(file="image/logo1.png")
        title = Label(self.root, text="Utility Store Management System ", image=self.icon_title, compound="left",
                      font=("times new roman", 40, "bold"), bg="#010c48", fg="white", padx=20)
        title.place(x=0, y=0, relwidth=1, height=70)

        # ---button log out------
        btn_logout = Button(self.root, text="Log Out", font=("times new roman", 15, "bold"), bg="yellow", command=self.logout, cursor="hand2")
        btn_logout.place(x=1200, y=10, height=50, width=150)


        # ----clock-------
        self.lbl_clock = Label(self.root,
                               text="Welcome to Utility Store Management System\t\t Date:dd-mm-yy \t\t time: HH:MM:SS ",
                               font=("times new roman", 15,), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)

        # ----left Menu------
        self.Menulogo = Image.open("image/menu_im.png")
        self.Menulogo = self.Menulogo.resize((200, 200), Image.Resampling.LANCZOS)

        self.Menulogo = ImageTk.PhotoImage(self.Menulogo)

        leftmenu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        leftmenu.place(x=0, y=102, width=200, height=565)

        Lbl_Menulogo = Label(leftmenu, image=self.Menulogo)
        Lbl_Menulogo.pack(side=TOP, fill=X)

        lbl_menu = Label(leftmenu, text="MENU", font=("times new roman", 20, "bold"), bg='#009688')
        lbl_menu.pack(side="top", fill=X)
        self.icon_side = PhotoImage(file="image/side.png")

        btn_employee = Button(leftmenu, text="Employee", command=self.employee , image=self.icon_side, compound=LEFT, padx=5, anchor="w",
                              font=("times new roman", 20, "bold"), bg='white', bd=3, cursor="hand2")
        btn_employee.pack(side="top", fill=X)

        btn_category = Button(leftmenu, text="Category", command=self.category ,image=self.icon_side, compound=LEFT, padx=5, anchor="w",
                              font=("times new roman", 20, "bold"), bg='white', bd=3, cursor="hand2")
        btn_category.pack(side="top", fill=X)

        btn_product = Button(leftmenu, text="Product",command=self.product , image=self.icon_side, compound=LEFT, padx=5, anchor="w",
                             font=("times new roman", 20, "bold"), bg='white', bd=3, cursor="hand2")
        btn_product.pack(side="top", fill=X)

        btn_sales = Button(leftmenu, text="Report",command=self.report, image=self.icon_side, compound=LEFT, padx=5, anchor="w",
                           font=("times new roman", 20, "bold"), bg='white', bd=3, cursor="hand2")
        btn_sales.pack(side="top", fill=X)

        btn_exits = Button(leftmenu, text="Exits", image=self.icon_side, compound=LEFT, padx=5, anchor="w",
                           font=("times new roman", 20, "bold"), bg='white', bd=3, cursor="hand2")
        btn_exits.pack(side="top", fill=X)

        # -----Content------
        self.lbl_employee = Label(self.root, text="Total Employees ", bd=5 , relief=RIDGE , font=("groudy old style", 20, "bold"),
                                  bg="#33bbf9", fg="white")
        self.lbl_employee.place(x=300, y=120, height=150, width=300)

        self.lbl_category = Label(self.root, text="Total category ", bd=5 , relief=RIDGE , font=("groudy old style", 20, "bold"),
                                  bg="#ff5722", fg="white")
        self.lbl_category.place(x=650, y=120, height=150, width=300)

        self.lbl_product = Label(self.root, text="Total Products ", bd=5 , relief=RIDGE , font=("groudy old style", 20, "bold"),
                                  bg="#009688", fg="white")
        self.lbl_product.place(x=1000, y=120, height=150, width=300)

        self.lbl_sales = Label(self.root, text="Report", bd=5 , relief=RIDGE , font=("groudy old style", 20, "bold"),
                                  bg="#ffc107", fg="white")
        self.lbl_sales.place(x=300, y=300, height=150, width=300)


        # ----Footer-------
        lbl_footer = Label(self.root,
                           text="Utility Store Management System | Developed by Sameen Younas (BC190411559) ",
                           font=("times new roman", 15,), bg="#4d636d", fg="white")
        lbl_footer.pack(side="bottom", fill=X)
    #===================================================================================
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeclass(self.new_win  )



    def category(self):
        self.new_win=Toplevel(self.root) 
        self.new_obj=categoryclass(self.new_win)   

    def  product(self):
         self.new_win=Toplevel(self.root) 
         self.new_obj=ProductPage(self.new_win)   

    def  report(self):
         self.new_win=Toplevel(self.root) 
         self.new_obj=reportclass(self.new_win)   
     

    def  logout(self):
         self.root.destroy() 
         os.system("python login.py")      

    def mainloop(self):
        self.root.mainloop()


if __name__ == "__main__":
    root = Tk()
    obj = UMS(root)
    obj.mainloop()
