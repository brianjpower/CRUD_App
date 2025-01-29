# This is a sample Python script.
import os
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def addButtons(window):
    #Need buttons to insert, update, fetch, delete and reset
    insertBtn = Button(window,text="Insert", font=("Sans", 12), bg="white",command=insertData)
    insertBtn.place(x=20, y=160)
    updateBtn = Button(window,text="Update", font=("Sans", 12), bg="white")
    updateBtn.place(x=80, y=160)
    fetchBtn = Button(window,text="Fetch", font=("Sans", 12), bg="white")
    fetchBtn.place(x=150, y=160)
    deleteBtn = Button(window,text="Delete", font=("Sans", 12), bg="white")
    deleteBtn.place(x=210, y=160)
    resetBtn = Button(window,text="Reset", font=("Sans", 12), bg="white")
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


def listBox(window):
    showData = Listbox(window)
    showData.place(x=330, y=30)

def crud_gui():
    window = Tk()
    window.geometry("600x270")
    window.title("Employee CRUD App")
    addLabels(window)
    enterID, enterName, enterDept = addEntry(window)
    addButtons(window)
    listBox(window)
    insertData(enterID, enterName, enterDept)
    window.mainloop()

def insertData(enterID, enterName, enterDept):
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
        sql = "INSERT INTO employees (empID, empName, empDept) VALUES (id, name, dept)"
        myCur.execute(sql)
        mydb.commit()

        #Clear the names filled by the user in the gui so it is ready for next operation
        enterID.delete(0, END)
        enterName.delete(0, END)
        enterDept.delete(0, END)
        messagebox.showinfo("Insert Status", "Data inserted successfully")
        myCur.close()
        mydb.close()

if __name__ == '__main__':
    crud_gui()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
