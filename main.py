# This is a sample Python script.
from tkinter import *
from PIL import Image, ImageTk
import mysql.connector

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def addButtons(window):
    #Need buttons to insert, update, fetch, add, delete or reset
    insertBtn = Button(window,text="Insert", font=("Sans", 12), bg="white")
    insertBtn.place(x=20, y=160)
    updateBtn = Button(window,text="Update", font=("Sans", 12), bg="white")
    updateBtn.place(x=120, y=160)
    fetchBtn = Button(window,text="Fetch", font=("Sans", 12), bg="white")
    fetchBtn.place(x=220, y=160)
    addBtn = Button(window,text="Add", font=("Sans", 12), bg="white")
    addBtn.place(x=320, y=160)
    deleteBtn = Button(window,text="Delete", font=("Sans", 12), bg="white")
    deleteBtn.place(x=420, y=160)
    resetBtn = Button(window,text="Reset", font=("Sans", 12), bg="white")
    resetBtn.place(x=520, y=160)

def addLabels(window):
    #Need labels for employee ID, employee name and employee dept
    empID = Label(window,text="Employee ID", font=("Serif", 12))
    empID.place(x=20,y=30)
    empName = Label(window,text="Employee Name", font=("Serif", 12))
    empName.place(x=20,y=60)
    empDept = Label(window,text="Employee Dept", font=("Serif", 12))
    empDept.place(x=20,y=90)

def addEntry(window):
    enterID = Entry(window)
    enterID.place(x=170, y=30)
    enterName = Entry(window)
    enterName.place(x=170, y=60)
    enterDept = Entry(window)
    enterDept.place(x=170, y=90)

def gui():
    window = Tk()
    window.geometry("600x270")
    window.title("Employee CRUD App")
    addLabels(window)
    addEntry(window)
    addButtons(window)
    window.mainloop()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    gui()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
