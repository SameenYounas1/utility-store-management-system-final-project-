import tkinter as tk
from tkinter import ttk
import sqlite3
import pandas as pd


class reportclass:
    def __init__(self, root):
        # Function to fetch data from the database and display in the treeview
        def show_data():
            # Connect to the SQLite database
            conn = sqlite3.connect('ums.db')

            # Fetch data from the product table
            query = 'SELECT * FROM product'
            df = pd.read_sql_query(query, conn)

            # Close the database connection
            conn.close()

            # Display the data in the treeview
            display_data(df)

        # Function to display data in the treeview
        def display_data(df):
            # Clear previous data in the treeview
            tree.delete(*tree.get_children())

            # Insert data from the DataFrame into the treeview
            for index, row in df.iterrows():
                tree.insert("", tk.END, values=row.tolist())

        # Create a tkinter GUI
        root.geometry('800x400')
        root.title("Utility Store Management System | Report Generation")

        # Button to fetch data and show in the treeview
        show_data_button = tk.Button(root, text="Show Data", command=show_data)
        show_data_button.pack()

        # Treeview to display the data
        columns = ['Product ID', 'Product Name', 'Price', 'Qty', 'Category', 'Selling Price', 'Purchased Price', 'Profit']
        tree = ttk.Treeview(root, columns=columns, show='headings')

        # Set column headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100)

        # Call the show_data() function
        show_data()

        tree.pack()

if __name__ == "__main__":
    root = tk.Tk()
    reportclass(root)
    root.mainloop()
