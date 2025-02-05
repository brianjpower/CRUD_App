# This is a sample Python script.
import os
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def addButtons(window,enterID, enterName, enterDept, listBox):
    #Need buttons to insert, update, fetch, delete and reset
    insertBtn = Button(window,text="Insert", font=("Sans", 12), bg="white",command=lambda: insertData(enterID, enterName, enterDept, listBox))
    insertBtn.place(x=20, y=160)
    updateBtn = Button(window,text="Update", font=("Sans", 12), bg="white",command=lambda: updateData(enterID, enterName, enterDept, listBox))
    updateBtn.place(x=80, y=160)
    fetchBtn = Button(window,text="Fetch", font=("Sans", 12), bg="white",command=lambda: getData(enterID, enterName, enterDept))
    fetchBtn.place(x=150, y=160)
    deleteBtn = Button(window,text="Delete", font=("Sans", 12), bg="white",command=lambda: removeData(enterID,enterName, enterDept))
    deleteBtn.place(x=210, y=160)
    resetBtn = Button(window,text="Reset", font=("Sans", 12), bg="white", command=lambda: resetFields(enterID, enterName, enterDept))
    resetBtn.place(x=20, y=210)

def addLabels(window):
    #Need labels for employee ID, employee name and employee dept
    empID = Label(window,text="Employee ID", font=("Serif", 12))
    empID.place(x=20,y=30)
    empName = Label(window,text="Employee Name", font=("Serif", 12))
    empName.place(x=20,y=60)
    empDept = Label(window,text="Employee Dept", font=("Serif", 12))
    empDept.place(x=20,y=90)

def addEntry(window):
    #Need entry fields for empID, empName and empDept
    enterID = Entry(window)
    enterID.place(x=170, y=30)
    enterName = Entry(window)
    enterName.place(x=170, y=60)
    enterDept = Entry(window)
    enterDept.place(x=170, y=90)
    return enterID, enterName, enterDept  # Return the entry widgets for later use


def listbox(window):
    showData = Listbox(window)
    showData.place(x=330, y=30)
    return showData

def crud_gui():
    window = Tk()
    window.geometry("600x270")
    window.title("Employee CRUD App")
    addLabels(window)
    enterID, enterName, enterDept = addEntry(window)
    listBox = listbox(window)
    addButtons(window, enterID, enterName, enterDept, listBox)
    #insertData(enterID, enterName, enterDept)
    window.mainloop()

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

def removeData(enterID,enterName, enterDept):
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

def updateData(enterID, enterName, enterDept, window):
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
        listBox.insert(END, f"{'Employee ID':<15}{'Name':<25}{'Department':<15}")
        listBox.insert(END, "=" * 55)

        # Insert rows into the Listbox dynamically
        for row in records:
            listBox.insert(END, f"{row[0]:<15}{row[1]:<25}{row[2]:<15}")

    except mysql.connector.Error as e:
        # Handle database errors with a meaningful message
        messagebox.showerror("Database Error", f"An error occurred: {e}")
    finally:
        # Always close the database cursor and connection to avoid leaks
        if 'myCur' in locals():
            myCur.close()
        if 'mydb' in locals():
            mydb.close()

def resetFields(enterID, enterName, enterDept):
    enterID.delete(0, END)
    enterName.delete(0, END)
    enterDept.delete(0, END)


if __name__ == '__main__':
    crud_gui()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
