from tkinter import *
from tkinter import messagebox
from utilities import show
from sql_database_ops import insertData, removeData, getData, updateData, resetFields

def addButtons(window,enterID, enterName, enterDept, listBox):
    #Need buttons to insert, update, fetch, delete and reset
    insertBtn = Button(window,text="Insert", font=("Sans", 12), bg="white",command=lambda: insertData(enterID, enterName, enterDept, listBox))
    insertBtn.place(x=20, y=160)
    updateBtn = Button(window,text="Update", font=("Sans", 12), bg="white",command=lambda: updateData(enterID, enterName, enterDept, listBox))
    updateBtn.place(x=80, y=160)
    fetchBtn = Button(window,text="Fetch", font=("Sans", 12), bg="white",command=lambda: getData(enterID, enterName, enterDept))
    fetchBtn.place(x=150, y=160)
    deleteBtn = Button(window,text="Delete", font=("Sans", 12), bg="white",command=lambda: removeData(enterID,enterName, enterDept, listBox))
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
    showData.place(x=330, y=30, width = 300)
    return showData

def crud_gui():
    window = Tk()
    window.geometry("800x470")
    window.title("Employee CRUD App")
    addLabels(window)
    enterID, enterName, enterDept = addEntry(window)
    listBox = listbox(window)
    addButtons(window, enterID, enterName, enterDept, listBox)
    show(listBox)
    window.mainloop()