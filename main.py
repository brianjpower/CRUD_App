# This is a sample Python script.
from tkinter import *
from PIL import Image, ImageTk
import mysql.connector

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def gui():
    window = Tk()
    window.geometry("600x270")
    window.title("Employee CRUD App")
    empID = Label(window,text="Employee ID", font=("Serif", 12))
    empID.place(x=20,y=30)
    empName = Label(window,text="Employee Name", font=("Serif", 12))
    empName.place(x=20,y=60)
    empDept = Label(window,text="Employee Depart", font=("Serif", 12))
    empDept.place(x=20,y=90)
    window.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    gui()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
