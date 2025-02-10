import os
from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk
import mysql.connector

def show(listBox):
    try:
        # Connect to the database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv("DB_PASSWORD"),
            database="employee"
            )
        myCur = mydb.cursor()

        # Execute query to fetch all data from the table
        myCur.execute("SELECT * FROM empDetails")
        records = myCur.fetchall()

        # Clear the Listbox before updating it
        listBox.delete(0, END)

        # Insert column headers at the top of the Listbox (optional)
        listBox.insert(END, f"{'Employee ID':<25}{'Name':<25}{'Department':<35}")
        listBox.insert(END, "=" * 55)

        # Insert rows into the Listbox dynamically
        for row in records:
            listBox.insert(END, f"{row[0]:<25}{row[1]:<25}{row[2]:<35}")

    except mysql.connector.Error as e:
        # Handle database errors with a meaningful message
        messagebox.showerror("Database Error", f"An error occurred: {e}")
    finally:
        # Always close the database cursor and connection to avoid leaks
        if 'myCur' in locals():
            myCur.close()
        if 'mydb' in locals():
            mydb.close()