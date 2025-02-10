# This is a module containing CRUD sql operations
import os
from tkinter import *
from tkinter import messagebox
from utilities import show

import mysql.connector

def insertData(enterID, enterName, enterDept, listBox):
    id = enterID.get()
    name = enterName.get()
    dept = enterDept.get()

    if id== "" or name== "" or dept== "":
        messagebox.showwarning("Cannot insert","All three fields, employee id, employee name and employee dept are required")
    else:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv("DB_PASSWORD"),
            database="employee"
        )
        myCur = mydb.cursor()
        #sql = "INSERT INTO empDetails (empID, empName, empDept) VALUES (id, name, dept)"
        sql = "INSERT INTO empDetails (empID, empName, empDept) VALUES (%s, %s, %s)"
        myCur.execute(sql, (id, name, dept))
        mydb.commit()

        #Clear the names filled by the user in the gui so it is ready for next operation
        enterID.delete(0, END)
        enterName.delete(0, END)
        enterDept.delete(0, END)
        show(listBox)
        messagebox.showinfo("Insert Status", "Data inserted successfully")
        myCur.close()
        mydb.close()

def removeData(enterID,enterName, enterDept, listBox):
    id = enterID.get().strip()
    if id == "":
        messagebox.showwarning("Cannot delete this data",
                               "Please enter employee id in order to delete the data for this employee")
        return
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv("DB_PASSWORD"),
            database="employee"
        )
        myCur = mydb.cursor()
        #check_query = "SELECT * FROM empDetails WHERE empID = %s"
        #myCur.execute(check_query, (id,))
        #result = myCur.fetchone()
        #if result is None:  # If no record is found with the given empID
        #    messagebox.showerror("Delete Error", "Employee ID must exist to delete the entry")
        #else:
        del_query = "DELETE FROM empDetails WHERE empID = %s"
        myCur.execute(del_query, (id,))
        if myCur.rowcount == 0:
            messagebox.showerror("Delete Error", f"No data found for Employee ID: {id}")
        else:
            #Complete the transaction
            mydb.commit()
            messagebox.showinfo("Delete Status", f"Data deleted successfully for employee {id}")
            # Clear the names filled by the user in the gui so it is ready for next operation
            show(listBox)
            enterID.delete(0, END)
            enterName.delete(0, END)
            enterDept.delete(0, END)
    except mysql.connector.Error as e:
        # Handle database connection errors or query errors
        messagebox.showerror("Database Error", f"An error occurred: {e}")
    finally:
        # Close database connection
        if 'myCur' in locals():
            myCur.close()
        if 'mydb' in locals():
            mydb.close()

def getData(enterID, enterName, enterDept):
    id = enterID.get().strip() # Get the id and remove any trailing characters
    #Check if id is empty
    if id == "":
        messagebox.showwarning("Cannot fetch this data",
                               "Please enter employee id in order to fetch the data for the other fields")
        return
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv("DB_PASSWORD"),
            database="employee"
        )
        myCur = mydb.cursor()
        data_query = "SELECT empName, empDept FROM empDetails WHERE empID = %s"
        myCur.execute(data_query, (id,))
        #Use 'id' as a single-item tuple
        result = myCur.fetchone()
        if result is None:
            messagebox.showerror("Fetch Error", f"Employee ID does not exist for employee ID: {id}")
        else:
            empName, empDept = result
            enterName.delete(0, END)
            enterName.insert(0, empName)
            enterDept.delete(0, END)
            enterDept.insert(0, empDept)
            messagebox.showinfo("Fetch Status", "Data fetched successfully")
    except mysql.connector.Error as e:
        # Handle database connection errors or query errors
        messagebox.showerror("Database Error", f"An error occurred: {e}")
    finally:
        # Close database connection
        if 'myCur' in locals():
            myCur.close()
        if 'mydb' in locals():
            mydb.close()

def updateData(enterID, enterName, enterDept, listBox,):
    id = enterID.get()

    name = enterName.get()
    dept = enterDept.get()
    if id == "" or name == "" or dept == "":
        messagebox.showwarning("Cannot update",
                               "All three fields, employee id, employee name and employee dept are required to update en employee entry")
    else:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv("DB_PASSWORD"),
            database="employee"
        )
        myCur = mydb.cursor()
        check_query = "SELECT * FROM empDetails WHERE empID = %s"
        myCur.execute(check_query, (id,))
        result = myCur.fetchone()

        if result is None:  # If no record is found with the given empID
            messagebox.showerror("Update Error", "Employee ID must exist to update the entry")
        else:
            sql = "UPDATE empDetails SET empName = %s, empDept = %s WHERE empID = %s"
            myCur.execute(sql, (name, dept, id))
            mydb.commit()
            # Clear the names filled by the user in the gui so it is ready for next operation
            enterID.delete(0, END)
            enterName.delete(0, END)
            enterDept.delete(0, END)
            show(listBox)
            messagebox.showinfo("Update Status", "Data updated successfully")
        myCur.close()
        mydb.close()



def resetFields(enterID, enterName, enterDept):
    enterID.delete(0, END)
    enterName.delete(0, END)
    enterDept.delete(0, END)