import sqlite3
from tkinter import *
from tkinter import ttk, messagebox

class ProductPage:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.root.title("Utility Store Management System | Product Page")

        self.conn = sqlite3.connect("ums.db")
        self.cursor = self.conn.cursor()

       

        self.products = self.get_all_products()
        self.categories = self.get_categories()

        self.products = self.get_all_products()
        self.categories = self.get_categories()

        self.product_id = IntVar()
        self.product_name = StringVar()
        self.product_price = DoubleVar()
        self.product_quantity = IntVar()
        self.selected_category = StringVar()
        self.selling_price = DoubleVar()
        self.purchased_price = DoubleVar()
        self.profit = DoubleVar()

        self.create_widgets()

    def get_categories(self):
        self.cursor.execute("SELECT name FROM category")
        return [category[0] for category in self.cursor.fetchall()]

    def add_product(self):
        try:
            product_data = {
                "name": self.product_name.get(),
                "price": self.product_price.get(),
                "quantity": self.product_quantity.get(),
                "category": self.selected_category.get(),
                "selling_price": self.selling_price.get(),
                "purchased_price": self.purchased_price.get(),
                "profit": self.calculate_profit()
            }

            self.cursor.execute("INSERT INTO product (name, price, qty, category, selling_price, purchased_price, profit) VALUES (?, ?, ?, ?, ?, ?, ?)",
                                (product_data["name"], product_data["price"], product_data["quantity"],
                                product_data["category"], product_data["selling_price"], product_data["purchased_price"],
                                product_data["profit"]))

            self.conn.commit()
            self.show_products()
            messagebox.showinfo("Success", "Product added successfully.")
        except Exception as ex:
            messagebox.showerror("Error", f"Error occurred while adding product: {ex}")

    def update_product(self):
        try:
            product_data = {
                "id": self.product_id.get(),
                "name": self.product_name.get(),
                "price": self.product_price.get(),
                "quantity": self.product_quantity.get(),
                "category": self.selected_category.get(),
                "selling_price": self.selling_price.get(),
                "purchased_price": self.purchased_price.get(),
                "profit": self.calculate_profit()
            }

            self.cursor.execute("UPDATE product SET name=?, price=?, qty=?, category=?, selling_price=?, purchased_price=?, profit=? WHERE pid=?",
                                (product_data["name"], product_data["price"], product_data["quantity"],
                                product_data["category"], product_data["selling_price"], product_data["purchased_price"],
                                product_data["profit"], product_data["id"]))

            self.conn.commit()
            self.show_products()
            messagebox.showinfo("Success", "Product updated successfully.")
        except Exception as ex:
            messagebox.showerror("Error", f"Error occurred while updating product: {ex}")

    def delete_product(self):
        try:
            product_id = self.product_id.get()
            if product_id:
                self.cursor.execute("DELETE FROM product WHERE pid=?", (product_id,))
                self.conn.commit()
                self.show_products()
                messagebox.showinfo("Success", "Product deleted successfully.")
            else:
                messagebox.showerror("Error", "Please select a product to delete.")
        except Exception as ex:
            messagebox.showerror("Error", f"Error occurred while deleting product: {ex}")

    def get_all_products(self):
        self.cursor.execute("SELECT * FROM product")
        return self.cursor.fetchall()
    def calculate_profit(self):
        try:
            selling_price = self.selling_price.get()
            purchased_price = self.product_price.get()  # Changed from self.purchased_price.get() to self.product_price.get()
            profit = selling_price - purchased_price
            return profit
        except Exception as ex:
            return 0.0


    def create_widgets(self):
        # ----------Product Form
        product_frame = Frame(self.root)
        product_frame.grid(row=0, column=0, padx=20, pady=20)

        Label(product_frame, text="Product Name:", font="Helvetica 12 bold").grid(row=0, column=0, padx=10, pady=5)
        Entry(product_frame, textvariable=self.product_name).grid(row=0, column=1, padx=10, pady=5)

        Label(product_frame, text="Price:", font="Helvetica 12 bold").grid(row=1, column=0, padx=10, pady=5)
        Entry(product_frame, textvariable=self.product_price).grid(row=1, column=1, padx=10, pady=5)

        Label(product_frame, text="Quantity:", font="Helvetica 12 bold").grid(row=2, column=0, padx=10, pady=5)
        Entry(product_frame, textvariable=self.product_quantity).grid(row=2, column=1, padx=10, pady=5)

        Label(product_frame, text="Category:", font="Helvetica 12 bold").grid(row=3, column=0, padx=10, pady=5)
        self.category_combobox = ttk.Combobox(product_frame, textvariable=self.selected_category, values=self.categories, state="readonly")
        self.category_combobox.grid(row=3, column=1, padx=10, pady=5)

        Label(product_frame, text="Selling Price:", font="Helvetica 12 bold").grid(row=4, column=0, padx=10, pady=5)
        Entry(product_frame, textvariable=self.selling_price).grid(row=4, column=1, padx=10, pady=5)

        Label(product_frame, text="Purchased Price:", font="Helvetica 12 bold").grid(row=5, column=0, padx=10, pady=5)
        Entry(product_frame, textvariable=self.purchased_price).grid(row=5, column=1, padx=10, pady=5)

        self.profit_label = Label(product_frame, text="Profit: N/A", font="Helvetica 12 bold")
        self.profit_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

        # --------the "Profit button" section--------
        ttk.Button(product_frame, text="Calculate Profit", command=self.calculate_and_display_profit).grid(row=7, column=0, columnspan=2, padx=10, pady=5)

        # Buttons
        button_frame = Frame(self.root)
        button_frame.grid(row=1, column=0, padx=20, pady=10)

        ttk.Button(button_frame, text="Add Product", command=self.add_product).grid(row=0, column=0, padx=10, pady=5)
        ttk.Button(button_frame, text="Update Product", command=self.update_product).grid(row=0, column=1, padx=10, pady=5)
        ttk.Button(button_frame, text="Delete Product", command=self.delete_product).grid(row=0, column=2, padx=10, pady=5)

        # Search Bar
        search_frame = Frame(self.root)
        search_frame.grid(row=2, column=0, padx=20, pady=10)

        Label(search_frame, text="Search Product Name:", font="Helvetica 12 bold").grid(row=0, column=0, padx=10, pady=5)
        self.search_entry = Entry(search_frame)
        self.search_entry.grid(row=0, column=1, padx=10, pady=5)
        ttk.Button(search_frame, text="Search", command=self.search_product).grid(row=0, column=2, padx=10, pady=5)

        # Treeview
        self.initialize_treeview()

        self.show_products()

    def calculate_and_display_profit(self):
        profit = self.calculate_profit()
        self.profit.set(profit)
        self.profit_label.config(text=f"Profit: {profit:.2f}")

    def search_product(self):
        keyword = self.search_entry.get().strip().lower()
        filtered_products = [product for product in self.products if keyword in product[1].lower()]
        if filtered_products:
            self.products = filtered_products
            self.show_products()
        else:
            messagebox.showinfo("Not Found", "No products found with the given search keyword.")

    def initialize_treeview(self):
        product_list_frame = Frame(self.root)
        product_list_frame.grid(row=3, column=0, padx=20, pady=10)
        scrolly = Scrollbar(product_list_frame, orient=VERTICAL)
        scrollx = Scrollbar(product_list_frame, orient=HORIZONTAL)

        self.tree = ttk.Treeview(product_list_frame, columns=("ID", "Category", "Quantity", "Name", "Price", "Selling Price", "Purchased Price", "Profit"),
                                 yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.pack(side=BOTTOM, fill=X)
        scrollx.config(command=self.tree.xview)
        scrolly.config(command=self.tree.yview)

        self.tree.heading("ID", text="ID")
        self.tree.heading("Category", text="Category")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Price", text="Price")
        self.tree.heading("Selling Price", text="Selling Price")
        self.tree.heading("Purchased Price", text="Purchased Price")
        self.tree.heading("Profit", text="Profit")

        self.tree.column("ID", width=40, anchor="center")
        self.tree.column("Category", width=100, anchor="w")
        self.tree.column("Quantity", width=100, anchor="center")
        self.tree.column("Name", width=150, anchor="center")
        self.tree.column("Price", width=100, anchor="center")
        self.tree.column("Selling Price", width=100, anchor="center")
        self.tree.column("Purchased Price", width=100, anchor="center")
        self.tree.column("Profit", width=100, anchor="center")

        self.tree.pack(expand=1, fill=BOTH)

        self.tree.bind("<<TreeviewSelect>>", self.on_select_product)

    def show_products(self):
        self.tree.delete(*self.tree.get_children())
        for product in self.products:
            if len(product) == 8:
                self.tree.insert("", "end", values=(product[0], product[4], product[3], product[1], product[2], product[5], product[6], product[7]))
            else:
                print(f"Warning: Product with ID {product[0]} has an unexpected number of elements: {len(product)}")

    def on_select_product(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            values = self.tree.item(selected_item)["values"]
            self.product_id.set(values[0])
            self.selected_category.set(values[1])
            self.product_quantity.set(values[2])
            self.product_name.set(values[3])
            self.product_price.set(values[4])
            self.selling_price.set(values[5])
            self.purchased_price.set(values[6])
            self.profit.set(values[7])

if __name__ == "__main__":
    root = Tk()
    product_page = ProductPage(root)
    root.mainloop()
    